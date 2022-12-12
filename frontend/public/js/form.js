$(document).ready(function () {
    $("form").submit(function (event) {
      var formData = {
        name: $("#age").val(),
        email: $("#sex").val(),
        description: $("#description").val(),
        salary: $("#salary").val(),
        experience: $("#experience").val(),
      };
  
    //   $.ajax({
    //     type: "POST",
    //     url: "process.php",
    //     data: formData,
    //     dataType: "json",
    //     encode: true,
    //   }).done(function (data) {
    //     console.log(data);
    //   });
      console.log(formData)
      event.preventDefault();
    });
  });