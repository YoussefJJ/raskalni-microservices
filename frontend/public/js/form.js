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
        console.log(data);
      });
      console.log(formData)
  });