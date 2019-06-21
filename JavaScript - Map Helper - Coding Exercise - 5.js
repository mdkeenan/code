var paints = [ {color: 'red'}, {color: 'blue'}, {color: 'yellow'} ];
 
function pluck(paints /*array*/, color /*property*/) {
    var plucked = paints.map(function(paint) /* pass in variable to iterate over array objects*/ {
        return paint[color];
    });
    return plucked;
}

(pluck(paints, 'color'));
