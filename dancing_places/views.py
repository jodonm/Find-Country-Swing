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
        ([21.37831223400282, -157.93514207193752], "Whiskey Dix Saloon: Only country bar in Hawaii. Lots of dancers from Pearl Harbor. Very welcoming group with lots of dancing. $5 cover. <a href='https://whiskeydixhi.com' target='_blank'>Website</a>"),
        ([44.085139727957895, -121.29494206647543], "The Cross-Eyed Cricket Watering Hole: Only country bar in Bend. Younger crowd with lots or regulars. Lots of line-dancing. <a href='https://www.thecrosseyedcricketbend.com' target='_blank'>Website</a>"),
        ([30.26260567021625, -97.72699678443963], "The White Horse: Honky Tonk with live music, the dance style here is closer to what you find on the west-coast than traditional Texas two-step. Very welcoming crowd. $10 cash only cover. <a href='https://www.thewhitehorseaustin.com/events' target='_blank'>Website</a>"),
        ([30.240884013131655, -97.78520732429344], "The Broken Spoke: Traditional Texas Honky Tonk. This bar has lots of historical significance with artists like Willie Nelson and George Strait playing here in their youth. $10 cash only cover for the dance floor, bar area is free. <a href='https://www.brokenspokeaustintx.net/' target='_blank'>Website</a>"),
        ([30.083975942492884, -97.82635428177994], "Mavericks Dance Hall in Buda: Very large dance floor with DJ most nights. Younger crowd. Very modern with projector screens and light shows, has good A/C. $7 Cover. <a href='http://mavericksdancehall.com/' target='_blank'>Website</a>"),
        ([36.19854952092901, -86.2908059147214], "Cahoots Dancehall and Honkytonk: Home of free beer. Large dance floor and very very popular. Has a younger crowd. DJ will call out which songs are line dance only or swing dance only. $15 cover but free beer until midnight <a href='http://cahootslebanon.com/' target='_blank'>Website</a>"),
        ([36.162732795662244, -86.77543145737778], "Wildhorse Saloon: This was one of the only places to dance on Music Row, very large dance floor and live music. It is currently being transformed into Luke Combs bar. <a href='https://www.category10.com' target='_blank'>Website</a>"),

        # Add more custom locations with their descriptions
    ]

    # Create the map with custom markers 
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
    return render(request, 'dancing_places/form_page.html')

def submission_success(request):
    return render(request, 'success.html')

def redirect_to_map(request, exception=None):
    return redirect('map')