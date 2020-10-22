// Add datatables to history table
$(() => {
  $("#sales").DataTable({
    searching: true,
    scrollX: false,
    scrollCollapse: false,
    iDisplayLength: 10,
    order: [[0, "desc"]],
  });
});