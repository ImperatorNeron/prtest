function updateFileName(input) {
    let filename = input.files[0].name;
    for (let i = 1; i < input.files.length; i++){
        filename += `, ${input.files[i].name}`;
    }
    let label = input.closest('.form-field');
    label.querySelector('span').innerHTML = filename;
}