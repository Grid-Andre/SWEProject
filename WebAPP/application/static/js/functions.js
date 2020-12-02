function cal(baseCal, hr, min, weight)
{
    duration = (hr*60) + min;

    switch(weight){
        case weight >= 125 && weight < 155:
            calories = duration * baseCal
            break;
        case weight >= 155 && weight < 185:
            calories = duration * baseCal
            break;
        case weight > 185:
            calories = duration * baseCal
            break;
    }

    output = document.getElementById("test")
   
}