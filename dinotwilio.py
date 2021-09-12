from datetime import time
import re
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'pentaceratops' in incoming_msg:
        msg.body("https://go.echoar.xyz/CUAW")
        msg.body("""
        Here's some information about them
        Pentaceratops ("five-horned face") is a genus of herbivorous ceratopsid dinosaur from the late Cretaceous Period of what is now North America. Fossils of this animal were first discovered in 1921, but the genus was named in 1923 when its type species, Pentaceratops sternbergii, was described. Pentaceratops lived around 76–73 million years ago, its remains having been mostly found in the Kirtland Formation in the San Juan Basin in New Mexico. About a dozen skulls and skeletons have been uncovered, so anatomical understanding of Pentaceratops is fairly complete. One exceptionally large specimen later became its own genus, Titanoceratops, due to its more derived morphology, similarities to Triceratops, and lack of unique characteristics shared with Pentaceratops.
        """)
    if 'baryonyx' in incoming_msg:
        msg.body("https://go.echoar.xyz/SSq1")
        msg.body("""
        Here's some information about them
Baryonyx is an extinct genus of Spinosaur, a member of the same group as the northern African dinosaurs Spinosaurus and Suchomimus. Baryonyx was smaller than these relatives but was still a big predator. It was 10 meters (33 feet) long and 2.5 meters (8.25 feet) high at the hips. However, studies in the fossils of Baryonyx indicate that it had not yet reached its adult stage, so it could be larger, and another study found that there were vertebrae a little larger than others, which would indicate a possible candle or hump in the adult specimen.

It had a long, narrow snout filled with teeth that were cone-shaped - a real difference from the blade-shaped teeth of typical meat-eating dinosaurs.
        """)
      
    if 'triceratops' in incoming_msg:
        msg.body("https://go.echoar.xyz/M3v5")
        msg.body("""
        Here's some information about them
        Triceratops, (genus Triceratops), large quadrupedal plant-eating ceratopsian dinosaur that had a frill of bone at the back of its skull and three prominent horns. Fossils of “three-horned face,” as its Latin name is usually translated, date to the final 3 million years of the Cretaceous Period (145.5 million to 65.5 million years ago), making it one of the last of the non-avian dinosaurs to have evolved. Paleontologists estimate that the body length of Triceratops approached 9 metres (30 feet). The largest adults are thought to have weighed 5,450–7,260 kg (approximately 12,000–16,000 pounds).

Triceratops is the most commonly recovered dinosaur in the uppermost Cretaceous deposits of western North America, and its remains have been found throughout the region. Although many other large ceratopsians have been discovered in massive bone beds representing numerous individuals, Triceratops has only rarely been found in groups of three or more individuals. When the first specimen was discovered in 1887, it was mistaken for a gigantic species of extinct bison. Only later did further discoveries reveal that it was actually a horned dinosaur. Triceratops was officially named and described by American paleontologist O.C. Marsh in 1889. At present there are two recognized species: T. horridus and T. prorsus.


        """)
      
    if 'apatosaurs' in incoming_msg:
        msg.body("https://go.echoar.xyz/oWKp")
        msg.body("""
        Here's some information about them
Apatosaurus, (genus Apatosaurus), subsumes Brontosaurus, genus of at least two species of giant herbivorous sauropod dinosaurs that lived between about 156 million and 151 million years ago, during the late Jurassic Period. Its fossil remains are found in North America and Europe. Although the genus has subsumed Brontosaurus formally since 1903, a body of evidence suggests that Apatosaurus and Brontosaurus should be classified as separate genera.

Apatosaurus, which is considered to be one of the largest land animals of all time, weighed as much as 41 tonnes (roughly 45 tons) and measured up to 23 metres (about 75 feet) long, including its long neck and tail. It had four massive and pillarlike legs, and its tail was extremely long and whiplike. Although some scientists have suggested that the tail could have been cracked supersonically like a bullwhip, this is unlikely, as damage to the vertebrae would have been a more probable result.

        """)
      
    if 'raptor' in incoming_msg:
        msg.body("https://go.echoar.xyz/8QQZ")
        msg.body("""
        
Here's some information about them
Raptor roamed the Earth about 85.8 million to 70.6 million years ago during the end of the Cretaceous Period. 

In 1924, Henry Fairfield Osborn, then-president of the American Museum of Natural History, named Velociraptor. He bestowed the name on this dinosaur, which is derived from the Latin words "velox" (swift) and "raptor" (robber or plunderer), as an apt description of its agility and carnivorous diet. 

Earlier that year, Osborn had called the dinosaur Ovoraptor djadochtari in an article in the popular press, but the creature wasn't formally described in the article and the name "Ovoraptor" wasn't mentioned in a scientific journal, making Velociraptor the accepted name.

There are two Velociraptor species, V. mongoliensis and V. osmolskae, the second of which was only identified in 2008.

A member of the Dromaeosauridae family of small- to medium-sized birdlike dinosaurs, Velociraptor was roughly the size of a small turkey and smaller than others in this family of dinosaurs, which included Deinonychus and Achillobator. Adult Velociraptors grew up to 6.8 feet (2 meters) long, 1.6 feet (0.5 meter) tall at the hip and weighed up to 33 lbs. (15 kilograms).

Like Tyrannosaurus rex, Velociraptor had a prominent role in the "Jurassic Park" movies, but scientists do not believe it resembled anything close to its Hollywood depiction in terms of size or appearance. In fact, the movies' Velociraptor was actually modeled after Deinonychus, and sported a similar size and snout.

While the Velociraptor was featherless in the movies, paleontologists discovered quill knobs (places where the flight-related feathers of birds are anchored to the bone) on a well-preserved Velociraptor forearm from Mongolia in 2007, indicating the dinosaur had feathers. 

Despite having feathers, however, the arms of Velociraptors were too short to allow them to fly or even glide. The find suggests that the dinosaurs' dromaeosaurid ancestors could fly at one point, but lost that ability, according to the study published in the journal Science. 

        """)
        return str(resp)    
    if 'indominus' in incoming_msg:
        msg.body("https://go.echoar.xyz/MfWm")
        msg.body("""
        Here's some information about them
At first glance, Indominus rex most closely resembles a T. rex. But its distinctive head ornamentation and ultra-tough bony osteoderms can be traced from Abelisaurs. Indominus' roar is estimated to reach 140-160 dB -- the same as a 747 taking off. It can reach speeds of 30 mph...while confined to its enclosure.

        """)
       
    if 'utahraptor' in incoming_msg:
        msg.body("https://go.echoar.xyz/dGix")
        msg.body("""
        Here's some information about them
 Utahraptor ostrommaysorum is one of the geologically oldest and largest known dromaeosaurids. This group of carnivorous dinosaurs had a large retractable sickle claw on its foot, specialized for cutting.  With a name meaning “Utah’s predator,” Utahraptor was a ferocious hunter that used its sickle-shaped claws to attack and rip apart its prey. The claw itself was 9.5 inches (24 cm) long! The species name ‘ostrommaysorum’ honors Dr. John Ostrom of Yale University for his pioneering research linking carnivorous dinosaurs to the ancestry of birds. Utahraptor was the inspiration for the Velociraptors in the film Jurassic Park! Utahraptor, however, was quite a bit bigger than Velociraptor; adults were around 20 feet (6.1 meters) long and around 5 feet (1.5 meters) tall at the hip
        """)
       
    if 'gallimimus' in incoming_msg:
        msg.body("https://go.echoar.xyz/ic6X")
        msg.body("""
        Here's some information about them
Gallimimus was a speedy theropod, the largest of its type. They were called chicken mimics because they probably moved like modern flightless birds. Unlike other theropods, Gallimimus had no teeth. In fact, it had a very small head. This was probably one of the fastest dinosaurs, with speed like an ostrich, it could probably run up to 30 miles per hour.

With its small, toothless head, it is believed that Gallimimus probably had a diet of insects, small animals, eggs, and maybe even some plants. They had a much longer neck than any other theropod dinosaur.

        """)
       
    if 'tylosaurus' in incoming_msg:
        msg.body("https://go.echoar.xyz/xwV4")
        msg.body("""
        Here's some information about them
Tylosaurus was the deadliest hunter of the ancient seas, ready to seize and kill just about any smaller creature that crossed its path with true jaws of death—lined on each side with two rows of pointy, cone-shaped teeth. Tylosaurus used its snout to locate prey, which, once inside the mosasaur's menacing jaws, was swallowed whole. When the sea monster opened wide for the final gulp, two extra rows of teeth on the roof of its mouth allowed crippled captives no escape.

Tylosaurus grew more than 45 feet (14 meters) long, making it the largest of the marine reptiles called mosasaurs. Like all mosasaurs, a long and muscular, vertically flattened tail powered Tylosaurus through the water, allowing it to ambush its prey with rapid bursts of acceleration. Paddle-like limbs helped steer the slim body covered in lizard-like scales through the water.

Preserved stomach contents indicate a diet heavy on fish, but seabirds, sharks, plesiosaurs, and other mosasaurs also failed to escape Tylosaurus's lethal grip. Though not a dinosaur, Tylosaurus lived alongside them and went extinct at around the same time. Many Tylosaurus remains have been found in Kansas, which was once covered by a large ocean called the Western Interior Seaway.

        """)
            
    if 'polacanthus' in incoming_msg:
        msg.body("https://go.echoar.xyz/Bo2q")
        msg.body("""
        Here's some information about them
Polacanthus was a quadrupedal ornithischian or "bird-hipped" dinosaur. It lived 130 to 125 million years ago in what is now western Europe. Polacanthus foxii was named after a find on the Isle of Wight in 1865. There are not many fossil remains of this creature, and some important anatomical features, such as its skull, are poorly known. Early depictions often gave it a very generic head as it was only known from the rear half of the creature. It grew to about 5 metres (16 ft) long. Its body was covered with armour plates and spikes. It possibly was a basal member of the Nodosauridae.
        """)        
    if 'velociraptor' in incoming_msg:
        msg.body("https://go.echoar.xyz/hjBT")
        msg.body("""
        Here's some information about them
Velociraptor, in real life, was a genus of dromaeosaurid theropod dinosaur from the Late Cretaceous period which inhabited what is now the Mongolia-China border with other unique dinosaurs. Velociraptor was no bigger than a wolf and with its feathers it bore a very bird-like appearance that would make it all the more different from the films, being more akin to a flightless hawk. It had a long claw ("terrible claw") on the second toe of both feet, 8 centimeters (3 inches) long, which was probably used as a weapon, plunging into the flesh of victims and causing deep wounds. Velociraptor was the first dromaeosaurid to be discovered (1923) and is still the most well known to paleontologists, with over a dozen recovered fossil skeletons - the most of any other member of its family. Since its appearance in the first film, it has become a symbol of Jurassic Park and has appeared in all the films and games.

        """)     
    if 'trex' in incoming_msg:
        msg.body("https://go.echoar.xyz/pbhx")
        msg.body("""
Here's some information about them
Tyrannosaurus is a genus of tyrannosaurid theropod dinosaur. The species Tyrannosaurus rex (rex meaning "king" in Latin), often called T. rex or colloquially T-Rex, is one of the best represented of these large theropods. Tyrannosaurus lived throughout what is now western North America, on what was then an island continent known as Laramidia. Tyrannosaurus had a much wider range than other tyrannosaurids. Fossils are found in a variety of rock formations dating to the Maastrichtian age of the Upper Cretaceous period, 68 to 66 million years ago. It was the last known member of the tyrannosaurids and among the last non-avian dinosaurs to exist before the Cretaceous–Paleogene extinction event.
        """)
    if 'sauropod' in incoming_msg:
        msg.body("https://go.echoar.xyz/f3Jj")
        msg.body("""
Here's some information about them
Sauropod, any member of the dinosaur subgroup Sauropoda, marked by large size, a long neck and tail, a four-legged stance, and a herbivorous diet. These reptiles were the largest of all dinosaurs and the largest land animals that ever lived.

Sauropods shared a body plan consisting of: a small head on an extremely long neck; a long, massive body housing an enormous gut; thick pillarlike legs to support the torso; and a very long, tapering, often whiplike tail. A massive hip girdle was fused to the backbone, usually by five sacral vertebrae; this arrangement provided solid support for the body and tail. The backbone itself was hollowed out at the sides, which thus reduced its weight while retaining structural strength. Sauropods were once thought to have spent their time wallowing in shallow water that would help support their ponderous bodies, but considerable evidence indicates that they were better equipped for living on solid ground. The animals’ long necks enabled them to take foliage from even the tallest trees in somewhat the same manner as do modern giraffes. Their teeth tended to be spoon-shaped or pencil-shaped, and they apparently depended on swallowed stones or bacteria in the gut to help break down the plant matter they ate.
        """)
    if 'spinosaurus' in incoming_msg:
        msg.body("https://go.echoar.xyz/ok4W")
        msg.body("""
        Here's some information about them
        Spinosaurus, a genus of theropod dinosaurs belonging to the family Spinosauridae, known from incomplete North African fossils that date to Cenomanian times (roughly 100 to 94 million years ago). Spinosaurus, or “spined reptile,” was named for its “sail-back” feature, created by tall vertebral spines. It was named by German paleontologist Ernst Stromer in 1915 on the basis of the discovery of a partial skeleton from Bahariya Oasis in western Egypt by his assistant Richard Markgraf. These fossils were destroyed in April 1944 when British aircraft inadvertently bombed the museum in Munich in which they were housed. For several decades Spinosaurus was known only from Stromer’s monographic descriptions; however, additional fragmentary remains were discovered during the 1990s and 2000s in Algeria, Morocco, and Tunisia. Related taxa in the family Spinosauridae include Baryonyx from England, Irritator from Brazil, and Suchomimus from Niger.
        """)  
    if 'help' in incoming_msg:
        msg.body("""
List  of available dinosaurs

1.Tylosaurus

2.Gallimimus

3.Polacanthus

4.Velociraptor

5.Trex

6.Pentaceratops

7.Baryonyx

8.Triceratops

9.Apatosaurs

10.Raptor

11.Indominus

12.Utahraptor

13.Sauropod

14.Spinosaurus
        """)
    return str(resp)    

if __name__ == '__main__':
    app.run()