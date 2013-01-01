var adaptive = {};

(function() {
    var eventBindings = {};
    var thresholds = [550, 979];
    var prevBracket = "";
    var thresholdBreaks = {
        550: 'small',
        979: 'medium',
        fallback: 'standard',
    }
    function switchClass(obj, className) {
        var classString = obj.className;
        var classList = classString.split(/\s+/);
        for (i in classList) {
            if (classList[i].match(/^adaptive-/)) {
                classList.splice(i, 1);
            }
        }
        classList.push(className);
        classString = classList.join(' ');
        obj.className = classString;
    }
    function adapt() {
        var width = window.innerWidth;
        var bracket = thresholdBreaks.fallback;
        for (i in thresholds) {
            if (window.innerWidth <= thresholds[i]) {
                bracket = thresholdBreaks[thresholds[i]];
                break;
            }
        }
        var body = document.documentElement;
        className = "adaptive-" + bracket;
        switchClass(body, className);
        // bindEvents(prevBracket, bracket);
        prevBracket = bracket;
    }

    function mobile() {
        return !!navigator.userAgent.match(/(mobile)|(iphone)/i)
    }

    if (!mobile()) {
        window.addEventListener('resize', adapt);
        adapt();
    } else {
        document.documentElement.addClass('adaptive_small')
    }

})();
