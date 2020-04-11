function get_date(date_str){
    var date_split = date_str.split(" ");
    var time_field = date_split[0] + " " + date_split[1][0] + date_split[1][2];
    /*
    var day_field = 1
    if(date_split.length > 3){
        day_field = date_split[3][0];
    }
    var temp = new Date('1970/01/0'+ day_field + ' ' + time_field);
    */
    var temp = new Date('1970/01/01 ' + time_field);
    return temp;
}

function sort_cell(x, y, is_asc){
    var x_str = x.innerHTML.toLowerCase();
    var y_str = y.innerHTML.toLowerCase();
    var is_time_cell = ~x_str.indexOf(".");  // check if date field
    var shouldSwitch = false;
    if(is_time_cell == 0){
        if (is_asc) {
            if (x_str > y_str) {
            // If so, mark as a switch and break the loop:
                shouldSwitch = true;
            }
        } else {
            if (x_str < y_str) {
            // If so, mark as a switch and break the loop:
                shouldSwitch = true;
            }
        }
    }
    else{
        var x_delta = get_date(x_str) - get_date(y_str);
        if (is_asc) {
            if (x_delta > 0) {
            // If so, mark as a switch and break the loop:
                shouldSwitch = true;
            }
        } else {
            if (x_delta < 0) {
            // If so, mark as a switch and break the loop:
                shouldSwitch = true;
            }
        }
    }
    
    return shouldSwitch;
}
