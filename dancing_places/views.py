from django.shortcuts import render, redirect
import folium
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SpotForm
from django.contrib import messages


def map_view(request):
    # Define custom locations (same as in your Streamlit app)
    locations_data = [
        ([46.73489782122985, -117.00119446375352], "Moose Lodge: Dance hall popular with university students. Dancing every Wednesday night from 9PM-12AM when school is in session. $5 cover. <a href='https://www.facebook.com/Palousecountryswing' target='_blank'>Facebook</a>"),
        ([47.707297013906306, -117.03240164407349], "Nashville North: Country Bar. Live music and dancing Friday & Saturday night. $5 Cover. <a href='https://www.thenashvillenorth.com' target='_blank'>Website</a>"),
        ([43.620422691638765, -116.30959909439918], "CLOSED. The Buffalo Club: Country Bar. Live music and dancing. Older music. Also popular with other swing styles. <a href='http://thebuffaloclubboise.com/' target='_blank'>Website</a>"),
        ([43.49129480402318, -116.42184487417322], "127 Saloon: Popular country swing bar. Small dance floor but lots of talented dancers. <a href='http://127saloon.com/' target='_blank'>Website</a>"),
        ([48.371103555952686, -114.24033149339925], "Blue Moon Nite Club: Popular bar with locals. Not always a country band but still the best place to dance on weekends."),
        ([47.60170817943568, -122.63077979283953], "McClouds Grill House: Best bar in the Kitsap area for country swing dancing. <a href='https://mccloudsgrillhouse.com/' target='_blank'>Website</a>"),
        ([45.68771311088347, -111.04463165736743], "Bourbon: Popular spot for country swing dancing on Saturday nights <a href='http://www.bourbonmt.com/' target='_blank'>Website</a>"),
        ([43.61400379346505, -116.2012090487591], "Dirty Little Roddy's: Very popular night club with western theme. Not the best for country dancing but you might see some when it's less crowded. <a href='https://dirtylittleroddys.com/' target='_blank'>Website</a>"),
        ([39.795162070087386, -104.98699700682839], "The Grizzly Rose: Popular country bar with live country music Tuesday-Sunday. Frequently hosts concerts. Has lessons several times throughout the week. <a href='https://www.grizzlyrose.com/' target='_blank'>Website</a>"),
        ([39.6723121325138, -104.86528727753583], "Stampede: Large dance floor. Wednesday night is country night with line-dance lessons. <a href='https://www.stampedeclub.net/' target='_blank'>Website</a>"),
        ([40.69926787373029, -111.9392146616003], "Westerner Club: Popular for country swing and other swing styles. Lessons Wednesday through Saturday <a href='http://www.westernerslc.com/' target='_blank'>Website</a>"),
        ([46.20845072481442, -119.12093024559294], "Branding Iron: Live bands and line dance lessons Friday & Saturday <a href='https://brandingironnightclub.com/' target='_blank'>Website</a>"),
        ([45.3799076112494, -122.7608340607681], "Bushwackers: Largest country swing bar in Portland. Lessons Thursday through Saturday <a href='http://www.bushwhackerssaloon.com/' target='_blank'>Website</a>"),
        ([45.59734393114103, -122.66874347632411], "Ponderosa Bar & Grill (AKA Jubitz): Country swing dancing at a truck-stop bar. Old-timey feel. <a href='http://jubitz.com/ponderosa-lounge-country-bar/' target='_blank'>Website</a>"),
        # Add more custom locations with their descriptions
    ]

    # Create the map with custom markers (logic adapted from your Streamlit app)
    if locations_data:
        locations = [location for location, _ in locations_data if location]
        map_center = [sum([lat for lat, _ in locations]) / len(locations), sum([lon for _, lon in locations]) / len(locations)]
        
        min_lon, max_lon = -200, 60
        min_lat, max_lat = -10, 90


        folium_map = folium.Map(
            location=map_center,
            zoom_start=5, 
            zoom_control=False, 
            max_bounds=True, 
            min_lat=min_lat,
            max_lat=max_lat,
            min_lon=min_lon,
            max_lon=max_lon,
            )
        folium.TileLayer('OpenStreetMap', no_wrap=True).add_to(folium_map)

        for location, popup_content in locations_data:
            folium.Marker(
                location,
                popup=folium.Popup(popup_content, max_width=300)
            ).add_to(folium_map)

        # Convert map to HTML
        map_html = folium_map._repr_html_()

        # Pass the map HTML to the template
        return render(request, 'dancing_places/map_display.html' , {'map_html': map_html})

    else:
        # If no locations, just render an empty page or a message
        return render(request, 'dancing_places/map_display.html', {'map_html': 'No locations to display'})


def about_view(request):
    return render(request, 'dancing_places/about.html')

# legacy code for internal user submit form, replaced by redirect to google form
# def add_spot(request):
#     if request.method == 'POST':
#         form = SpotForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('submission_success')  # Redirect to the success page
#         else:
#             # This else block is optional and can be used to provide feedback on why the form is not valid
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = SpotForm()
#     return render(request, 'add_spot.html', {'form': form})

# def add_spot(request):
#     return render(request, 'dancing_places/form.html')

def add_spot(request):
    return render(request, 'dancing_places/redirect.html')

def submission_success(request):
    return render(request, 'success.html')

def redirect_to_map(request, exception=None):
    return redirect('map')