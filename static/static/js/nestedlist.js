
	$(document).on('click','.list-down-btn',function(event)
  {
  	event.preventDefault();
    var target = $(this).attr('data-toggle');
    //fire AJAX to load requests under sub service with subservice id
    var subservice_id = target.replace('#','');
    request_search_ajax(subservice_id);
    $(target).slideToggle();
    var clicked = event.target;
    $(clicked).toggleClass("fa-chevron-down  fa-chevron-up");
  });

  service_search_ajax(
        {
            'search_text': "",
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        }
    )

    subservice_search_ajax(
            {
                'search_text': "",
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            }
        )


    $(document).on('click', "#service-search-button", function(){
        service_search_ajax({
                'search_text': $('#service_search_input').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            })}
    );

    $(document).on('click', "#subservice-search-button", function(){
        subservice_search_ajax({
                'search_text': $('#subservice_search_input').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            })}
    );


    function service_search_ajax(json_data){
        console.log('event is: ' + event)
        $.ajax({
            type: "POST",
            url: "/searchservice",
            data: json_data,
            success: function(data) {
                //alert(data)
                $('#service_block').html(data);
            },
            error: function(data){
                //alert('Error Thrown')
                //$('#service_block').html(data);
            }
        });
    }


    function subservice_search_ajax(json_data){
        console.log('event is: ' + event)
        $.ajax({
            type: "POST",
            url: "/searchsubservice",
            data: json_data,
            success: function(data) {
                //alert(data)
                $('#subservice_block').html(data);
            },
            error: function(data){
                //alert('Error Thrown')
                //$('#service_block').html(data);
            }
        });
    }

    function request_search_ajax(subservice_id){
        console.log('event is: ' + event)
        $.ajax({
            type: "POST",
            url: "/searchrequest",
            data: {
                'subserviceid': subservice_id,
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data) {
                //alert(data)
                $('#'.concat(subservice_id)).html(data);
            },
            error: function(data){
                //alert('Error Thrown')
                //$('#service_block').html(data);
            }
        });
    }
