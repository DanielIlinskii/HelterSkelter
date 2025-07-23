

// Mobile menu toggle
function toggleMobileMenu() {
    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("mobileOverlay");

    sidebar.classList.toggle("active");

    if (sidebar.classList.contains("active")) {
        overlay.style.display = "block";
        document.body.style.overflow = "hidden";
    } else {
        overlay.style.display = "none";
        document.body.style.overflow = "auto";
    }
}

// Calendar Functionality
let currentDate = new Date();
const monthNames = [
    "Январь",
    "Февраль",
    "Март",
    "Апрель",
    "Май",
    "Июнь",
    "Июль",
    "Август",
    "Сентябрь",
    "Октябрь",
    "Ноябрь",
    "Декабрь",
];
let selectedDate = null;
let selectedTime = null;
let selectedMaster = null;

// Initialize calendar
function initCalendar() {
    updateCalendarHeader();
    renderCalendar();

    // Set up event listeners for month navigation
    document
        .getElementById("prevMonth")
        .addEventListener("click", function () {
            currentDate.setMonth(currentDate.getMonth() - 1);
            updateCalendarHeader();
            renderCalendar();
        });

    document
        .getElementById("nextMonth")
        .addEventListener("click", function () {
            currentDate.setMonth(currentDate.getMonth() + 1);
            updateCalendarHeader();
            renderCalendar();
        });

    // Set up form submission
    document
        .getElementById("bookingForm")
        .addEventListener("submit", function (e) {
            e.preventDefault();

            if (!selectedDate || !selectedTime || !selectedMaster) {
                alert("Пожалуйста, выберите дату, время и мастера");
                return;
            }
            // если не выбран один из трех параметров, то выдаем ошибку с этим параметром
            // if (!selectedDate) {
            //     alert("Пожалуйста, выберите дату");
            //     return;
            // }
            // if (!selectedTime) {
            //     alert("Пожалуйста, выберите время");
            //     return;
            // }
            // if (!selectedMaster) {
            //     alert("Пожалуйста, выберите мастера");
            //     return;
            // }

            // Simulate form submission
            const submitBtn = this.querySelector(".form-submit");
            const originalText = submitBtn.textContent;

            submitBtn.textContent = "Обработка...";
            submitBtn.disabled = true;

            setTimeout(() => {
                submitBtn.textContent = "Запись создана!";
                submitBtn.style.background = "var(--success)";

                setTimeout(() => {
                    submitBtn.textContent = originalText;
                    submitBtn.disabled = false;
                    submitBtn.style.background = "";
                    this.reset();

                    // Reset selection
                    selectedDate = null;
                    selectedTime = null;
                    selectedMaster = null;
                    document.getElementById("selectedDateTimeValue").textContent =
                        "Пожалуйста, выберите в календаре";

                    // Reset master selection
                    document.querySelectorAll(".master-item").forEach((item) => {
                        item.classList.remove("selected");
                    });
                }, 2000);
            }, 1500);
        });
}

function updateCalendarHeader() {
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();
    document.getElementById(
        "currentMonth"
    ).textContent = `${monthNames[month]} ${year}`;
}

/**
 * Отрисовывает календарь на текущий месяц.
 * Основное изменение: показываются только дни текущего месяца,
 * дни предыдущего и следующего месяцев заменены на пустые ячейки для
 * сохранения структуры сетки календаря.
 */
function renderCalendar() {
    const calendarDays = document.getElementById("calendarDays");
    calendarDays.innerHTML = "";

    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();

    // Получаем первый день месяца
    const firstDay = new Date(year, month, 1);

    // Определяем день недели для первого дня (0 - воскресенье, 1 - понедельник, и т.д.)
    let firstDayOfWeek = firstDay.getDay();
    // Преобразуем в формат, где понедельник - первый день (0), воскресенье - последний (6)
    firstDayOfWeek = firstDayOfWeek === 0 ? 6 : firstDayOfWeek - 1;

    // Количество дней в текущем месяце
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    // Создаем пустые ячейки для заполнения дней недели до первого дня месяца
    // Вместо отображения дней предыдущего месяца используем скрытые ячейки
    for (let i = 0; i < firstDayOfWeek; i++) {
        const dayElement = document.createElement("div");
        dayElement.className = "calendar-day";
        dayElement.style.visibility = "hidden"; // Делаем ячейки невидимыми, но сохраняем структуру сетки
        calendarDays.appendChild(dayElement);
    }

    // Текущая дата для выделения сегодняшнего дня
    const today = new Date();
    const isCurrentMonth =
        today.getMonth() === month && today.getFullYear() === year;

    // Добавляем только дни текущего месяца
    for (let i = 1; i <= daysInMonth; i++) {
        const dayElement = document.createElement("div");
        dayElement.className = "calendar-day";
        dayElement.textContent = i;

        // Отмечаем сегодняшний день
        if (isCurrentMonth && i === today.getDate()) {
            dayElement.classList.add("today");
        }
        // Отмечаем все даты до сегодняшнего дня как прошедшие и их нельзя выбрать
        if (isCurrentMonth && i < today.getDate()) {
            dayElement.classList.add("unavailable");
        }


        dayElement.addEventListener("click", function () {
            // Снимаем выделение с предыдущего выбранного дня
            document
                .querySelectorAll(".calendar-day.selected")
                .forEach((day) => {
                    day.classList.remove("selected");
                });

            // Отмечаем текущий день как выбранный
            this.classList.add("selected");


            // Обновляем выбранную дату если день доступен
            if (this.classList.contains("unavailable")) {
                return;
            } else {
                selectedDate = new Date(year, month, i);
                updateSelectedDateTime();

                // Генерируем доступные временные слоты
                generateTimeSlots();
            }

        });


        calendarDays.appendChild(dayElement);
    }

    // Вычисляем количество ячеек для заполнения оставшихся строк календаря
    // Чтобы сохранить структуру сетки, но не показывать дни следующего месяца
    const totalDaysDisplayed = firstDayOfWeek + daysInMonth;
    const remainingCells = 7 - (totalDaysDisplayed % 7);

    // Добавляем пустые ячейки в конце, если нужно
    // Вместо отображения дней следующего месяца также используем скрытые ячейки
    if (remainingCells < 7) {
        for (let i = 0; i < remainingCells; i++) {
            const dayElement = document.createElement("div");
            dayElement.className = "calendar-day";
            dayElement.style.visibility = "hidden"; // Делаем ячейки невидимыми
            calendarDays.appendChild(dayElement);
        }
    }

    // Очищаем временные слоты при смене месяца
    document.getElementById("timeSlots").innerHTML = "";
}

function generateTimeSlots() {
    const timeSlotsContainer = document.getElementById("timeSlots");
    timeSlotsContainer.innerHTML = "";

    // Если дата не выбрана, не генерируем слоты
    if (!selectedDate) return;

    // Время работы студии с 10:00 до 20:00
    const startHour = 10;
    const endHour = 20;

    // Интервал между слотами - 1 час
    for (let hour = startHour; hour < endHour; hour++) {
        // Создаем два слота на каждый час (целый час и половина)
        for (let minute of [0, 30]) {
            const timeSlot = document.createElement("div");
            timeSlot.className = "time-slot";

            // Форматируем время
            const timeString = `${hour}:${minute === 0 ? "00" : minute}`;
            timeSlot.textContent = timeString;

            // Добавляем обработчик событий для выбора времени
            timeSlot.addEventListener("click", function () {
                // Снимаем выделение с предыдущего выбранного слота
                document
                    .querySelectorAll(".time-slot.selected")
                    .forEach((slot) => {
                        slot.classList.remove("selected");
                    });

                // Отмечаем текущий слот как выбранный
                this.classList.add("selected");

                // Обновляем выбранное время
                selectedTime = timeString;
                updateSelectedDateTime();
            });

            timeSlotsContainer.appendChild(timeSlot);
        }
    }
}

function updateSelectedDateTime() {
    const selectedDateTimeElement = document.getElementById(
        "selectedDateTimeValue"
    );

    if (selectedDate) {
        // Форматируем дату
        const day = selectedDate.getDate();
        const month = monthNames[selectedDate.getMonth()];
        const year = selectedDate.getFullYear();

        if (selectedTime) {
            selectedDateTimeElement.textContent = `${day} ${month} ${year}, ${selectedTime}`;
        } else {
            selectedDateTimeElement.textContent = `${day} ${month} ${year}, время не выбрано`;
        }
    } else {
        selectedDateTimeElement.textContent =
            "Пожалуйста, выберите в календаре";
    }
}

// function selectMaster(element) {
//     // Снимаем выделение с предыдущего выбранного мастера
//     document.querySelectorAll(".master-item.selected").forEach((item) => {
//         item.classList.remove("selected");
//     });

//     // Отмечаем текущего мастера как выбранного
//     element.classList.add("selected");

//     // Обновляем выбранного мастера
//     selectedMaster = element.getAttribute("data-master");
// }

// Initialize calendar when DOM is loaded
document.addEventListener("DOMContentLoaded", initCalendar);
