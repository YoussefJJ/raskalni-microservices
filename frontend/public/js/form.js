$("#submit-btn").on("click", function (event) {
    event.preventDefault();
    console.log("here")
      var formData = {
        age: $("#age").val(),
        sex: $("input[name=sex]:checked").val(),
        description: $("#description").val(),
        salary: $("#salary").val(),
        experience: $("#experience").val(),
        duration: $("#duration").val(),
      };
  
      $.ajax({
        type: "POST",
        url: "http://localhost:5000",
        data: formData,
        dataType: "json",
        encode: true,
      }).done(function (data) {
        // add a success message
        $("#success").empty();
        // create message
        var message = $("<h2>");
        // add classes
        message.addClass(["text-center", "text-success", "mt-5", "border-2", "bg-green-400", "border-green-900", "p-3"])
        // add text
        message.text("Success!");
        $("#success").append(message);
        // clear form
        console.log(formData)
  });
});