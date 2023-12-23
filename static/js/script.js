document.addEventListener('DOMContentLoaded', function() {
    var lis = document.querySelectorAll('#myNavbar li');
    lis.forEach(function(li) {
        li.addEventListener('click', function() {
            setActive(this);
        });
    });

    function setActive(element) {
        lis.forEach(function(li) {
            li.classList.remove('active');
        });

        element.classList.add('active');
    }
});