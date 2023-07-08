var quickElements = document.getElementsByClassName('quick');

for (var i = 0; i < quickElements.length; i++) {
    var quickElement = quickElements[i];
    quickElement.addEventListener('click', function() {
        var quickLinks = this.nextElementSibling;
        quickLinks.style.display = (quickLinks.style.display === 'flex') ? 'none' : 'flex';
        var arrowImage = this.querySelector('img');
        arrowImage.classList.toggle('rotate');
    });
}
