function validateForm() {
    let isValid = true;
    let title = document.getElementById("title").value.trim();
    let location = document.getElementById("location").value.trim();
    let startDate = document.getElementById("start_date").value;
    let endDate = document.getElementById("end_date").value;
    let capacity = document.getElementById("capacity").value.trim();
    let ticketPrice = document.getElementById("ticket_price").value.trim();

    clearErrors();

    const titleRegex = /^[a-zA-Z0-9\s]+$/;
    const locationRegex = /^[a-zA-Z0-9\s,.-]+$/;

    if (title === "") {
        document.getElementById("titleError").innerText = "Title is required.";
        isValid = false;
    } else if (!titleRegex.test(title)) {
        document.getElementById("titleError").innerText = "Title contains invalid characters.";
        isValid = false;
    }

    if (location === "") {
        document.getElementById("locationError").innerText = "Location is required.";
        isValid = false;
    } else if (!locationRegex.test(location)) {
        document.getElementById("locationError").innerText = "Location contains invalid characters.";
        isValid = false;
    }

    if (startDate === "") {
        document.getElementById("startDateError").innerText = "Start date is required.";
        isValid = false;
    }

    if (endDate === "") {
        document.getElementById("endDateError").innerText = "End date is required.";
        isValid = false;
    }

    if (startDate && endDate && new Date(startDate) >= new Date(endDate)) {
        document.getElementById("endDateError").innerText = "End date must be after start date.";
        isValid = false;
    }

    if (capacity === "" || capacity === "0") {
        document.getElementById("capacityError").innerText = "Capacity is required.";
        isValid = false;
    } else if (!/^\d+$/.test(capacity) || parseInt(capacity) <= 0) {
        document.getElementById("capacityError").innerText = "Capacity must be a positive whole number.";
        isValid = false;
    }

    if (ticketPrice === "0") {
        document.getElementById("ticketPriceError").innerText = "Leave the field empty for free events.";
        isValid = false;
    } else if (!/^\d+$/.test(ticketPrice) || parseInt(ticketPrice) < 0) {
        document.getElementById("ticketPriceError").innerText = "Ticket price must be a non-negative whole number.";
        isValid = false;
    }

    return isValid;
}

function clearErrors() {
    document.getElementById("titleError").innerText = "";
    document.getElementById("locationError").innerText = "";
    document.getElementById("startDateError").innerText = "";
    document.getElementById("endDateError").innerText = "";
    document.getElementById("capacityError").innerText = "";
    document.getElementById("ticketPriceError").innerText = "";
}
