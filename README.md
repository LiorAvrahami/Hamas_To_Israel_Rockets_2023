There is a theory that Hamas fires rockets only on full hours, so in order to check if this is true, I wrote a script that extracts all the alarms from the [National Emergency Portal website](https://www.oref.org.il/12481-en/Pakar.aspx). I extracted all the alarms that were in the last month and made a histogram to check if this is true. 

It turns out that this is really, really true, but sometimes they shoot on a half-full hour.
<table><tr>
<td><img src="https://github.com/LiorAvrahami/Hamas_To_Israel_Rockets_2023/blob/main/rockets_fire_on_hole_hours.png" width="300"></td>
<td><img src="https://github.com/LiorAvrahami/Hamas_To_Israel_Rockets_2023/blob/main/rockets_fire_on_hole_hours_ENG.png" width="300"></td>
</tr></table>
I also made a histogram of the distribution throughout the day (you can really see the spikes of the round and semi-round hours)
<table><tr>
<td><img src="https://github.com/LiorAvrahami/Hamas_To_Israel_Rockets_2023/blob/main/rocket_fire_throught_the_day.png" width="300"></td>
<td><img src="https://github.com/LiorAvrahami/Hamas_To_Israel_Rockets_2023/blob/main/rocket_fire_throught_the_day_ENG.png" width="300"></td>
</tr></table>

I'm working on also doing analysis on the location data, but I found no good way to map location name to real world coordinates
