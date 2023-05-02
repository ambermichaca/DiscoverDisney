############################STANDARD THINGS WE NEED##############################
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

####################################VARIABLES####################################
current_id = 10
rides = {
    "1":{
        "id": "1",
        "title": "Haunted Mansion",
        "image": "https://allears.net/wp-content/uploads/2019/08/Haunted-Mansion-Madame-Renata-Ghost-Halloween-Lighting-Mickeys-Not-So-Scary-Halloween-Party-MNSSHP-2.jpg",
        "description": "The disembodied voice of the Ghost Host is your private guide through the cadaverous realm of an eerie haunted estate, home to ghosts, ghouls and supernatural surprises.Glide past a casket-filled conservatory, Madame Leotas chilling séance room and a ghostly graveyard of singing specters as you attempt to find your way out. Beware of hitchhikers—these phantom pranksters may follow you home.A musical crypt, a leaky tomb and a ghostly writer are among the creepy haunts youll find outside the main entrance.",
        "video": "https://www.youtube.com/embed/WuYp0-m9pOs?start=41",
        "alt_video_text" : "a virtual tour of the Hunted Mansion",
        "captions" : "/static/vtt/huntedMansion.vtt",
        "accesibility": ["Must Transfer from Wheelchair/ECV", "Audio Description", "Handheld Captioning"], 
        "neighborhood": "Liberty Square, Magic Kingdom Park", 
        "alt_text": "An exterior view of the Haunted Mansion attraction at Magic Kingdom. The Victorian-style building is adorned with Gothic features, including a tower with a weathervane and a wrought-iron fence surrounding a garden. A ghostly carriage and a hearse are parked outside the mansion's entrance, and a few trees and shrubs frame the scene."
    },
    "2":{
        "id": "2",
        "title": "Dumbo the Flying Elephant",
        "image": "https://live.staticflickr.com/4704/39920275892_7270734fb7_b.jpg",
        "description": "Based on the 1941 Disney animated masterpiece Dumbo, this classic attraction lets you hop atop everybodys favorite circus elephant as he discovers he can fly. Dumbos faithful friend Timothy Q. Mouse helps keeps you aloft with his “magic” feather. As the jubilant organ melody begins, lift off for a graceful cruise around (and around and around) Storybook Circus. You can adjust your altitude during your flight, so you can soar high or swoop low.",
        "video" : "https://www.youtube.com/embed/9PyxUbaoCYs?start=03",
        "alt_video_text" : "a virtual tour of Dumbo Flying Elephant ride",
        "captions" : "/static/vtt/dumbo.vtt",
        "accesibility": ["Must Transfer from Wheelchair/ECV"], 
        "neighborhood": "Fantasyland, Magic Kingdom Park", 
        "alt_text": "A photo of the Dumbo the Flying Elephant ride at Magic Kingdom, featuring rows of colorful flying elephants on a spinning platform. Children and families can be seen riding in the elephants with smiles on their faces." 

    },
    "3":{
        "id": "3",
        "title": "Big Thunder Mountain Railroad",
        "image": "https://www.disneyfoodblog.com/wp-content/uploads/2021/09/2021-wdw-disney-world-atmosphere-magic-kingdom-frontierland-big-thunder-mountain-railroad2.jpg",
        "description": "Legend has it that soon after gold was first discovered here in the 1850s, eerie things began to happen. Trains would take off and race through tunnels—by themselves.After you arrive at the legendary Big Thunder Mining Company, descend into an abandoned mine shaft and board your train. As you enter the cursed cavern, the engine speeds up along the rickety track. Dodge exploding dynamite and falling boulders as you swoop around turns, drop into canyons and dart through the mysterious ghost town of Tumbleweed. Big Thunder Mountain Railroad is a fast roller coaster-type attraction designed for kids and adults. However, some parts of this attraction are bumpy and, in some instances, take place in the dark.",
        "alt_video_text" : "a virtual tour of Thunder Mountain",
        "video" : "https://www.youtube.com/embed/_UbdTL5PiA0?start=2",
        "captions" : "/static/vtt/thundermountain.vtt",
        "accesibility": ["Must Transfer from Wheelchair/ECV", "For safety, you should be in good health and free from high blood pressure, heart, back or neck problems, motion sickness, or other conditions that could be aggravated by this adventure. Expectant mothers should not ride."],
        "neighborhood": "Frontierland, Magic Kingdom Park",
        "alt_text": "An action-packed roller coaster ride at Magic Kingdom called Big Thunder Mountain Railroad. The train cars can be seen speeding through a rugged landscape with rock formations, tunnels, and steep drops." 

    },
    "4":{
        "id": "4",
        "title": "It's a Small World",
        "image": "https://wdwmagic.twic.pics/ElementGalleryItems/attractions/Fullsize/Its-A-Small-World_Full_27515.jpg",
        "description": "Sing along to the classic anthem of world peace during a delightful musical boat tour. Cruise along the Seven Seaways Waterway on a gentle 10-minute journey through all 7 continents. Pass through vivid, fantastical scenes representing the iconic sights and sounds of dozens of nations. Behold a cast of dancing darlings from nearly every corner of the globe and watch as the Audio-Animatronics figures achieve universal harmony as they sing one song in many languages.",
        "video" : "https://www.youtube.com/embed/BvXhhw-nuuk?start=82",
        "alt_video_text" : "a virtual boat tour of It's a Small World",
        "captions" : "/static/vtt/smallworld.vtt",
        "accesibility": ["Must Transfer to Wheelchair", "Audio Description", "Handheld Captioning"], 
        "neighborhood": "Fantasyland, Magic Kingdom Park",
        "alt_text": "A brightly colored boat ride through a whimsical and diverse world of animatronic characters in traditional clothing, singing and dancing to the classic song 'It's a Small World.' The ride features different scenes from various countries, including Asia, Africa, Europe, and the Americas, all depicting cultural elements unique to each region. The iconic clock tower with moving dolls is also visible in the background." 

    }, 
    "5":{
        "id": "5",
        "title": "Walt Disney's Enchanted Tiki Room",
        "image": "http://www.wdw-magazine.com/wp-content/uploads/2017/08/ATTRACTION-2-JUDD.jpg",
        "description": "Sing along with a lively menagerie of exotic birds, flowers and Tiki statues in this jubilant Disney classic. A feast for your eyes and ears, this theater-in-the-round show invites you to sit back, relax and experience the beauty of the South Pacific with a cast of over 225 choreographed Audio-Animatronics performers.",
        "video" : "https://www.youtube.com/embed/8PAfghcKhs0?start=374",
        "alt_video_text" : "a virtual tour of the Tiki Room",
        "captions" : "/static/vtt/tiki.vtt",
        "accesibility": ["May Remain in Wheelchair/ECV", "Handheld Captioning", "Audio Description", "Assistive Listening"], 
        "neighborhood": "Adventureland, Magic Kingdom Park",
        "alt_text": "An interior shot of Walt Disney's Enchanted Tiki Room. Animatronic birds are perched on wooden branches and are brightly colored in shades of blue, green, yellow, and red. The flowers are also brightly colored in shades of pink, orange, and purple, and are positioned on green stalks." 

    }, 
    "6":{
        "id": "6",
        "title": "Pirates of the Caribbean", 
        "image": "https://variety.com/wp-content/uploads/2018/03/pirates-of-the-caribbean-disney-world.jpg",
        "description": "Set sail on a swashbuckling voyage to a long-forgotten time and place when pirates and privateers ruled the seas.",
        "video" : "https://www.youtube.com/embed/F4D8J4dBFMg?start=18",
        "alt_video_text" : "a virtual tour of Thunder the Pirates of the Caribbean",
        "captions" : "/static/vtt/pirates.vtt",
        "rider": ["Any Height", "All ages"],
        "accesibility": ["Slow Rides", "Small Drops", "Dark", "Must Transfer to Wheelchair, Then to Ride Vehicle", "Audio Description", "Handheld Captioning"],
        "neighborhood": "Adventureland, Magic Kingdom Park", 
        "alt_text": "A dark and adventurous boat ride through a 17th century pirate-infested Caribbean town, complete with cannon blasts, singing pirates, and lots of water."
        },

    "7":{
        "id": "7",
        "title": "TRON Lightcycle Run", 
        "image": "https://www.travelandleisure.com/thmb/x1I3aHz-7-p_daJdIEbgbkKAuz8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/TAL-disney-world-tron-cycle-ride-WDWTRON0123-14983ed5ee884369ac993ec0627cb830.jpg",
        "description": "Speed across a world with no horizons in a high-stakes race based on the Disney sci-fi film TRON: Legacy.",
        "video" : "https://www.youtube.com/embed/kcxdAZa__2A?start=6",
        "alt_video_text" : "a virtual tour of Tron Lightcycle Run rollercoaster",
        "captions" : "/static/vtt/tron.vtt",
        "Rider" : ["48in (122cm) or taller", "Kids, Teens, Adults"],
        "accesibility": ["Big Drops," "Thrill Ride", "Dark", "Must Transfer to Wheelchair, Then to Ride Vehicle", "Audio Description", "Handheld Captioning", "Service Animals Not Permitted"],
        "neighborhood": "Tomorrowland, Magic Kingdom Park", 
        "alt_text": "An exhilarating indoor roller coaster ride based on the Tron franchise, where riders board a light cycle and speed through a futuristic world filled with neon lights and sharp turns."
    },

    "8":{
        "id": "8",
        "title": "Space Mountain", 
        "image": "https://www.ocregister.com/wp-content/uploads/2021/07/OCR-L-APRIL2021-POM-54.jpg?w=1024",
        "description": "Blast off on a rip-roaring rocket into the furthest reaches of outer space on this roller-coaster ride in the dark.",
        "video" : "https://www.youtube.com/embed/WMMiZFPYg6M?start=2&end=185",
        "alt_video_text" : "a virtual tour of the indoor rollercoaster Space Mountain",
        "captions" : "/static/vtt/spacemountain.vtt",
        "rider": ["44in (112cm) or taller","Kids, Tweens, Teens, Adults"],
        "accesibility": ["Thrill Ride", "Big Drops", "Dark", "Must Transfer to Wheelchair, Then to Ride Vehicle", "Service Animals Not Permitted"],
        "neighborhood": "Tomorrowland, Magic Kingdom Park", 
        "alt_text": "A roller coaster track in the dark with starry lights surrounding it, surrounded by a space-themed environment and riders seated in a spaceship vehicle"
    },
    "9":{
        "id": "9",
        "title": "Buzz Lightyear's Space Ranger Spin", 
        "image": "https://attractionsmagazine.com/wp-content/uploads/2014/09/buzz_189_189.jpg",
        "description": "Fire your laser to earn points and defeat the Evil Emperor Zurg as you journey through a galactic space battle.",
        "video" : "https://www.youtube.com/embed/fRfnS044VNU",
        "alt_video_text" : "a virtual ride on Buzz Lightyear's Space Ranger Spin",
        "captions" : "/static/vtt/buzz.vtt",
        "Rider" : ["Any Height", "All ages"],
        "accesibility": ["Slow Rides", "Spinning", "Children under age 7 years must be accompanied by a person age 14 years or older.", "Must Transfer to Wheelchair", "Audio Description", "Handheld Captioning"], 
        "neighborhood": "Tomorrowland, Magic Kingdom Park", 
        "alt_text": "Board your XP-37 star cruiser and voyage deep into the Gamma Quadrant, where youll take aim at the glowing “Z” targets with your infrared laser cannon. Use your cruisers joystick to spin a full 360 degrees, so you can blast all the targets in sight."
    },

    "10":{
        "id": "10",
        "title": "Tomorrowland Speedway", 
        "image": "https://www.wdwinfo.com/wp-content/uploads/2022/05/Tomorrowland-Speedway-03.jpeg",
        "description": "Put the pedal to the metal in your very own hotrod and cruise along a scenic miniature motorway.",
        "video" : "https://www.youtube.com/embed/7W6iEx2Fh1g?start=6",
        "alt_video_text" : "a virtual ride on Tomorrowland's Speedway",
        "captions" : "/static/vtt/racecar.vtt",
        "rider": ["32in (81cm) or taller", "All ages"],
        "accesibility": ["Must Transfer from Wheelchair/ECV"],
        "neighborhood": "Tomorrowland, Magic Kingdom Park", 
        "alt_text": "Guests drive their own gas-powered cars through a winding racetrack with colorful scenery and props inspired by Tomorrowland."
    }
}

####################################ROUTES####################################
@app.route('/')
def hello_world():
   return render_template('home.html', rides = rides) #server sends data so that it will be accessible in html/js

@app.route('/view/<id>')
def display_details(id=None):
    
    global rides
    ride = rides[id]
    return render_template('display_ride.html', ride = ride) 

@app.route('/search_results/<searchString>')
def search(searchString=None):
    
    global rides
    nameResults = []
    neighborhoodResults = []
    accesibilityResults = []

    for r in rides.values():
        if searchString.lower() in r["title"].lower():  
            nameResults.append(r)
            #continue
        elif searchString.lower() in r["neighborhood"].lower():
            neighborhoodResults.append(r)
            #continue
        else:
            accesibilityFeatures = r["accesibility"]
            for i in range(len(accesibilityFeatures)):
                if searchString.lower() in accesibilityFeatures[i].lower():
                    print(accesibilityFeatures[i].lower())
                    accesibilityResults.append(r)
                    #break
                
    numOfResults = len(accesibilityResults) + len(neighborhoodResults) + len(nameResults)
    print("neighborhood results: ")
    print(neighborhoodResults)

    return render_template('search.html', nameResults=nameResults, neighborhoodResults= neighborhoodResults, accesibilityResults=accesibilityResults, searchString = searchString, numOfResults = numOfResults)

############################STANDARD THINGS WE NEED##############################
if __name__ == '__main__':
   app.run(debug = True)


