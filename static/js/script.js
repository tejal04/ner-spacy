$(document).ready(function() {
    $("th").click(function() {
        var table = $(this).closest("table");
        var columnIndex = $(this).index();
        var rows = table.find("tbody > tr").get();

        rows.sort(function(a, b) {
            var aValue = $(a).find("td").eq(columnIndex).text();
            var bValue = $(b).find("td").eq(columnIndex).text();

            return aValue.localeCompare(bValue);
        });

        table.children("tbody").empty().append(rows);
    });
});