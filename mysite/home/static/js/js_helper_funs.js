// arrow_active_color = ['&#9652', '&#9662'];
//arrow_deactive_color = ['&#9653', '&#9663'];
arrow_active_color = ['\u25b4', '\u25be'];
arrow_deactive_color = ['\u25b5', '\u25bf'];

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

function sortTable(table_id, n, is_asc){
    // sort function
    var table = document.getElementById(table_id);
    var rows, i, x, y, shouldSwitch = 0;
    var switching = true;
    /* Make a loop that will continue until
    no switching has been done: */
    while (switching) {
        // Start by saying: no switching is done:
        switching = false;
        rows = table.rows;
        /* Loop through all table rows (except the
        first, which contains table headers): */
        for (i = 1; i < (rows.length - 1); i++) {
            // Start by saying there should be no switching:
            // shouldSwitch = false;
            /* Get the two elements you want to compare,
            one from current row and one from the next: */
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];
            /* Check if the two rows should switch place,
            based on the direction, asc or desc: */
            shouldSwitch = sort_cell(x, y, is_asc);
            if(shouldSwitch){break;}
        }
        if (shouldSwitch) {
            /* If a switch has been marked, make the switch
            and mark that a switch has been done: */
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            // Each time a switch is done, increase this count by 1:
        } 
    }
}
