$(document).ready(function() {
    $('a.abstract').click(function() {
        $(this).parent().parent().find(".abstract.hidden").toggleClass('open');
    });
    $('a.bibtex').click(function() {
        $(this).parent().parent().find(".bibtex.hidden").toggleClass('open');
    });
    $('a').removeClass('waves-effect waves-light');

    $('.pron-play-btn').each(function() {
        var btn = $(this);
        var audio = new Audio(btn.data('audio'));
        var icon = btn.find('i');

        btn.click(function() {
            audio.currentTime = 0;
            audio.play();
            icon.removeClass('fa-play').addClass('fa-pause');
            btn.addClass('playing');
        });

        audio.addEventListener('ended', function() {
            icon.removeClass('fa-pause').addClass('fa-play');
            btn.removeClass('playing');
        });
    });
});