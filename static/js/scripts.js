var removedItem,
    sum = 0;

$(function(){
    // calculate the values at the start
    calculatePrices();

    // Click to remove an item
    $(document).on("click", "a.remove", function() {
        removeItem.apply(this);
    });

    // Undo removal link click
    $(document).on("click", ".removeAlert a", function(){
        // insert it into the table
        addItemBackIn();
        //remove the removal alert message
        hideRemoveAlert();
    });

    $(document).on("change", "input.quantity", function(){
        var val = $(this).val(),
            pricePer,
            total

        if ( val <= "0") {
            removeItem.apply(this);
        } else {
            // reset the prices
            sum = 0;

            // get the price for the item
            pricePer = $(this).parents("td").prev("td").text();
            // set the pricePer to a nice, digestable number
            pricePer = formatNum(pricePer);
            // calculate the new total
            total = parseFloat(val * pricePer).toFixed(0);
            // set the total cell to the new price
            $(this).parents("td").siblings(".itemTotal").text(total + " تومان ");

            // recalculate prices for all items
            calculatePrices();
        }
    });

});


function removeItem() {
    // store the html
    removedItem = $(this).closest("tr").clone();
    // fade out the item row
    $(this).closest("tr").fadeOut(500, function() {
        $(this).remove();
        sum = 0;
        calculatePrices();
    });
    // fade in the removed confirmation alert
    $(".removeAlert").fadeIn();

    // default to hide the removal alert after 5 sec
    setTimeout(function(){
        hideRemoveAlert();
    }, 5000);
}

function hideRemoveAlert() {
    $(".removeAlert").fadeOut(500);
}

function addItemBackIn() {
    sum = 0;
    $(removedItem).prependTo("table.items tbody").hide().fadeIn(500)
    calculatePrices();
}

function updateSubTotal(){
    $("table.items td.itemTotal").each(function(){
        var value = $(this).text();
        // set the pricePer to a nice, digestable number
        value = formatNum(value);

        sum += parseFloat(value);
        $("table.pricing td.subtotal").text(sum.toFixed(0) + " تومان ");
    });
}

function addTax() {
    var tax = parseFloat(sum * 0).toFixed(0);
    $("table.pricing td.tax").text(tax + " تومان ");
}

function calculateTotal() {
    var subtotal = $("table.pricing td.subtotal").text(),
        tax = $("table.pricing td.tax").text(),
        shipping = $("table.pricing td.shipping").text(),
        total;

    subtotal = formatNum(subtotal);
    tax = formatNum(tax);
    shipping = formatNum(shipping);

    total = (subtotal + tax + shipping).toFixed(0);

    $("table.pricing td.orderTotal").text(total + " تومان ");
}

function calculatePrices() {
    updateSubTotal();
    addTax();
    calculateTotal();
}

function formatNum(num) {
    return parseFloat(num.replace(/[^0-9-.]/g, ''));
}