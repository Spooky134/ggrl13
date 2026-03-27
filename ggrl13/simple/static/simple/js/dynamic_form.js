$(document).ready(function () {
    let counter = 1;

    $('#add-input').click(function () {
        let newInput = `
            <div class="input-item">
                <input type="text" name="name_${counter}" placeholder="Enter the value">
            </div>
        `;
        $('#inputs-container').append(newInput);
        counter++;
    });
});