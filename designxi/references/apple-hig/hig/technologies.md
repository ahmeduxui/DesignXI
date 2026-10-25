# Apple HIG — Technologies
Bundled HIG pages for the “Technologies” group. Each page kept verbatim under an anchor heading `## <slug>`. Cite as **technologies.md › <slug> › heading**.


<a id="airplay"></a>
## airplay

# AirPlay

> Source: <https://developer.apple.com/design/human-interface-guidelines/airplay>
> Section: Technologies
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2023-05-02 (Consolidated guidance into one page.)

AirPlay lets people stream media content wirelessly from iOS, iPadOS, macOS, and tvOS devices to Apple TV, HomePod, and TVs and speakers that support AirPlay.

---

## Best practices

**Prefer the system-provided media player.** The built-in media player offers a standard set of controls and supports features like chapter navigation, subtitles, closed captioning, and AirPlay streaming. It’s also easy to implement, provides a consistent and familiar playback experience across the system, and accommodates the needs of most media apps. Consider designing a custom video player only if the system-provided player doesn’t meet your app’s needs. For developer guidance, see [AVPlayerViewController](https://developer.apple.com/documentation/avkit/avplayerviewcontroller).

**Provide content in the highest possible resolution.** Your [HTTP Live Streaming](https://developer.apple.com/documentation/http-live-streaming) (HLS) playlist needs to include the full range of available resolutions so that people can experience your content in the resolution that’s appropriate for the device they’re using (AVFoundation automatically selects the resolution based on the device). If you don’t include a range of resolutions, your content looks low quality when people stream it to a device that can play at higher resolutions. For example, content that looks great on iPhone at 720p will look low quality when people use AirPlay to stream it to a 4K TV.

**Stream only the content people expect.** Avoid streaming content like background loops and short video experiences that make sense only within the context of the app itself. For developer guidance, see [usesExternalPlaybackWhileExternalScreenIsActive](https://developer.apple.com/documentation/avfoundation/avplayer/usesexternalplaybackwhileexternalscreenisactive).

**Support both AirPlay streaming and mirroring.** Supporting both features gives people the most flexibility.

**Support remote control events.** When you do, people can choose actions like play, pause, and fast forward on the lock screen, and through interaction with Siri or HomePod. For developer guidance, see [Remote command center events](https://developer.apple.com/documentation/mediaplayer/remote-command-center-events).

**Don’t stop playback when your app enters the background or when the device locks.** For example, people expect the TV show they started streaming from your app to continue while they check their mail or put their device to sleep. In this type of scenario, it’s also crucial to avoid automatic mirroring because people don’t want to stream other content on their device without explicitly choosing to do so.

**Don’t interrupt another app’s playback unless your app is starting to play immersive content.** For example, if your app plays a video when it launches or auto-plays inline videos, play this content on only the local device, while allowing current playback to continue. For developer guidance, see [ambient](https://developer.apple.com/documentation/avfaudio/avaudiosession/category-swift.struct/ambient).

**Let people use other parts of your app during playback.** When AirPlay is active, your app needs to remain functional. If people navigate away from the playback screen, make sure other in-app videos don’t begin playing and interrupt the streaming content.

**If necessary, provide a custom interface for controlling media playback.** If you can’t use the system-provided media player, you can create a custom media player that gives people an intuitive way to enter AirPlay. If you need to do this, be sure to provide custom buttons that match the appearance and behavior of the system-provided ones, including distinct visual states that indicate when playback starts, is occurring, or is unavailable. Use only Apple-provided symbols in custom controls that initiate AirPlay, and position the AirPlay icon correctly in your custom player — that is, in the lower-right corner (in iOS 16 and iPadOS 16 and later).

## Using AirPlay icons

You can download AirPlay icons in [Resources](https://developer.apple.com/design/resources/). You have the following options for displaying the AirPlay icon in your app.

### Black AirPlay icon

Use the black AirPlay icon on white or light backgrounds when other technology icons also appear in black.

### White AirPlay icon

Use the white AirPlay icon on black or dark backgrounds when other technology icons also appear in white.

### Custom color AirPlay icon

Use a custom color when other technology icons also appear in the same color.

**Position the AirPlay icon consistently with other technology icons.** If you display other technology icons within shapes, you can display the AirPlay icon in the same manner.

**Don’t use the AirPlay icon or name in custom buttons or interactive elements.** Use the icon and the name *AirPlay* only in noninteractive ways.

**Pair the icon with the name *AirPlay* correctly.** You can show the name below or beside the icon if you also reference other technologies in this way. Use the same font you use in the rest of your layout. Avoid using the AirPlay icon within text or as a replacement for the name *AirPlay*.

**Emphasize your app over AirPlay.** Make references to AirPlay less prominent than your app name or main identity.

## Referring to AirPlay

**Use correct capitalization when using the term *AirPlay*.** *AirPlay* is one word, with an uppercase *A* and uppercase *P*, each followed by lowercase letters. If your layout displays only all-uppercase designations, you can typeset *AirPlay* in all uppercase to match the style of the rest of the layout.

**Always use *AirPlay* as a noun.**

|  | Example text |
| --- | --- |
| ✓ | Use AirPlay to listen on your speaker |
| ✗ | AirPlay to your speaker |
| ✗ | You can AirPlay with [App Name] |

**Use terms like *works with*, *use*, *supports*, and *compatible*.**

|  | Example text |
| --- | --- |
| ✓ | [App Name] is compatible with AirPlay |
| ✓ | AirPlay-enabled speaker |
| ✓ | You can use AirPlay with [App Name] |
| ✗ | [App Name] has AirPlay |

**Use the name *Apple* with the name *AirPlay* if desired.**

|  | Example text |
| --- | --- |
| ✓ | Compatible with Apple AirPlay |

**Refer to AirPlay if appropriate and to add clarity.** If your content is specific to AirPlay, you can use Airplay to make that clear. You can also refer to AirPlay in technical specifications.

|  | Example text |
| --- | --- |
| ✓ | [App Name] now supports AirPlay |

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS. Not supported in watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| May 2, 2023 | Consolidated guidance into one page. |

---


<a id="app-clips"></a>
## app-clips

# App Clips

> Source: <https://developer.apple.com/design/human-interface-guidelines/app-clips>
> Section: Technologies
> Platforms covered: iOS, iPadOS
> Last change on Apple's site: 2025-06-09 (Updated guidance to include demo App Clips.)

An App Clip is a lightweight version of your app or game that provides an on-the-go or demo experience that’s instantly available.

---

App Clips deliver an experience from your app or game without requiring people to download the full app from the App Store. App Clips focus on a fast solution to a task or contain a demo that showcases the full app or game, and they remain on the device for a limited amount of time while preserving people’s privacy.

People discover and launch App Clips in a variety of situations and contexts. At a physical location, people launch an App Clip by scanning an App Clip Code, NFC tag, or a QR code. An App Clip Code tends to be the best way for people to discover and launch your App Clip because its distinct design is immediately recognizable, and people trust it to offer a fast, secure way to launch an App Clip.

On their device, people launch an App Clip from location-based suggestions they permit in Siri Suggestions, the Maps app, Smart App Banners on websites, App Clip cards in Safari, and by tapping links others share with them in the Messages app. Starting with iOS 17, an app can include links and App Clip previews that people tap to launch another app’s App Clip.

Consider creating an App Clip if your app provides an in-the-moment experience that helps people perform a task over a finite amount of time. For example:

- A rental bike could come with an App Clip Code that people tap or scan to launch an App Clip that lets them rent the bike.
- A coffee shop could offer an App Clip for fast advance orders that customers launch from a Smart App Banner or an App Clip card on the shop’s website. Customers could share a link to the website from the Messages app, which recipients then tap to launch the App Clip from within Messages.
- A food truck could create marketing material (for example, a poster to promote a seasonal dish) that includes an App Clip Code. People can scan the App Clip Code with the Camera app on their device and instantly launch the App Clip to order the seasonal dish.
- A restaurant could let diners pay for a meal by launching an App Clip from the Maps app or a suggestion from Siri Suggestions, or by holding their device close to an App Clip Code or NFC tag at their table.
- A museum could have visitors scan App Clip Codes or QR codes on labels next to displayed works to launch an App Clip that reveals augmented reality content or provides audio commentary.

Consider creating an App Clip to let people experience your app or game before committing to a purchase or subscription. Focus on providing people with an opportunity to experience and understand your app or game. For example:

- A game might offer an App Clip that lets people play a demo version of the game, including a tutorial and the first level of the game.
- A fitness app might offer an App Clip with a free workout and a guided meditation.
- A text editor might allow people to create and save a document using the demo App Clip.

For developer guidance, see [App Clips](https://developer.apple.com/documentation/appclip).

## Designing your App Clip

**Allow people to complete a task or a demo in your App Clip.** Don’t require people to install the full app to experience the entire demo, to complete a task, or to finish a level in a game.

**Focus on essential features.** Interactions with App Clips are quick and focused. Limit features to what’s necessary to accomplish the task at hand. Reserve advanced or complex features for the app. If you offer a demo version of your full app, focus on essential features that give people a good sense of your game or your app’s functionality.

**Don’t use App Clips solely for marketing purposes.** App Clips need to provide real value and help people accomplish tasks. Don’t use them as a means to advertise services or products, and don’t display ads in your App Clip.

**Avoid using web views in your App Clip.** App Clips use native components and frameworks to offer an app-quality experience. If only web components are available to you, offer a quick link to your website instead of an App Clip.

**Design a linear, easy-to-use, and focused user interface.** App Clips don’t need tab bars, complex navigation, or settings. Keep the number of screens and entry forms to a minimum. Remove extraneous information and reduce complexity in the user interface wherever possible.

**On launch, show the most relevant part of your App Clip.** Skip unnecessary steps and take people immediately to the part of the App Clip that best fits their context.

**Ensure people can use your App Clip immediately.** App Clips need to include all required assets, omit splash screens, and never make people wait on launch.

**Ensure your App Clip is small.** The smaller your App Clip, the faster it will launch on a person’s device. Keeping your App Clip small is especially important when bandwidth is limited. As much as possible, reduce unnecessary code and remove unused assets. Avoid downloading additional data, which can take away the feeling of immediacy.

**Make the App Clip shareable.** When someone shares a link to an App Clip in the Messages app, recipients can launch the App Clip from within the Messages app. Offer the ability to share links to specific points in your App Clip, and encourage people to share the App Clip with others.

**Make it easy to pay for a service or product.** Entering payment information can be a long and error-prone task. Consider supporting [Apple Pay](apple-pay.md) to offer express checkout and let people enter shipping information with no typing.

**Avoid requiring people to create an account before they can benefit from your App Clip.** Creating an account is a complex task that takes time and effort. Consider not requiring an account, or think about asking people to create an account after they finish a task. If your App Clip requires an account to provide value, limit the amount of information people need to provide — for example, by offering [Sign in with Apple](sign-in-with-apple.md).

**Provide a familiar, focused experience in your app.** When people install the full app, it replaces the App Clip on their device. From this moment, invocations that would have launched the App Clip launch the full app instead. Ensure your app provides a focused, familiar experience to people who previously used the App Clip. Don’t require additional steps that slow people down; for example, don’t require people to log in again when they transition from the App Clip to the app.

### Preserving privacy

The system imposes limits on App Clips to ensure people’s privacy. For example, App Clips can’t perform background operations. For developer guidance, see [Choosing the right functionality for your App Clip](https://developer.apple.com/documentation/appclip/choosing-the-right-functionality-for-your-app-clip).

**Limit the amount of data you store and handle yourself.** If you need to store people’s data — for example, login information — store it securely. In addition, don’t rely on the availability of data you previously stored on the device — the system may have removed the App Clip from the device between launches and deleted all of its data. If you store login information, securely store it off the device.

**Consider offering Sign in with Apple.** Sign in with Apple securely retains login information off people’s devices and preserves their privacy. For guidance, see [Sign in with Apple](sign-in-with-apple.md).

**Offer a secure way to pay for services or goods that also respects people’s privacy.** For example, consider offering [Apple Pay](apple-pay.md).

### Showcasing your app

People don’t manage App Clips themselves, and App Clips don’t appear on the Home screen. Instead, the system removes an App Clip after a period of inactivity.

Because apps remain the best way to keep people engaged over time, the system helps them discover and install the full app:

- On the App Clip card, people can either launch the App Clip or visit the full app’s page on the App Store.
- When people first launch the App Clip, the system displays an app banner at the top of the screen. Like the App Clip card, the banner allows people to visit the app’s page on the App Store.

In addition, you can display an overlay in your App Clip that allows people to download the full app from within the App Clip.

**Don’t compromise the user experience by asking people to install the full app.** If your App Clip offers an on-the-go experience, consider whether the App Clip card and the system-provided app banner provide enough incentive for people to download the full app. If your App Clip offers a demo experience, let people fully experience the demo before asking them to install the full app.

**Pick the right time to recommend your app.**  When someone completes a task or reaches a natural pause, display an [SKOverlay](https://developer.apple.com/documentation/storekit/skoverlay) that allows people to initiate a download of your full app or game from the context of the App Clip.

**Recommend your app in a nonintrusive, polite way.** Don’t ask people to install the full app repeatedly or interrupt them during a task. Push notifications aren’t a good way to ask people to install the app either. Clearly communicate your app’s additional features.

For developer guidance, see [Recommending your app to App Clip users](https://developer.apple.com/documentation/appclip/recommending-your-app-to-app-clip-users).

### Limiting notifications

App Clips provide the option to schedule and receive notifications for up to 8 hours after launch, enough time to follow up and complete most common tasks.

**Only ask for permission to use notifications for an extended period of time if it’s really needed.** If your App Clip’s functionality spans more than a day, explicitly request permission to schedule and receive notifications. For example, a car rental company’s App Clip can ask for permission to send a notification that reminds people that they need to return a rented car soon.

**Keep notifications focused.** Don’t send purely promotional notifications, and only use notifications in response to an explicit user action. If a person completes their task without leaving the App Clip, you might not need to send any notifications at all.

**Use notifications to help people complete a task.** Notifications for an App Clip relate directly to the task the App Clip helps to accomplish. For example, an App Clip that helps people order food could send notifications related to a scheduled delivery.

For developer guidance, see [Enabling notifications in App Clips](https://developer.apple.com/documentation/appclip/enabling-notifications-in-app-clips).

### Creating App Clips for businesses

If you’re a platform provider who services businesses, you may create several App Clip experiences in [App Store Connect](https://appstoreconnect.apple.com) and use a single App Clip to power them all. To people using the App Clip, it appears with the branding of an individual business or location instead of your own branding.

**Use consistent branding.** When people see the App Clip card for a business, the brand for that business is front and center. Tone down your own branding and make sure the branding for the business is clearly visible to avoid confusing people when they enter the App Clip experience.

**Consider multiple businesses.** An App Clip may power many different businesses or a business that has multiple locations. In both scenarios, people may end up using the App Clip for more than one business or location at a time. The App Clip must handle this use case and update its user interface accordingly. For example, consider a way to switch between recent businesses or locations within your App Clip, and verify a person’s location when they launch it.

For developer guidance, see [Configuring App Clip experiences](https://developer.apple.com/documentation/appclip/configuring-the-launch-experience-of-your-app-clip).

## Creating content for an App Clip card

The system-provided App Clip card is people’s first interaction with your App Clip, so give careful consideration to its images and copy.

**Be informative.** Make sure the image on the App Clip card clearly communicates the features offered by your App Clip, supported tasks, or content.

**Prefer photography and graphics.** Avoid using a screenshot of your app’s user interface because it’s unlikely to communicate the purpose of your App Clip. Instead, use an image that helps people understand the App Clip’s value, or a photo of the location of its associated business or point of interest.

**Avoid using text.** Text in the header image isn’t localizable, can be difficult to read, and can make a card image less aesthetically pleasing.

**Adhere to image requirements.** Use a 1800x1200 px PNG or JPEG image without transparency.

**Use concise copy.** An App Clip card requires both a title and a subtitle. Clearly express the purpose of your App Clip within the available space so people can read and understand it at a glance. Create a title that has no more than 30 characters and a subtitle that has no more than 56 characters.

**Pick a verb for the action button that best fits your App Clip.** Possible verbs are *View*, *Play*, or *Open*. Pick *View* for media, or if your App Clip provides informational or educational content. Pick *Play* for games. Choose *Open* for all other App Clips.

## App Clip Codes

App Clip Codes are the best way for people to discover your App Clip. Their distinct design is immediately recognizable, and they offer a fast, secure way to launch your App Clip.

App Clip Codes always use the designs Apple provides and follow size, placement, and printing guidelines. Choose between the badge design that uses the App Clip logo ( App Clip) or, when space is at a premium, a design without it. Create App Clip Codes that use a default color pair, or choose custom foreground and background colors. For developer guidance, see [Creating App Clip Codes](https://developer.apple.com/documentation/appclip/creating-app-clip-codes).

### Interacting with App Clip Codes

App Clip Codes come in two variants: *scan-only* or with an embedded NFC tag (*NFC-integrated*).

The scan-only variant uses a camera icon in its center to let people know to use the Camera app or the Code Scanner in Control Center to scan the App Clip Code. The NFC-integrated variant uses an iPhone icon at its center that guides people to hold their device close to the App Clip Code or to scan it using the NFC Tag Reader in Control Center. People can also scan an NFC-integrated App Clip Code with the Camera app or the Code Scanner in Control Center. For example:

- A coffee shop could place an App Clip Code on their menu. A guest could hold their device close to the App Clip Code and instantly launch the shop’s App Clip to order a drink.
- A gas station could have an NFC-integrated App Clip Code attached to each pump. A traveler could hold their device close to it to launch the gas station’s App Clip and use it to pay for their refill.
- A video game creator could hand out marketing material at an industry event that includes an App Clip Code. An event attendee could scan the code to launch an App Clip that’s a playable demo of their latest video game.

### Displaying App Clip Codes

When you start designing your App Clip Codes, choose the variant that works best for the way people use your App Clip. If people can physically access the App Clip Code, use the NFC-integrated variant. For example:

- On a tabletop at a restaurant
- Near a register at a retail store
- In a storefront window
- On signage
- On a gift card or coupon

If you need to place your App Clip Code in an area that’s physically inaccessible or you need to display it digitally, use a scan-only App Clip Code. For example:

- On posters or printed advertising
- On signage behind a counter or unreachable in a storefront
- On digital materials such as digital displays, in emails, or on images you post to social media

No matter which of the two variants you use, it’s important you carefully consider where you place your App Clip Code to ensure a reliable scanning experience.

**Include the App Clip logo when space allows.** The logo helps make it clear that the code launches an App Clip; however, if you can’t meet the clear space requirements, use the App Clip Code design without the App Clip logo. Also, use the design without the App Clip logo if you place the App Clip Code on disposable paper or plastic items, or on items associated with gambling or drinking. For example, use the App Clip Code without the App Clip logo on playing cards, poker chips, or bar coasters. The App Clip logo is always part of the badge design where it appears below the App Clip Code; never use the App Clip logo on its own.

**Place your App Clip Code on a flat or cylindrical surface only.** If you place your App Clip Code on a cylindrical surface — for example, on a scooter’s handlebar — make sure the width of the App Clip Code doesn’t exceed one-sixth of the cylinder’s circumference.

**Help your App Clip Code remain as flat as possible so it’s easy for people to scan.** To provide the best scanning experience, avoid displaying App Clip Codes on deformable materials that readily fold or crumple, such as paper, plastic, or fabric. If you need to make your App Clip Code available on a bag, flexible box, or other deformable object, display it on something rigid — like a card — that you attach to the object. If you create an App Clip Code sticker, make sure it adheres well to flat surfaces.

**Place your App Clip Code in a location that helps ensure reliable scanning.** For example, place a scan-only App Clip Code in a location that offers enough light to ensure reliable scanning, and don’t require people to scan from a wide angle.

**Make sure the App Clip Code is unobstructed.** Don’t overlay the App Clip Code with text, logos, or images. Never animate the App Clip Code or dim it.

**Display the App Clip Code in an upright position.** Don’t rotate the generated App Clip Code or display the center glyph at an angle.

**Don’t create App Clip Codes that are too small.** App Clip Codes must adhere to the following specifications.

| Type | Minimum size |
| --- | --- |
| Printed communications | Minimum diameter of 3/4 inch (1.9 cm). |
| Digital communications | Minimum size of 256×256 px. Use a PNG or SVG file. |
| NFC-integrated App Clip Code | The embedded NFC tag needs to be at least 35 mm in diameter or of equivalent size. For example, if your embedded NFC tag is 35 mm in diameter, your printed App Clip Code needs to be at least 1.37 inches (3.48 cm) in diameter. |

When determining the dimensions of your App Clip Codes, consider a distance to code size ratio of no more than 20:1. If possible, use a ratio of 10:1 to ensure reliable scanning. For example, an App Clip that people scan from 40 inches (101 cm) away needs to be at least 4 inches (10.16 cm) in diameter.

If you display an App Clip Code near a QR Code or other scannable item, choose a size for the App Clip Code that’s at least the other code’s or item’s size.

**Provide enough space between an App Clip Code and adjacent App Clip Codes, graphics, or materials.** The minimum clear space around an App Clip Code is equal to the space between the center glyph and the circular code. If you place your App Clip Code next to another App Clip Code or other machine-readable code, leave enough clear space to allow for reliable scanning of each code.

### Using clear messaging

Add clear messaging that informs people how they can use the App Clip Code to launch your App Clip, especially if you use the design without the App Clip logo. For example, add a call to action next to an App Clip Code you display in an email or on a poster. Use the suggested call-to-action messaging or your own copy. Always use a simple, clear call to action.

For a scan-only App Clip Code, you can use the following call to action:

- Scan to [*describe what people can do with your App Clip*].
- Scan using the camera on your iPhone or iPad to [describe what people can do with your App Clip].

For an NFC-integrated App Clip Code, you can use the following call to action:

- Scan to [*describe what people can do with your App Clip*].
- Hold your iPhone near the [*object name*] to launch an App Clip that [*describe what a person can do with your App Clip*].

For more information, see [NFC](nfc.md).

**Adhere to [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html) when referring to your App Clip and App Clip Codes.** For example, Apple trademarks can’t appear in your app name or images, always use title case when using the terms App Clips or App Clip Code, and so on. For additional information, see [Legal requirements](#legal-requirements).

### Customizing your App Clip Code

Use [App Store Connect](https://appstoreconnect.apple.com) or the [App Clip Code Generator](https://developer.apple.com/app-clips/resources/) command-line tool to create App Clip Codes, and follow best practices to ensure a reliable scanning experience.

**Always use the generated App Clip Code.** Don’t create your own App Clip Code design or modify a generated App Clip Code in any way. Don’t apply filters, augment its colors, or add glows, shadows, gradients, or reflections. They negatively impact people’s scanning experience. When scaling a generated App Clip Code, don’t change the generated code’s aspect ratio, and be sure to scale all attributes of the App Clip Code — for example the stroke widths.

**Choose colors with enough contrast that ensure accurate scanning.** Each App Clip Code uses three colors: a foreground color, a background color, and a third color that’s generated for you based on the foreground and background colors. Both [App Store Connect](https://appstoreconnect.apple.com) and the [App Clip Code Generator](https://developer.apple.com/app-clips/resources/) command-line tool offer a selection of default color pairs. Alternatively, you can choose custom foreground and background colors. Note that you can’t choose custom colors that will lead to a suboptimal scanning experience. If your color selection doesn’t work well, neither App Store Connect nor the command-line tool will generate an App Clip Code. To help you choose a color combination that works well, both tools contain functionality to suggest a different foreground color based on your custom background color. For more information, see [Creating App Clip Codes with the App Clip Code Generator](https://developer.apple.com/documentation/appclip/creating-app-clip-codes-with-the-app-clip-code-generator) and [Creating App Clip Codes with App Store Connect](https://developer.apple.com/documentation/appclip/creating-app-clip-codes-with-app-store-connect).

## Printing guidelines

App Clip Codes offer the best experience to launch App Clips. As a result, it’s important to manufacture and display App Clip Codes that offer a reliable scanning experience for a long time. You can print App Clip Codes yourself, or work with a professional printing service — for example, [RR Donnelley](https://touchless.acc.rrd.com/).

Always test printed App Clip Codes before you distribute them to be sure they’re scannable from a variety of angles.

**Use high-quality, non-textured print materials.** Print App Clip Codes on matte finishes. Avoid shine, gloss, reflective or holographic overlays, as well as thin laminate finishes or materials. In case you need to laminate print material with an App Clip Code on it, use a matte laminate to avoid shine and reflections. If you place your App Clip Code outdoors, use UV-resistant materials or coatings to prevent fading from exposure to sunlight, rain, and other weather conditions. If you work with a professional printing service, use flexographic printing for best results. If you print the App Clip Codes yourself using a desktop printer, use an inkjet printer for best results.

**Use high-resolution images and printer settings.** When rasterizing the SVG file, set the image resolution to at least 600 ppi, and print your App Clip Codes with a minimum resolution of 300 dpi. Consider leveling and calibrating your printer before printing to ensure a high print quality, and avoid poor color channel alignment, inaccurate gamma values, artifacts, or printing elliptical or otherwise distorted App Clip Codes. When using receipt printers, print App Clip Codes as close to the paper’s maximum bounds as possible.

**Use correct color settings when you convert the generated SVG file to a CMYK image.** Both the [App Clip Code Generator](https://developer.apple.com/app-clips/resources/) command-line tool and [App Store Connect](https://appstoreconnect.apple.com) generate App Clip Codes as SVG files in the sRGB color space. To print colors that match the SVG file, convert the sRGB image to a CMYK image. Use a relative calorimetric (media-relative) intent when performing the conversion. Use “Generic CMYK ICC profile” on CMYK printers or “Gracol 2013 ICC profile” on CMYKOV printers and allow for a color tolerance CIELab Delta E of 2.5.

**If you’re using a printer that only prints in grayscale, only generate grayscale App Clip Codes.** Codes generated in color and then printed in grayscale may work less reliably.

**For NFC-integrated App Clip Codes, choose Type 5 NFC tags.** The embedded NFC tag needs to be at least 35 mm in diameter or of equivalent size.

**If you create large batches of App Clip Codes, thoroughly test your printing workflow, and verify printed App Clip Codes.** For example, conduct small, inexpensive print runs using a subset of codes. Print your App Clip Codes on print templates with additional padded regions that allow you to display the encoded invocation URL and the SVG filename alongside each code for validation at the time of print.

If you create many App Clip Codes with the [App Clip Code Generator](https://developer.apple.com/app-clips/resources/) tool or [App Store Connect](https://appstoreconnect.apple.com), you’ll likely work with a professional printing service. If this is the case, you need to handle a lot of SVG files. Because you have no way of knowing which App Clip Code encodes which URL by looking at an App Clip Code, you need to use a file that contains information about which SVG file maps to which invocation URL. Under any circumstance, careful file management, versioning, and change tracking are key to avoiding faulty print runs. For more information, see [Preparing multiple App Clip Codes for production](https://developer.apple.com/documentation/appclip/preparing-multiple-app-clip-codes-for-production).

### Verifying your printer’s calibration

A reliable scanning experience depends on the quality of your printed App Clip Codes. To ensure printing App Clip Codes results in a reliable scanning experience and to avoid using a printer that can’t print high-quality App Clip Codes, Apple offers [printer calibration test sheets](https://developer.apple.com/app-clips/resources/printer-calibration-test-sheets.zip) you can use to verify your printer’s settings and print quality.

**Verify print quality of your chosen color pair with the printer calibration test sheet that shows text boxes for each default color pair.** Follow the instructions on the sheet to print it at the right scale and to verify that your printer can create high-quality App Clip Codes.

**Verify your printer’s grayscale settings by printing the printer calibration test sheet that shows two grayscale bars.** If any of the specific gray colors are light or entirely missing, the printer may need calibration or may not be suitable for printing an App Clip Code that allows for reliable scanning.

## Legal requirements

Only the Apple-provided App Clip Codes created in App Store Connect or with the App Clip Code Generator command-line tool and that follow these guidelines are approved for use.

App Clip Codes are approved for use to indicate availability of an App Clip. Apple may update the App Clip Code design from time to time at Apple’s discretion.

In the event your App Clip is no longer active, also stop displaying the App Clip Code associated with that inactive App Clip.

You may not use the App Clip Code (including, without limitation, the Apple Logo, the App Clip mark, and the App Clip Code designs) as part of your own company name or as part of your product name. You may not seek copyright or trademark registration for the App Clip Codes or any elements contained therein.

The App Clip Codes described in these guidelines must not be used in any manner that is likely to reduce, diminish, or damage the goodwill, value, or reputation associated with Apple or App Clips; or that infringes or violates the trademarks or other proprietary rights of any third party; or that is likely to cause confusion as to the source of products or services.

Apple retains all rights to its trademarks, copyrights, or other intellectual property rights contained in the materials provided for use hereunder, including, without limitation, the App Clip Codes and any elements contained therein.

Don’t add a symbol to App Clip Codes created in App Store Connect or with the App Clip Code Generator command-line tool.

Don’t translate any Apple trademark. Apple trademarks must remain in English even when they appear within text in a language other than English. With Apple’s approval, a translation of the legal notice and credit lines (but not the trademarks) can be used in materials distributed outside the U.S.

For more information about using Apple trademarks, see [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html).

## Platform considerations

*No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| June 9, 2025 | Updated guidance to include demo App Clips. |
| May 2, 2023 | Consolidated guidance into one page. |

## Related guidelines

- [Apple Pay](apple-pay.md)
- [Sign in with Apple](sign-in-with-apple.md)

---


<a id="apple-in-app-purchase"></a>
## apple-in-app-purchase

# Apple In-App Purchase

> Source: <https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase>
> Section: Technologies
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2026-09-17 (Rebranded as Apple In-App Purchase and refined guidance to reflect current best practices.)

People can use Apple In-App Purchase to pay for digital goods and services, like premium content and subscriptions, securely within your app.

---

You can also promote and offer your Apple In-App Purchase items directly through the App Store.

> **Tip:** Apple In-App Purchase and [Apple Pay](apple-pay.md) are different technologies that support different use cases. Use Apple In-App Purchase to sell virtual goods in your app, such as premium content for your app and subscriptions for digital content. Use Apple Pay in your app to sell physical goods like groceries, clothing, and appliances; for services such as club memberships, hotel reservations, and event tickets; and for donations.

Apple In-App Purchase supports four types of content:

- *Consumable* content like lives or gems in a game. After purchase, consumable content depletes as people use it, and people can purchase it again.
- *Non-consumable* content like premium features in an app. Purchased non-consumable content doesn’t expire.
- *Auto-renewable subscriptions* to virtual content, services, and premium features in your app on an ongoing basis. An auto-renewable subscription continues to automatically renew at the end of each subscription period until people choose to cancel it.
- *Non-renewing subscriptions* to a service or content that lasts for a limited time, like access to an in-game battle pass. People purchase a non-renewing subscription each time they want to extend their access to the service or content.

For marketing and business guidance, see [Apple In-App Purchase](https://developer.apple.com/in-app-purchase/) and [Auto-renewable subscriptions](https://developer.apple.com/app-store/subscriptions/). For information about what you can and can’t sell in your app, including usage requirements and restrictions for Apple In-App Purchase, see [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/). For developer guidance, see [Apple In-App Purchase](https://developer.apple.com/documentation/storekit/in-app-purchase).

> **Note:** For apps with exceptionally large, frequently updated catalogs of one-time purchases or subscription content from multiple creators, or apps that provide subscriptions with optional add-on content as a single purchase within the app, the Advanced Commerce API allows you to manage your catalog of Apple In-App Purchase items directly. See [the Advanced Commerce API App Store support page](https://developer.apple.com/in-app-purchase/advanced-commerce-api/) for an overview, and see [Advanced Commerce API](https://developer.apple.com/documentation/advancedcommerceapi) for developer guidance.

## Best practices

**Let people experience your app before making a purchase.** People may be more inclined to invest in paid items or features after they’ve enjoyed your app and discovered its value. If you offer [Auto-renewable subscriptions](#auto-renewable-subscriptions), consider supporting limited free access to your content.

**Design an integrated shopping experience.** You don’t want people to think they’ve entered a different app when they browse and purchase your digital products. Present products and handle transactions in ways that mirror the style of your app.

**Use simple, succinct product names and descriptions.** Titles that don’t truncate or wrap and plain, direct language can help people find products quickly.

**Display the total billing price for each in-app purchase you offer, regardless of type.** People need to know the total billing amount for every purchase they consider.

**Display your store only when people can make payments.** If someone canʼt make payments — for example, because of parental restrictions — consider hiding your store or displaying UI that explains why the store isnʼt available. For developer guidance, see [canMakePayments](https://developer.apple.com/documentation/storekit/appstore/canmakepayments).

**Use the default confirmation sheet.** When someone makes a purchase using Apple In-App Purchase, the system displays a confirmation sheet to help prevent accidental purchases. Don’t modify or replicate this sheet.

### Supporting Family Sharing

People can use Family Sharing to share access to their purchased content, such as auto-renewable subscriptions and non-consumable in-app purchases, with up to five additional family members, across all their Apple devices. To encourage people to take advantage of the Family Sharing support you offer, consider the following guidelines.

**Prominently mention Family Sharing in places where people learn about the content you offer.** For example, including “Family” or “Shareable” in a subscription or item name and referring to Family Sharing in your sign-up screen can highlight the feature and help people make an informed choice.

**Help people understand the benefits of Family Sharing and how to participate.** When you turn on Family Sharing, people can receive notifications about the change, depending on their current settings. For example, an existing subscriber whose sharing setting is turned off (the default) receives a notice from Apple that invites them to share their subscription with family members. Similarly, a family member can get a notification about content that’s being shared with them. To learn more about the types of notifications people can receive, see [Auto-renewable subscriptions](https://developer.apple.com/app-store/subscriptions/).

**Aim to customize your in-app messaging so that it makes sense to both purchasers and family members.** For example, when a family member views shared content for the first time, you might welcome them with wording like “Your family subscription includes…”.

### Providing help

Sometimes, people need help with a purchase or want to request a refund. To help make this experience convenient, you can present custom UI within your app that provides assistance, offers alternative solutions, and helps people initiate the system-provided refund flow. For developer guidance, see [beginRefundRequest(for:in:)](https://developer.apple.com/documentation/storekit/transaction/beginrefundrequest(for:in:)-65tph); for related guidance specific to auto-renewable subscriptions, see [Helping people manage their subscriptions](#helping-people-manage-their-subscriptions).

**Provide help that customers can view before they request a refund.** In addition to including a link to the system-provided refund flow, your custom purchase-help screen can provide assistance you tailor to your app. For example, your custom screen might help people resolve problems with missing purchases, answer frequently asked questions about the in-app purchases you offer, and give people ways to submit feedback or contact you directly for support.

**Use a simple title for the refund action, like “Refund” or “Request a Refund”.** The system-provided refund flow makes it clear that people request a refund from Apple, so there’s no need to reiterate this information.

**Help people find the problematic purchase.** For each recent purchase you display, include contextual information that helps people identify the one they want. For example, you might display an image of the product — along with its name and description — and list the original purchase date.

**Consider offering alternative solutions.** For example, if the customer didn’t receive the item they purchased, you might offer immediate fulfillment or a conciliatory item. Regardless of the alternatives you offer, make it clear that people can still request a refund.

**Make it easy for people to request a refund.** Although your purchase-help screen can offer useful information and alternative solutions, make sure this content doesn’t create a barrier to requesting a refund. For example, avoid making people scroll or open another screen to reveal your refund-request button. When people choose your refund-request item, they automatically enter the system-provided refund flow shown below.

**Avoid characterizing or providing guidance on Apple’s refund policies.** For example, don’t speculate about whether customers will receive the refund they request. To help people understand the refund-request process, you can provide a link to [Request a refund for apps or content that you bought from Apple](https://support.apple.com/en-us/HT204084).

## Auto-renewable subscriptions

**Call attention to subscription benefits during onboarding.** By showing the value of your subscription when people first launch your app, you can educate them on how the app works and help them understand what they’ll gain by subscribing. Include a strong call to action and a clear summary of subscription terms (see [Making signup effortless](#making-signup-effortless)). For related guidance, see [Onboarding](onboarding.md).

**Offer a range of content choices, service levels, and durations.** People appreciate the flexibility to choose the subscription that best meets their needs.

**Consider letting people try your content for free before signing up.** Limited free access gives people the opportunity to sample your content and encourages people who already engaged with your content to sign up. For example, you might offer a freemium app, a metered paywall, or a free trial.

*Illustrated: Freemium app, Metered paywall, Free trial.*

**Prompt people to subscribe at relevant times, like when they near their monthly limit of free content.** Additionally, consider making it easy for people to subscribe at any time by including prompts at relevant points throughout your app.

**Encourage a new subscription only when someone isn’t already a subscriber.** Otherwise, people may believe their existing subscription has lapsed when that’s not actually the case. If you offer the same subscription options in multiple apps or through your website, provide a sign-in option so people don’t think they have to pay multiple times for the same service.

### Making signup effortless

A simple and informative sign-up experience makes it easy for people to act on their interest in your content, whether they’re in your app or viewing your App Store product page.

**Provide clear, distinguishable subscription options.** Use short, self-explanatory names that differentiate subscription options from one another, and specify the price and duration for each option. If you offer an introductory price, be sure to list the introductory price, the duration of the offer, and the standard price the customer pays after the offer ends.

**Simplify initial signup by asking only for necessary information.** A lengthy sign-up process may lower your subscription conversion rate. Defer asking for additional information until after people have signed up.

**In your tvOS app, help people sign up or authenticate using another device.** Instead of asking people to input information in your tvOS app, send a code to another device where they can enter the information you need.

**Give people more information in your app’s sign-up screen.** In addition to including links to your Terms of Service and Privacy Policy in your app and App Store metadata, the in-app sign-up screen needs to include:

- The subscription name, duration, and the content or services provided during each subscription period
- The billing amount, correctly localized for the territories and currencies where the subscription is available for purchase
- A way for existing subscribers to sign in or restore purchases

For example, the Forest Explorer sign-up screen displays billing totals for monthly, biannual, and annual subscriptions in the most prominent positions. In subordinate positions, it shows breakdowns of the biannual and annual prices, so that people can compare the values and make an informed choice. The sign-up screen also contains a button that existing subscribers can use to restore their purchases.

**Clearly describe how a free trial works.** It’s particularly important to make sure people know that when the free trial is over, a payment will be automatically initiated for the next subscription period. For example, the Ocean Journal sign-up screen explicitly states both the duration of the free trial and the amount that’s billed when it ends.

**Include a sign-up opportunity in your app’s settings.** App and account settings are common places for people to look for a way to subscribe.

### Supporting offer codes

In iOS and iPadOS, subscription offer codes let you use both online and offline channels to give new, existing, and lapsed subscribers free or discounted access to your subscription content. For example, you might provide offer codes through email, give them out at a store or event, or print one on a physical product.

There are two types of offer codes you can support:

- A *one-time use code* is a unique code you generate in App Store Connect. People can redeem a one-time use code through a redemption URL (a shareable link), within your app (when you support redemption), or by entering it in the App Store, where they’re prompted to install your app if they haven’t already. Consider using one-time use codes when your distribution is small or when you need to restrict access to a code.
- A *custom code* is a code you create, such as NEWYEAR or SPRINGSALE. People can redeem a custom code through a redemption URL or within your app (when you support redemption). Consider using a custom code when you want to support a large campaign that requires a mass distribution of codes.

For developer guidance on implementing offer codes, see [Offer codes](https://developer.apple.com/app-store/subscriptions/#offer-codes) and [Set up offer codes](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-subscription-offer-codes). For guidance on other types of offers, see [Providing subscription offers](https://developer.apple.com/app-store/subscriptions/#providing-subscription-offers).

**Clearly explain offer details.** To help people make an informed decision, provide a straightforward and succinct description of your offer in your marketing materials.

**Follow guidelines for creating a custom code.** A custom code can contain only alphanumeric ASCII characters. Don’t use special characters, including Chinese and Arabic characters.

**Tell people how to redeem a custom code.** Because people can’t redeem a custom code by entering it in their App Store account settings, it’s important to let them know that they can redeem it through a redemption URL or within your app.

**Consider supporting offer redemption within your app.** The system automatically provides screens that present the offer-redemption flow, whether people redeem the offer in your app or in the App Store. When you use StoreKit API to let people redeem offer codes within your app, the only custom UI you need to create is one that initiates the system-provided flow. For developer guidance, see [presentOfferCodeRedeemSheet(from:options:)](https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(from:options:)-89agc) and [offerCodeRedemption(options:isPresented:onCompletion:)](https://developer.apple.com/documentation/swiftui/view/offercoderedemption(options:ispresented:oncompletion:)). There are several natural places to provide this custom UI. For example, you could add a “Redeem Code” button to your paywall, onboarding screens, or your app’s settings screen.

After people tap your custom redeem button, the system automatically provides a series of code-redemption screens like the ones shown below.

**Supply an engaging and informative promotional image.** Creating this optional image can help people understand the value of your content. If you don’t supply a promotional image, the code redemption screens use your app icon by default. To learn more, see [Promoting your in-app purchases](https://developer.apple.com/app-store/promoting-in-app-purchases/).

**Help people benefit from unlocked content as soon as they complete the redemption flow.** Think about ways to align the post-redemption experience in your app with the subscriber’s new status. For example, you might provide a welcome experience for new subscribers or a brief tour of new features for an existing subscriber who’s unlocked additional functionality. In particular, be prepared to welcome people who subscribe before they open your app for the first time. For example, if you require people to create an account or sign in before they can use your app, make this process as smooth as possible for new subscribers who haven’t experienced it before.

### Helping people manage their subscriptions

Supporting subscription management means people can upgrade, downgrade, or cancel a subscription without leaving your app. Offering subscription management within your app also gives you a natural place to provide help for common subscriber issues and present alternative offers for people to consider.

**Provide summaries of the customer’s subscriptions.** In particular, people appreciate viewing the upcoming renewal date without having to search for it. Consider displaying this information in a settings or account screen, near the subscription-management option. For developer guidance, see [Product.SubscriptionInfo](https://developer.apple.com/documentation/storekit/product/subscriptioninfo).

**Consider using the system-provided subscription-management UI.** Using StoreKit APIs lets you present a consistent experience that helps people manage or cancel their subscriptions without leaving your app. For developer guidance, see [showManageSubscriptions(in:)](https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(in:)).

**Encourage a subscriber to keep their subscription or resubscribe later.** When someone attempts to cancel, consider reminding them what they’d lose access to, suggesting a different plan, or offering a discount to encourage them to stay subscribed. If someone still cancels, consider reaching out later with a personalized, discounted offer to resubscribe. For developer guidance, see [Retention Messaging API](https://developer.apple.com/documentation/retentionmessaging) and [Win-back offers](https://developer.apple.com/app-store/subscriptions/#win-back-offers).

**Always make it easy for customers to cancel an auto-renewable subscription.** If the manage subscription action is deep within an app — or hard to recognize — subscribers can feel they’re being discouraged or prevented from canceling.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.*

## Change log

| Date | Changes |
| --- | --- |
| September 17, 2026 | Rebranded as Apple In-App Purchase and refined guidance to reflect current best practices. |
| September 12, 2023 | Updated artwork and guidance for redeeming offer codes. |
| November 3, 2022 | Added a guideline for displaying the total billing price for every in-app purchase item and consolidated guidance into one page. |

---


<a id="apple-pay"></a>
## apple-pay

# Apple Pay

> Source: <https://developer.apple.com/design/human-interface-guidelines/apple-pay>
> Section: Technologies
> Platforms covered: iOS, iPadOS, macOS (guidance specific to visionOS, watchOS omitted)
> Last change on Apple's site: 2026-06-08 (Refined guidance to reflect the latest Apple Pay appearance and capabilities.)

Apple Pay is a secure, easy way to make payments for physical goods and services, donations, and subscriptions in apps and in any browser.

---

Use Apple Pay to sell physical goods like groceries, clothing, and appliances; for services such as club memberships, hotel reservations, and event tickets; and for donations. Apps and websites that accept Apple Pay display it as an available payment option and include an Apple Pay button in the purchasing flow that people use to bring up a payment sheet.

During checkout, the payment sheet can show the credit or debit card linked to Apple Pay, purchase amount (including tax and fees), shipping options, contact information, and other relevant details. People make any necessary adjustments and then authorize payment and complete the purchase using credentials stored securely on the device.

People pay using Face ID, Touch ID, or Optic ID on supported devices, or by double-clicking on Apple Watch. In browsers, they can also pay using a nearby iPhone or Apple Watch, or by scanning a code with an iPhone or iPad.

For developer guidance, see [Apple Pay](https://developer.apple.com/documentation/passkit/apple-pay) and [Apple Pay on the Web](https://developer.apple.com/documentation/applepayontheweb). For a hands-on demo of Apple Pay on the web, see [Apple Pay on the web interactive demo](https://applepaydemo.apple.com).

> **Note:** Use [Apple In-App Purchase](apple-in-app-purchase.md) to sell virtual goods in your app, such as premium content, and subscriptions for digital content.

## Offering Apple Pay

**Offer Apple Pay on all devices and browsers that support it.** If the device doesn’t support Apple Pay, don’t present Apple Pay as a payment option. For developer guidance, see [PKPaymentAuthorizationController](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller) (iOS, watchOS) and [applePayCapabilities](https://developer.apple.com/documentation/applepayontheweb/applepaysession/applepaycapabilities) (web).

**Make Apple Pay the primary payment option when credentials are available.** If you use Apple Pay APIs to find out whether someone has an active card in Wallet, you must make Apple Pay the primary — but not necessarily sole — payment option everywhere you use the APIs. Don’t separate Apple Pay into a different step or flow. For example, you might pre-select Apple Pay when displaying it alongside other options. For developer guidance, see [Offering Apple Pay in Your App](https://developer.apple.com/documentation/passkit/offering-apple-pay-in-your-app) (iOS, watchOS) and [Checking for Apple Pay availability](https://developer.apple.com/documentation/applepayontheweb/checking-for-apple-pay-availability) (web).

**Use Apple Pay buttons only to initiate payment or, when appropriate, the Apple Pay setup process.** When people choose an Apple Pay button to make a purchase, but their device doesn’t have Apple Pay set up, they’re given the opportunity to set up Apple Pay. Don’t use Apple Pay buttons in any other way.

**If you use a custom button to start the Apple Pay payment process, make sure your custom button doesn’t display “Apple Pay” or the Apple Pay logo.** In this scenario, you must let people know that you accept Apple Pay by displaying the [Apple Pay mark](#apple-pay-mark) graphic or referencing Apple Pay in text on the same page that displays your payment button.

**Use the Apple Pay mark graphic only to communicate that you accept Apple Pay.** The Apple Pay mark doesn’t facilitate payment. Never use it as a payment button or position it as a button. When using the Apple Pay mark to indicate Apple Pay as the selected payment method, you can create a separate custom button that matches your app or website design to initiate the Apple Pay payment.

**Don’t hide an Apple Pay button or make it appear unavailable.** If an Apple Pay button can’t be used yet, such as when a product size or color hasn’t been selected, gracefully point out the problem after someone taps or clicks the button.

**Inform search engines that Apple Pay is accepted on your website.** If your website uses semantic markup to provide product details to search engines, list Apple Pay as a payment option.

> **Important:** All websites that offer Apple Pay must include a privacy statement and adhere to the [Acceptable use guidelines for Apple Pay on the web](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/).

## Streamlining checkout

**Provide a cohesive checkout experience.** It’s best when the entire checkout flow feels tightly integrated with your app or website. Use your branding throughout the checkout experience and avoid opening different pages or windows. For website checkout flows in particular, opening new windows during the process can cause confusion and may even lead people to think they’ve been handed off to a different website.

**If Apple Pay is available, assume people want to use it.** Consider presenting the Apple Pay button as the first payment option, displaying it larger than other options, or using a line to visually separate it from other choices.

**Accelerate single-item purchases with Apple Pay buttons on product detail pages.** In addition to a shopping cart, consider offering Apple Pay buttons on product detail pages so people can purchase an individual item quickly. Purchases initiated in this way need to be for an individual item only, excluding any items already in the cart. If the cart contains the purchased item, remove the item from the cart once the purchase is complete.

**Accelerate multi-item purchases with express checkout.** An express checkout feature immediately shows the payment sheet and lets someone purchase everything in their cart quickly using a single shipping method and destination.

**Support coupons and promotional codes in the payment sheet.** If you offer a coupon or promotional code, let people enter it directly on the payment sheet rather than requiring a separate step. This is especially important for express checkout flows, where people bypass the standard checkout experience.

**Collect necessary information, like color and size options, before people reach the Apple Pay button.** When information is missing at checkout time — perhaps because someone forgot to choose an option — gracefully point out the problem and help them correct it. Use highlighting or warning text to identify missing information, and automatically navigate to the problematic field so people can correct it quickly and complete their purchase.

**Collect optional information before checkout begins.** There’s no way to input optional data — like gift messages or delivery instructions — on the payment sheet, so collect this information ahead of time or even after the purchase is complete.

**Gather multiple shipping methods and destinations before showing the payment sheet.** The payment sheet lets people select a single shipping method and destination for an entire order. If people can choose different shipping methods and destinations for individual items in an order, collect those details before Apple Pay checkout.

**For in-store pickup, help people choose a pickup location before displaying the payment sheet.** After someone chooses a pickup location, show the location’s address on the payment sheet. For developer guidance, see [Displaying a Read-Only Pickup Address](https://developer.apple.com/documentation/passkit/displaying-a-read-only-pickup-address).

**Prefer checkout information from Apple Pay.** Assume that Apple Pay information is complete and up to date. Even if your app or website has existing contact, shipping, and payment information, consider fetching the latest from Apple Pay during checkout to reduce potential corrections.

**Avoid requiring account creation before purchase.** If you want people to register for an account, ask them to do so on the order confirmation page. Prepopulate as many registration fields as possible using information provided during checkout.

**Report transaction results in the payment sheet.** In failure cases, such as a bad address, provide error messages so people can take steps to fix the problem.

**Display an order confirmation or thank-you page.** After the payment sheet shows the result of the transaction, display an order confirmation page to thank people for their purchase, provide details about when the order will ship, and indicate how to check its status. Listing Apple Pay on the confirmation page isn’t necessary, but if you do, show it after the last four digits of the account used to process the transaction or as a separate note. For example, ”1234 (Apple Pay)” or ”Paid with Apple Pay.”

### Customizing the payment sheet

**Only present and request essential information.** People may get confused or have privacy concerns if the payment sheet includes extraneous information. For example, it makes sense to see a contact email address but not a shipping address if the purchase is a gift card that’s delivered electronically. Showing or asking for a shipping address in this scenario may give the false impression that something is physically delivered.

**Display the active coupon or promotional code, or let people enter one.** If people can enter a code before the payment sheet appears, show it on the sheet to reassure them that you applied the code. Consider allowing code entry on the payment sheet as well, particularly in an express checkout flow.

**Let people choose the shipping method in the payment sheet.** To the extent space permits, show a clear description, a cost, and, optionally, an estimated delivery or pickup date — or range of dates — for each available option. Leverage the shipping method’s calendar and time-zone support to provide accurate delivery or pickup information, regardless of the person’s current location. For developer guidance, see [PKDateComponentsRange](https://developer.apple.com/documentation/passkit/pkdatecomponentsrange).

**For in-store pickup, consider letting people choose a pickup window that works for them.** You can use the shipping method to supply a range of dates and times from which people can choose.

**Use line items to explain additional charges, discounts, pending costs, add-on donations, recurring payments, and future payments.** A line item includes a label and cost; a line item for a recurring payment can also include a frequency. Don’t use line items to show an itemized list of products that make up the purchase. For developer guidance, see [paymentSummaryItems](https://developer.apple.com/documentation/passkit/pkpaymentrequest/paymentsummaryitems); for guidance on donations, see [Supporting donations](#supporting-donations).

*Illustrated: iOS, Web.*

**Keep line items short.** Make line items specific and easily understandable at a glance. Whenever possible, fit line items on a single line.

**Provide a business name after the word *Pay* on the same line as the total.** Use the same business name people will see when they look for the charge on their bank or credit card statement. This provides reassurance that payment is going to the right place. For example, Pay [*Business_Name*].

**If you’re not the end merchant, identify both businesses in the payment sheet.** When your app, App Clip, or website acts as an intermediary, such as a marketplace where people buy from third-party sellers, people may not realize two businesses are involved. Clearly describe the relationship in the Pay line using something like *Pay [End_Merchant_Business_Name (via Your_Business_Name)]*.

**Clearly disclose when people may incur additional costs after payment authorization.** In some cases, you may not know the total cost at checkout time. For example, the price of a car ride based on distance or time might change after checkout. Or, someone might want to add a tip after they receive their delivery. In situations like these, and when local regulations allow, you can provide a clear explanation in the payment sheet and a subtotal marked as Amount Pending. If you’re preauthorizing a specific amount, be sure the payment sheet accurately reflects this information.

**Handle data entry and payment errors gracefully.** If an error occurs during checkout, help people resolve it quickly so they can complete their transaction. For related guidance, see [Data validation errors](#data-validation-errors).

**Defer to the payment sheet for progress information during payment.** The payment sheet already presents loading states and progress clearly. Additional spinners or progress indicators can create confusion about the state of the transaction.

## Displaying a website icon

Many websites provide an icon that appears with bookmarks, in URL fields, and on a device’s Home Screen. Websites that support Apple Pay can also use this icon during payment authorization — most notably during Handoff, when a person authorizes payment on a connected device — to provide visual reassurance that payment is going to the right place. For subscription payment flows, the icon can also appear in Wallet.

If your website supports Apple Pay, provide an icon in the following sizes:

| @2x | @3x |
| --- | --- |
| 60x60 pt (120x120 px @2x) | 60x60 pt (180x180 px @3x) |

## Handling problems

Provide clear, actionable guidance when problems occur during checkout or payment processing, so people can resolve them quickly and complete their transaction.

### Data validation errors

Your app or website can respond to user input when the payment sheet appears, when people change certain field values on the payment sheet, and after they authenticate the transaction. Use these opportunities to check for data entry problems and to provide clear and consistent messaging.

*Illustrated: iOS, Web.*

When data is invalid, system-provided error messages highlight relevant fields on the payment sheet. People can choose a field to view additional details and resolve the problem. Provide customized error messages for the detail view that appears when people choose a problematic field.

For developer guidance, see [PKPaymentAuthorizationViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate) (iOS, watchOS) and  [Apple Pay on the Web](https://developer.apple.com/documentation/applepayontheweb) (web).

> **Note:** For privacy reasons, your app or website has limited access to data until people attempt to authorize a transaction. Before authorization, only the card type and a redacted shipping address are accessible. It’s critical to display errors when authorization fails, but to the extent possible, you also need to attempt to validate available information and report problems before authorization.

**Avoid forcing compliance with your business logic.** Design a data validation process that’s intelligent enough to ignore irrelevant data and infer missing data whenever possible. For example, if your app requires a five-digit zip code but someone enters a Zip+4 code, ignore the additional digits rather than asking for a correction. Let people enter phone numbers in multiple formats — such as with and without dashes, and with and without a country code — without producing an error.

**Accurately report problems to the system.** When a problem occurs, provide a custom error message and the correct status code so the system can show the most relevant error on the payment sheet. For developer guidance, see [PKPaymentError](https://developer.apple.com/documentation/passkit/pkpaymenterror) (iOS, watchOS) and [Apple Pay Status Codes](https://developer.apple.com/documentation/applepayontheweb/apple-pay-status-codes) (web).

**Explain the problem clearly and succinctly when data is invalid or incorrectly formatted.** Reference the relevant field and indicate exactly what’s expected. For example, if people enter an invalid zip code, instead of showing “Address is invalid,” show a specific message like “Zip code doesn’t match city.” If the shipping address is unserviceable, indicate why with a message like “Shipping not available for this state.” Use noun phrases with sentence-style capitalization and no ending punctuation. Aim to keep messages at 128 characters or fewer to avoid truncation.

### Payment processing problems

**Handle interruptions correctly.** An event like a cancellation or timeout might interrupt the payment flow, causing the payment sheet to dismiss. When such an event occurs, you must cancel any in-progress payment. After the payment sheet dismisses, people can restart the process by choosing the Apple Pay button again. For developer guidance, see [PKPaymentAuthorizationViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate) (iOS, watchOS) and [oncancel](https://developer.apple.com/documentation/applepayontheweb/applepaysession/oncancel) (web).

## Supporting subscriptions

Your app or website can use Apple Pay to request authorization for recurring payments. A recurring payment can be a fixed amount, such as a monthly movie ticket subscription, or — when local regulations allow — a variable amount like a weekly grocery order. The initial authorization can also include discounts and additional fees.

*Illustrated: iOS, Web.*

**Clarify subscription details before showing the payment sheet.** Before asking people to authorize a recurring payment, make sure they fully understand the billing frequency and any other terms of service. You can show the billing frequency on the payment sheet.

**Include line items that reiterate billing frequency, discounts, and additional upfront fees.** Use these line items to remind people what they’re authorizing. If no payment is required at authorization time, clearly disclose when billing will occur.

*Illustrated: iOS, Web.*

**Clearly communicate trial period terms.** For subscriptions with a trial period, use line items to display the trial amount (including $0 if free), the regular amount after the trial, and the date regular billing begins.

**Clarify the current payment amount in the total line.** Make sure people know the amount they’re being billed at the time of authorization.

**Only show the payment sheet when a subscription change results in additional fees.** When someone changes a subscription, authorization isn’t necessary if the cost decreases or remains the same.

> **Important:** Treat the billing agreement field as a plain-language summary, not a substitute for formal terms. If you use this field, be concise and avoid duplicating information shown elsewhere in your app, website, or line items. When in doubt, leave this field blank to maintain a clean, simple payment sheet.

## Supporting donations

[Approved nonprofits](https://developer.apple.com/support/apple-pay-nonprofits/) can use Apple Pay to accept donations.

**Use a line item to identify a donation.** Display a line item on the payment sheet that reminds people they’re authorizing a donation; for example, display *Donation $50.00*.

**Streamline checkout by offering predefined donation amounts.** You can reduce steps in the donation process by offering recommended donations, like $25, $50, $100. Include an Other Amount option too, so people can customize the donation if they prefer.

## Using Apple Pay buttons

Apple Pay buttons come in several types and styles to fit different contexts and purchase flows. Use the Apple-provided APIs to create them. Doing so gives you:

- Buttons with Apple-approved captions, fonts, colors, and styles
- Content that scales proportionally at any size
- Automatic localization into the device’s language
- Corner radius customization to match your interface
- Built-in VoiceOver support with automatic alternative text

**Always use the Apple-provided API to display Apple Pay buttons.** Unlike button graphics, API-generated buttons always have the correct appearance and are localized automatically. Don’t create custom Apple Pay button designs or try to replicate the Apple-provided ones. For developer guidance, see [PKPaymentButtonType](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype) and [PKPaymentButtonStyle](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle) (iOS and macOS), [WKInterfacePaymentButton](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton) (watchOS), and [Apple Pay on the Web](https://developer.apple.com/documentation/applepayontheweb) (web).

> **Tip:** Use the [Apple Pay mark](#apple-pay-mark) graphic to communicate the availability of Apple Pay wherever you highlight payment options.

### Button types

Choose a button type that best fits the terminology and flow of your purchase or payment experience.

#### Apple Pay button

Use the buttons below to initiate payment. In some contexts, the system automatically displays an image of the default card on payment buttons, letting people know Apple Pay is set up and ready to use.

| Payment button type | Example usage |
| --- | --- |
| *image: button buy with* | An area in an app or website where people can make a purchase, such as a product detail page or shopping cart page. |
| *image: button pay with* | An app or website that lets people pay bills or invoices, such as those for a utility — like cable or electricity — or a service like plumbing or car repair. |
| *image: button check out with* | An app or website offering a shopping cart or purchase experience that includes other payment buttons that start with the text *Check Out*. |
| *image: button continue with* | An app or website offering a shopping cart or purchase experience that includes other payment buttons that start with the text *Continue*. |
| *image: button book with* | An app or website that helps people book flights, trips, or other experiences. |
| *image: button donate with* | An app or website for an [approved nonprofit](https://developer.apple.com/support/apple-pay-nonprofits/) that lets people make donations. |
| *image: button subscribe with* | An app or website that lets people purchase a subscription, such as a gym membership or a meal-kit delivery service. |
| *image: button reload with* | An app or website that uses the term *Reload* to help people add money to a card, account, or payment system associated with a service, such as transit or a prepaid phone plan. |
| *image: button add money with* | An app or website that uses the term *Add Money* to help people add money to a card, account, or payment system associated with a service, such as transit or a prepaid phone plan. |
| *image: button top up with* | An app or website that uses the term *Top Up* to help people add money to a card, account, or payment system associated with a service, such as transit or a prepaid phone plan. |
| *image: button order with* | An app or website that lets people place orders for items like meals or flowers. |
| *image: button rent with* | An app or website that lets people rent items like cars or scooters. |
| *image: button support with* | An app or website that uses the term *Support* to help people give money to projects, causes, organizations, and other entities. |
| *image: button contribute with* | An app or website that uses the term *Contribute* to help people give money to projects, causes, organizations, and other entities. |
| *image: button tip with* | An app or website that lets people tip for goods or services. |
| *image: ap button* | An app or website that has stylistic reasons to use a button that can have a smaller minimum width or that doesn’t specify a call to action. If you choose a payment button type that isn’t supported on the version of the operating system your app or website is running in, the system may replace it with this button. |

#### Set Up Apple Pay button

When a device supports Apple Pay but the person hasn’t set it up yet, you can use the Set Up Apple Pay button to show that you accept Apple Pay, and to give the person an explicit opportunity to set it up. Display the Set Up Apple Pay button in Settings, a user profile, or an interstitial page.

### Button styles

Use the *automatic* style to let the current system appearance determine the appearance of Apple Pay buttons. For developer guidance, see [PKPaymentButtonStyle.automatic](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle/automatic) (apps) and [ApplePayButtonStyle](https://developer.apple.com/documentation/applepayontheweb/applepaybuttonstyle) (web). To control button appearance yourself, choose from the following options.

#### Black

Use on white or light-color backgrounds that provide sufficient contrast. Don’t use on black or dark backgrounds.

#### White with outline

Use on white or light-color backgrounds that don’t provide sufficient contrast. Don’t place on dark or saturated backgrounds.

#### White

Use on dark-color backgrounds that provide sufficient contrast.

### Button size and position

**Prominently display the Apple Pay button.** Make the Apple Pay button no smaller than other payment buttons, and avoid making people scroll to see it.

**Position the Apple Pay button correctly in relation to an Add to Cart button.** In a side-by-side layout, place the Apple Pay button to the right of an Add to Cart button.

In a stacked layout, place the Apple Pay button above an Add to Cart button.

**Adjust the corner radius to match the appearance of other buttons.** By default, an Apple Pay button has rounded corners. You can change the corner radius to produce a button with square corners or a capsule-shape button. For developer guidance, see [cornerRadius](https://developer.apple.com/documentation/passkit/pkpaymentbutton/cornerradius).

**Maintain the minimum button size and margins around the button.** Be mindful that the button title may vary in length depending on the locale.

> **Note:** If the size you specify doesn’t accommodate the translated title for the type of payment button you’re using, the system automatically replaces it with the plain Apple Pay button shown below on the left. There is no automatic replacement for the Set Up Apple Pay button.

Use the following values for guidance.

| Button | Minimum width | Minimum height | Minimum margins |
| --- | --- | --- | --- |
| Apple Pay | 100pt (100px @1x, 200px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |
| Book with Apple Pay | 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |
| Buy with Apple Pay | 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |
| Check Out with Apple Pay | 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |
| Donate with Apple Pay | 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |
| Set Up Apple Pay | 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |
| Subscribe with Apple Pay | 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |

### Apple Pay mark

Use the Apple Pay mark graphic to show that Apple Pay is an available payment option when showing other available payment options. The Apple Pay mark isn’t a button; if you need an Apple Pay button, choose one of the buttons described in [Button types](#button-types). For design guidance related to showing Apple Pay as a payment option, see [Offering Apple Pay](#offering-apple-pay).

**Use only the artwork provided by Apple, with no alterations other than height.** You can specify a height for the Apple Pay mark, but make sure that the height you use is equal to or larger than other payment brand marks in your payment flow. Don’t adjust the width, corner radius, or aspect ratio of the artwork; don’t add a trademark symbol or any other content; don’t remove the border; don’t add visual effects to the mark, such as shadows, glows, or reflections; and don’t flip, rotate, or animate the Apple Pay mark.

**Maintain a minimum clear space around the mark of 1/10 of its height.** Don’t let the Apple Pay mark share its surrounding border with another graphic or button.

Download the Apple Pay mark graphic and full usage guidelines from the [Apple Pay Marketing Guidelines page](https://developer.apple.com/apple-pay/marketing/).

## Referring to Apple Pay

You can use plain text to promote Apple Pay and indicate that Apple Pay is a payment option. As with all Apple product names, use Apple Pay exactly as shown in [Apple Trademark List](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html) — never make it plural or possessive — and adhere to [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html).

**Capitalize Apple Pay in text as it appears in the Apple Trademark List.** Use two words with an uppercase *A*, an uppercase *P*, and lowercase for all other letters. Display Apple Pay entirely in uppercase only when doing so is necessary for conforming to an established typographic style that capitalizes all letters.

**Never use the Apple logo to represent the name *Apple* in text.** In the United States, use the registered trademark symbol (®) the first time Apple Pay appears in body text. Don’t include a registered trademark symbol when Apple Pay appears as a selection option during checkout.

|  | Example text |
| --- | --- |
| ✓ | Purchase with Apple Pay |
| ✓ | Purchase with Apple Pay® |
| ✗ | Purchase with ApplePay |
| ✗ | Purchase with  Pay |
| ✗ | Purchase with APPLE PAY (when not conforming to an interface style that uses only capital letters) |

**Coordinate the font face and size with your app or website.** Don’t mimic Apple typography. Instead, use text attributes that are consistent with the rest of your app or website.

**Don’t translate *Apple Pay* or any other Apple trademark.** Always use Apple trademarks in English, even when they appear within non-English text.

**In a payment selection context, you can display a text-only description of Apple Pay only when all payment options have text-only descriptions.** If any other payment option description includes an icon or logo, you must use the Apple Pay mark graphic as described in [Offering Apple Pay](#offering-apple-pay).

**When promoting Apple Pay in an app, follow App Store guidelines.** For specific guidance, see the [App Store marketing guidelines](https://developer.apple.com/app-store/marketing/guidelines/).

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, visionOS, or watchOS. Not supported in tvOS.*

## Change log

| Date | Changes |
| --- | --- |
| June 8, 2026 | Refined guidance to reflect the latest Apple Pay appearance and capabilities. |
| December 16, 2025 | Clarified supported platforms, including web browsers and Apple Vision Pro. |
| June 10, 2024 | Updated links to developer guidance for offering Apple Pay on the web. |
| September 12, 2023 | Updated artwork. |
| May 2, 2023 | Consolidated guidance into one page. |

---


<a id="augmented-reality"></a>
## augmented-reality

# Augmented reality

> Source: <https://developer.apple.com/design/human-interface-guidelines/augmented-reality>
> Section: Technologies
> Platforms covered: iOS, iPadOS (guidance specific to visionOS omitted)

Augmented reality (or AR) lets you deliver immersive, engaging experiences that seamlessly blend virtual objects with the real world.

---

Using the device’s camera to present the physical world onscreen live, your app can superimpose three-dimensional virtual objects, creating the illusion that these objects actually exist. Depending on the platform and the experiences your app offers, people can reorient the device to explore the objects from different angles, interact with objects using gestures and movement, and even join other people in multiuser AR experiences. For developer guidance, see [ARKit](https://developer.apple.com/documentation/arkit).

**Offer AR features only on capable devices.** If your app’s primary purpose is AR, make your app available only to devices that support ARKit. If your app includes features that require specific AR capabilities, or if AR features are optional in your app, don’t show people an error if they try to use these features on a device that doesn’t support them; instead, simply avoid offering the feature on an unsupported device. For developer guidance, see [Verifying Device Support and User Permission](https://developer.apple.com/documentation/arkit/verifying-device-support-and-user-permission).

> **Note:** The following guidance applies to apps that run in iOS and iPadOS. To learn about using ARKit to create immersive augmented reality experiences in visionOS, see [ARKit](https://developer.apple.com/documentation/arkit).

## Best practices

**Let people use the entire display.** Devote as much of the screen as possible to displaying the physical world and your app’s virtual objects. Avoid cluttering the screen with controls and information that diminish the immersive experience.

**Strive for convincing illusions when placing realistic objects.** Design detailed 3D assets with lifelike textures to create objects that appear to inhabit the physical environment in which you place them. Using information from ARKit, you can scale objects properly and position them on detected real-world surfaces, reflect environmental lighting conditions and simulate camera grain, cast top-down diffuse object shadows on real-world surfaces, and update visuals as the camera’s position changes. To help avoid breaking the illusion you create, make sure your app updates scenes 60 times per second so objects don’t appear to jump or flicker.

**Consider how virtual objects with reflective surfaces show the environment.** Reflections in ARKit are approximations based on the environment captured by the camera. To help maintain the illusion that an AR experience is real, prefer small or coarse reflective surfaces that downplay the effect of these approximations.

**Use audio and haptics to enhance the immersive experience.** A sound effect or bump sensation is a great way to confirm that a virtual object has made contact with a physical surface or other virtual object. Background music can also help envelop people in the virtual world. For guidance, see [Playing audio](playing-audio.md) and [Playing haptics](playing-haptics.md).

**Minimize text in the environment.** Display only the information that people need for your app experience.

**If additional information or controls are necessary, consider displaying them in screen space.** Content in *screen space* appears fixed to a consistent location either in the virtual world or, less commonly, on the device screen. It’s typically easy for people to find and view content in screen space because it remains stationary while the underlying AR environment moves with the device.

**Consider using indirect controls when you need to provide persistent controls.** *Indirect controls* are not part of the virtual environment — instead, they are 2D controls displayed in screen space. If people need access to persistent controls in your app, consider placing the controls so that people don’t have to adjust how they’re holding the device to reach them. Also, consider using translucency in an indirect control to help avoid blocking the underlying scene. For example, the Measure app uses screen space to display a mix of translucent and opaque controls that people use to measure objects in the real world.

**Anticipate that people will use your app in a wide variety of real-world environments.** People may open your app in a place where there isn’t much room to move around or there aren’t any large, flat surfaces. Clearly communicate your app’s requirements and expectations to people up front to help them understand how their physical environment can affect their AR experience. You might also consider offering different sets of features for use in different environments.

**Be mindful of people’s comfort.** Holding a device at a certain distance or angle for a prolonged period can be fatiguing. To help avoid causing fatigue, consider placing objects at a distance that reduces the need to move the device closer to the object; in a game, consider keeping levels short and intermixed with brief periods of downtime.

**If your app encourages people to move, introduce motion gradually.** For example, you might not want to make people dodge a virtual projectile as soon as they enter your AR game. Give people time to adapt to the AR experience in your app and then progressively encourage movement.

**Be mindful of people’s safety.** When people are immersed in an AR experience, they’re not necessarily aware of their physical surroundings, so making rapid, sweeping, or expansive motions might be dangerous. Consider ways of making your app safe to operate; for example, a game could avoid encouraging large or sudden movements.

## Providing coaching

Before people can enjoy an AR experience in your app, they need to move their device in ways that lets ARKit evaluate the surroundings and detect surfaces. Consider using the built-in coaching view to show people what to do and provide feedback during the initialization process. You can also use the coaching view to help people reinitialize AR — a process known as *relocalization* — after an AR experience is interrupted by, for example, people switching briefly to a different app. For guidance on relocalization, see [Handling interruptions](#handling-interruptions); for developer guidance, see [ARCoachingOverlayView](https://developer.apple.com/documentation/arkit/arcoachingoverlayview).

**Hide unnecessary app UI while people are using a coaching view.** By default, the coaching view appears automatically when initialization or relocalization starts, so be prepared to hide unrelated UI to help people concentrate on the coaching view’s instructions.

**If necessary, offer a custom coaching experience.** Although you can configure the system-provided coaching view to help people provide specific information — such as the detection of a horizontal or vertical plane — you might need additional information or want to use a different visual style. If you want to design a custom coaching experience, use the system-provided coaching view for reference.

## Helping people place objects

**Show people when to locate a surface and place an object.** You can use the system-provided coaching view to help people find a horizontal or vertical flat surface on which to place an object. After ARKit detects a surface, your app can display a custom visual indicator to show when object placement is possible. You can help people understand how the placed object will look in the environment by aligning your indicator with the plane of the detected surface.

**When people place an object, immediately integrate that object into the AR environment.** Although surface detection quickly and progressively refines accuracy, it’s best to avoid waiting for more accurate data before placing an object. Use the information available to respond instantly when people place an object; then, when surface detection completes, subtly refine the object’s position if necessary. For example, if people place an object beyond the bounds of the detected surface, gently nudge the object back onto the surface. For developer guidance on refining an object’s position, see [ARTrackedRaycast](https://developer.apple.com/documentation/arkit/artrackedraycast).

**Consider guiding people toward offscreen virtual objects.** Sometimes, it can be difficult for people to locate an object that’s positioned offscreen. When this is the case, you can help people find such objects by offering visual or audible cues. For example, if an object is offscreen to the left, you could display an indicator along the left edge of the screen that guides people to point the camera in that direction.

**Avoid trying to precisely align objects with the edges of detected surfaces.** In AR, surface boundaries are approximations that may change as people’s surroundings are further analyzed.

**Incorporate plane classification information to inform object placement.** For example, only let people place a virtual piece of furniture on a plane that’s classified as “floor,” or require a plane to be classified as “table” in order to place a virtual game board.

## Designing object interactions

**Let people use direct manipulation to interact with objects when possible.** It’s more immersive and intuitive when people can interact with onscreen 3D objects by touching them directly, than by using indirect controls in screen space. However, in situations where people are moving around as they use your app, indirect controls can work better.

**Let people directly interact with virtual objects using standard, familiar gestures.** For example, consider supporting a single-finger drag gesture for moving objects, and a two-finger rotation gesture for spinning objects. For guidance, see [Gestures](gestures.md).

**In general, keep interactions simple.** Touch gestures are inherently two-dimensional, but an AR experience involves the three dimensions of the real world. Consider the following approaches to simplifying people’s interactions with virtual objects.

**Respond to gestures within reasonable proximity of interactive virtual objects.** It can be difficult for people to be precise when aiming to touch specific points on objects that are small, thin, or placed at a distance. When your app detects a gesture near an interactive object, it’s usually best to assume that people want to affect that object.

**Let people initiate object scaling when it makes sense in your app.** For example, if your app lets people explore an imaginary environment, it probably makes sense to support object scaling because your app doesn’t need to represent the real world. On the other hand, if your app helps shoppers decide on furniture to buy, letting people scale a chair object doesn’t help them visualize how the chair will look in a room.

> **Tip:** Regardless of the purpose of your app, don’t use scaling as a way to adjust the distance of an object. If you enlarge a distant object in an effort to make it appear closer, the result is a larger object that still looks far away.

**Be wary of potentially conflicting gestures.** A two-finger pinch gesture, for example, is similar to a two-finger rotation gesture. If you implement two similar gestures like this, be sure to test your app and make sure they’re interpreted properly.

**Strive for virtual object movement that’s consistent with the physics of your app’s AR environment.** People don’t necessarily expect an object to move smoothly over a rough or uneven surface, but they do expect objects to remain visible during movement. Aim to keep moving objects attached to real-world surfaces and avoid causing objects to jump or vanish and reappear as people resize, rotate, or move them.

**Explore even more engaging methods of interaction.** Gestures aren’t the only way for people to interact with virtual objects in AR. Your app can use other factors, like motion and proximity, to bring content to life. A game character, for example, could turn its head to look at a person as they walk toward it.

## Offering a multiuser experience

When multiple people share your app’s AR experience, each participant maps the environment independently and ARKit automatically merges the maps. For developer guidance, see [isCollaborationEnabled](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/iscollaborationenabled).

**Consider allowing people occlusion.** If your app supports placing virtual objects behind people who appear in the device’s camera feed, enhance the illusion of reality by letting the people occlude the objects. For developer guidance, see [Occluding virtual content with people](https://developer.apple.com/documentation/arkit/occluding-virtual-content-with-people).

**When possible, let new participants enter a multiuser AR experience.** Unless your app requires all participants to join before the experience begins, consider using implicit map merging to let new people quickly join an ongoing AR experience. For developer guidance, see [isCollaborationEnabled](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/iscollaborationenabled).

## Reacting to real-world objects

You can enhance an AR experience by using known images and objects in the real-world environment to make virtual content appear. For example, an app that recognizes theater posters for a sci-fi film could cause virtual space ships to emerge from the posters and fly around the environment. Another example is an app for an art museum that presents a virtual tour guide when it recognizes a sculpture. To support experiences like these, your app provides a set of 2D reference images or 3D reference objects, and ARKit indicates when and where it detects any of these items in the current environment. For developer guidance, see [Detecting Images in an AR Experience](https://developer.apple.com/documentation/arkit/detecting-images-in-an-ar-experience).

**When a detected image first disappears, consider delaying the removal of virtual objects that are attached to it.** ARKit doesn’t track changes to the position or orientation of each detected image. To help prevent virtual objects from flickering, consider waiting up to one second before fading them out or removing them.

**Limit the number of reference images in use at one time.** Image detection performance works best when ARKit looks for 100 or fewer distinct images in the real-world environment. If you need more than 100 reference images, you can change the set of active reference images based on context. For example, a museum guide app could ask permission to use location services to determine the part of the museum a person is in, and then look only for images displayed in that area.

**Limit the number of reference images requiring an accurate position.** Updating the position of a reference image requires more resources. Use a tracked image when the image may move in the environment or when an attached animation or virtual object is small compared to the size of the image.

## Communicating with people

**If you must display instructional text, use approachable terminology.** AR is an advanced concept that may be intimidating to some people. To help make it approachable, avoid using technical terms like ARKit, world detection, and tracking. Instead, use friendly, conversational terms that most people will understand.

| Do | Don’t |
| --- | --- |
| Unable to find a surface. Try moving to the side or repositioning your phone. | Unable to find a plane. Adjust tracking. |
| Tap a location to place the *[name of object to be placed]*. | Tap a plane to anchor an object. |
| Try turning on more lights and moving around. | Insufficient features. |
| Try moving your phone more slowly. | Excessive motion detected. |

**In a three-dimensional context, prefer 3D hints.** For example, placing a 3D rotation indicator around an object is more intuitive than displaying text-based instructions in a 2D overlay. Avoid displaying textual overlay hints in a 3D context unless people aren’t responding to contextual hints.

**Make important text readable.** Use screen space to display text used for critical labels, annotations, and instructions. If you need to display text in 3D space, make sure the text faces people and that you use the same type size regardless of the distance between the text and the labeled object.

**If necessary, provide a way to get more information.** Design a visual indicator that fits with your app experience to show people that they can tap for more information.

## Handling interruptions

ARKit can’t track device position and orientation during an interruption, such as when people briefly switch to another app or accept a phone call. After an interruption ends, previously placed virtual objects are likely to appear in the wrong real-world positions. When you support relocalization, ARKit attempts to restore those virtual objects to their original real-world positions using new information. For developer guidance, see [Managing Session Life Cycle and Tracking Quality](https://developer.apple.com/documentation/arkit/managing-session-life-cycle-and-tracking-quality).

**Consider using the system-provided coaching view to help people relocalize.** During relocalization, ARKit attempts to reconcile its previous state with new observations of the current environment. To make these observations more useful, you can use the coaching view to help people return the device to its previous position and orientation.

**Consider hiding previously placed virtual objects during relocalization.** To avoid flickering or other unpleasant visual effects during relocalization, it can be best to hide virtual objects and redisplay them in their new positions.

**Minimize interruptions if your app supports both AR and non-AR experiences.** One way to avoid interruptions is by embedding a non-AR experience within an AR experience so that people can handle the task without exiting and re-entering AR. For example, if your app helps people decide on a piece of furniture to purchase by placing the item in a room, you might let them change the upholstery without leaving the AR experience.

**Allow people to cancel relocalization.** If people don’t position and orient their device near where it was before an interruption, relocalization continues indefinitely without success. If coaching people to resume their session isn’t successful, consider providing a reset button or other way to restart the AR experience.

**Indicate when the front-facing camera is unable to track a face for more than about half a second.** Use a visual indicator to indicate that the camera can no longer track the person’s face. If you need to provide text instructions in this situation, keep them to a minimum.

## Suggesting problem resolutions

**Let people reset the experience if it doesn’t meet their expectations.** Don’t force people to wait for conditions to improve or struggle with object placement. Give them a way to start over again and see if they have better results.

**Suggest possible fixes if problems occur.** Analysis of the real-world environment and surface detection can fail or take too long for a variety of reasons — insufficient light, an overly reflective surface, a surface without enough detail, or too much camera motion. If your app is notified of these problems, use straightforward, friendly language to offer suggestions for resolving them.

| Problem | Possible suggestion |
| --- | --- |
| Insufficient features detected. | Try turning on more lights and moving around. |
| Excessive motion detected. | Try moving your phone slower. |
| Surface detection takes too long. | Try moving around, turning on more lights, and making sure your phone is pointed at a sufficiently textured surface. |

## Icons and badges

Apps can display an AR icon in controls that launch ARKit-based experiences. You can download this icon in [Resources](https://developer.apple.com/design/resources/#ios-apps).

**Use the AR glyph as intended.** The glyph is strictly for initiating an ARKit-based experience. Never alter the glyph (other than adjusting its size and color), use it for other purposes, or use it in conjunction with AR experiences not created using ARKit.

**Maintain minimum clear space.** The minimum amount of clear space required around an AR glyph is 10% of the glyph’s height. Don’t let other elements infringe on this space or occlude the glyph in any way.

Apps that include collections of products or other objects can use badging to identify specific items that can be viewed in AR using ARKit. For example, an app that sells vintage collectibles might use a badge to mark items that people can preview in their home before making a purchase.

**Use the AR badges as intended and don’t alter them.** You can download AR badges, available in collapsed and expanded form, in [Resources](https://developer.apple.com/design/resources/#ios-apps). Use these images exclusively to identify products or other objects that can be viewed in AR using ARKit. Never alter the badges, change their color, use them for other purposes, or use them in conjunction with AR experiences not created with ARKit.

**Prefer the AR badge to the glyph-only badge.** In general, use the glyph-only badge for constrained spaces that can’t accommodate the AR badge. Both badges work well at their default size.

**Use badging only when your app contains a mixture of objects that can be viewed in AR and objects that cannot.** If all objects in your app can be viewed in AR, then badging is redundant.

**Keep badge placement consistent and clear.** A badge looks best when displayed in one corner of an object’s photo. Always place it in the same corner and make sure it’s large enough to be seen clearly (but not so large that it occludes important detail in the photo).

**Maintain minimum clear space.** The minimum amount of clear space required around an AR badge is 10% of the badge’s height. Don’t allow other elements to infringe on this space and occlude the badge in any way.

## Platform considerations

*No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, or watchOS.*

## Related guidelines

- [Playing haptics](playing-haptics.md)
- [Gestures](gestures.md)

---


<a id="generative-ai"></a>
## generative-ai

# Generative AI

> Source: <https://developer.apple.com/design/human-interface-guidelines/generative-ai>
> Section: Technologies
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2026-06-08 (Added guidance for letting people refine results and providing feedback during content generation, and updated guidance for choosing a model type.)

Generative AI empowers you to enhance your app or game with dynamic content and offer intelligent features that unlock new levels of creativity, connection, and productivity.

---

Generative artificial intelligence uses [machine learning](machine-learning.md) models to create and transform text, images, and other content. Use it to offer novel, delightful features that help people express themselves creatively, communicate effectively, and complete tasks more easily. For instance, generative AI can enable people to edit text, create imaginative stories and images, or interact with a character in a game that uses AI-generated dialog.

## Best practices

**Design your experience responsibly.** Responsible AI is the intentional design and development of AI features that considers their direct and indirect impacts on people, systems, and society. With generative AI, it’s often easy to quickly prototype an exciting new feature for your app, yet challenging to create a robust experience that works in all real-world situations. Unlike classic programming, small changes to inputs (or even the same input, when given multiple times) often produce very different outcomes with generative AI. You also can’t always anticipate what requests people will make and how the AI will respond. Orient your design process around crafting AI experiences that are inclusive, designed with care, and protect privacy.

**Keep people in control.** While AI can manipulate and create content, respect people’s agency and ensure they remain in charge of decision making and the overall experience. Honor their requests when in scope and the expected output is clear, and handle sensitive content carefully. Give them the ability to dismiss new content they don’t want, and revert or retry content transformations or other actions they don’t agree with. Clearly identify when and where you use AI.

**Ensure an inclusive experience for all.** AI models learn from data and tend to favor the most common information. This may lead to harmful, unintended biases and stereotypes. Take extra care when designing your AI feature to consider how assumptions and personal attributes might impact the feature you have in mind. For example, if you generate images or descriptions of people, ask people to provide the information needed for the feature to work well rather than solely inferring personal or cultural characteristics. Seek clarity before making assumptions that may lead to common stereotypes, such as about gender identities or relationship types. Test your feature across a diverse set of people to identify and correct stereotypes, and ensure inclusive results. For guidance, see [Inclusion](inclusion.md) and [Accessibility](accessibility.md).

**Design engaging and useful generative features.** Generative AI is a powerful tool, but it’s not the right solution for every situation. Offer generative features when and where they provide clear and specific value, like time savings, improved communication, or enhanced creativity.

**Ensure a great experience even when generative features aren’t available or people opt not to use them.** In some cases, generative AI may be essential to an experience, and there’s no reasonable non-AI substitute. In other cases, AI may play a complementary role that enhances your app’s core functionality, but isn’t critical for people achieving their goals. For example, Genmoji offers a fun way to create new, original emoji, but people can still use regular emoji too. The Apple Intelligence summarization feature makes catching up with notifications faster, but people can still read notifications without it. When possible, consider offering a non-AI fallback.

## Transparency

**Communicate where your app uses AI.** Letting people know when and where your app uses AI sets expectations and gives people the opportunity to knowingly choose to use an AI-powered feature. Never trick someone into thinking they’re interacting with or viewing content authored by a human if they’re actually interacting with AI. Ensure your approach to disclosure aligns with any regulations in the regions where you offer your app.

**Set clear expectations about what your AI-powered feature can and can’t do.** Clarifying your experience’s capabilities and limitations helps people establish a mental model of your feature. For example, when you introduce a feature, you might offer a brief tutorial. For open-ended features like a search bar or generation prompt, consider offering curated suggestions that make it easy to get started. If your feature has known limitations, let people know up front, show them how to get good results, and explain why inferior results occur. For guidance, see [Limitations](machine-learning.md#limitations).

## Privacy

**Choose a model type that fits your feature’s needs and protects people’s privacy.** On-device models keep people’s information on their device, respond quickly, and work offline. When a feature needs more processing power or a larger context size, server-based models are worth considering. Always weigh privacy alongside capability and performance. For any server-based processing, take steps to protect people’s privacy. For example, process as much information locally as possible, and minimize what’s shared. Be transparent by making sure people know their information may be sent to a server, showing them what’s shared, and helping them understand what data may be stored off-device or used for training.

**Ask permission before using personal information and usage data.** Some interactions with an AI model may involve sensitive information, like personal details, messages, photos, and feature usage information. After obtaining permission, use the minimum data you need and always offer a clear way to opt out of its use. If you need sensitive data for model improvement or storage, get explicit permission and handle it with care. If you share data with third parties, understand their approach to privacy. Be aware that model outputs can inadvertently contain sensitive information. Note that [apps for kids](https://developer.apple.com/app-store/kids-apps/) have stricter rules and laws around what data you can use. For guidance, see [Requesting permission](privacy.md#requesting-permission).

**Clearly disclose how your app and its model use and store personal information.** People are more likely to be comfortable sharing data when they understand how it’s used. Empower people to make an informed decision about what data they share with your AI model. When asking for permission to use someone’s information, explain the benefits in a way that’s concise, specific, and easy to understand. Articulate whether your model uses personal information for training and improvement.

## Models and datasets

**Thoughtfully evaluate model capabilities.** There are different types of generative models, some of which possess general knowledge, while others are trained for specific tasks. It’s important to understand the capabilities of any model you consider. As early as you can, get a hands-on look at the models and data available to help orient your design. Keep in mind that some model types may be unavailable to people in certain situations due to factors like device compatibility, network access, and battery level. For example, the [Foundation Models](https://developer.apple.com/documentation/foundationmodels) framework requires a compatible device with Apple Intelligence turned on.

**Be intentional when choosing or creating a dataset.** Whether you’re training a model from scratch or customizing an existing model, the data you choose greatly impacts the model’s behavior. When you teach and evaluate your AI model, choose datasets that include a diverse range of subject matter representations. Learn where your data comes from and how it was gathered. Ensure you have relevant licenses for all data you don’t personally own, and offer appropriate choices when using people’s data. Most datasets gathered from the real world are imperfect, so allow time for testing and evaluation to proactively mitigate bias and misinformation that a model might learn and replicate.

## Inputs

**Guide people on how to use your generative feature.** Consider how to steer and educate people toward producing great results. One technique is to offer diverse, predefined example inputs that hint at what’s possible for a feature.

**Raise awareness about and minimize the chance of hallucinations.** When a generative model is unsure how to respond to a request, it may produce content that seems plausible but is made up. These hallucinations can misinform people because the model may convincingly present the information as factual, even when it’s not. Generative models sometimes get details wrong, like dates of important events or information about people, so it’s important to clearly communicate that AI-generated content may contain errors. You can minimize the chance of hallucinations and limit their impact by carefully scoping what you ask a model to generate. Avoid requesting factual information unless you’re confident the model has access to verified and up-to-date information for the task. Avoid using AI-generated content in situations where a possible hallucination could misinform and harm someone.

**Consider consequences and get permission before performing irreversible or potentially problematic tasks.** Before performing a task, consider whether a mistake or the inability to reverse the action might cause more work or stress for people. Avoid automating destructive actions, like deleting photos, and actions that are hard to undo, like making a purchase on a person’s behalf. Generally, ask for confirmation before performing a significant action on someone’s behalf. Keep in mind that certain situations may be prohibited or have extra rules. Review and adhere to model-specific usage policies, as well as government and regulatory AI policy as it applies to each locale in which the generative features will be available.

## Outputs

**Make it easy for people to refine or revert generated results, and acknowledge when their corrections take effect.** For example, surfacing controls like Edit, Undo, Retry, or Adjust near generated content preserves people’s agency while still letting them benefit from automation. When people adjust or personalize output, provide a clear signal that their action had an effect. This kind of feedback helps people build an accurate mental model of your feature and fosters trust over time.

**Help people improve requests when blocked or undesirable results occur.** Minimize scoped or blocked output by coaching people how to be more successful next time. For example, if prompted to generate harmful content, Image Playground says that it’s “Unable to use that description.” When possible, consider offering example requests that might lead to better results.

**Reduce unexpected and harmful outcomes with thoughtful design and thorough testing.** People generally use apps with good intentions, but harmful outcomes can still arise from both accidental and purposeful misuse, and when responding to potentially sensitive topics. It may not be possible to mitigate every harmful scenario, but taking a proactive approach to identify risks, devising policies to address them, and evaluating features can help minimize the chance of misuse and harm. Consider ways people might interact with your feature and test those scenarios. Challenge your policies and expected use cases. See what happens when requests are out-of-scope, unrelated to the app experience you designed, and not well-represented by the model’s training data. Try requests that are poorly phrased, vague, or ambiguous; include personal, sensitive, or controversial topics; and encourage harmful or incorrect results. Use what you learn to improve your model, inform prevention, and respond thoughtfully.

**Strive to avoid replicating copyrighted content.** Large AI models are trained using vast datasets from the internet and other sources. This means most generative models are familiar with and can unintentionally produce content similar to published work, including copyrighted content. You can reduce the likelihood of copyright infringement by building upon existing models that already protect against this, and by carefully curating inputs. For example, you might let people choose from a set of pre-approved prompts. You could also explicitly tell the model to avoid mimicking certain content or styles.

**Factor processing time into your design.** *Latency* is how much time it takes for a model to produce an output. Non-generative models, such as [body position tracking in ARKit](https://developer.apple.com/documentation/arkit/capturing-body-motion-in-3d) and the [Vision](https://developer.apple.com/documentation/vision) machine learning framework, typically have low latency and are suitable to run in real-time. Generative models typically take longer to produce a result, so design a loading experience or generate in the background while a person uses another part of the app. For guidance, see [Loading](loading.md).

**Consider giving specific, reassuring feedback during generation.** Messages that describe what’s actually happening can be more helpful than a vague status message. For example, instead of “Processing…”, say “Finding substitutions for ingredients” or “Summarizing key themes from your notes.” Specific feedback reduces uncertainty and makes waiting feel purposeful. If something goes wrong, describe what happened in plain language and offer a clear next step.

**Consider offering alternate versions of results.** Depending on the design of your feature, it might work best to present a single result or multiple meaningfully different results from which people can choose. Offering people a choice can give them a greater sense of control and help bridge the gap between the model’s interpretation and what someone actually wants. For example, Image Playground can generate multiple images that represent a person, allowing someone to pick the one they prefer. For guidance, see [Multiple options](machine-learning.md#multiple-options).

## Continuous improvement

**Consider ways to improve your model over time.** You may want to update your model to adapt to people’s behavior, respond to feedback, include new data, and leverage enhanced capabilities. You can make some improvements, such as updating a list of blocked words, frequently and independent of the app development cycle, and you can plan significant improvements and new features around regular app updates. Plan for fine-tuning, retesting, and prompt engineering when updating to a newer, more capable base model. If you train your own model, retrain with additional data and fine-tune to improve performance. Thoroughly test and refine all model updates to identify and correct unexpected behavior.

**Let people share feedback on outputs.** Feedback can help you identify and respond to unexpected outcomes and new potential issues that arise despite thorough testing. Feedback also gives people a way to celebrate what they like best about your AI experience and report concerns when outputs don’t match their expectations. Establish trust by taking feedback seriously and resolving issues quickly. Always make providing feedback voluntary. Respect people’s time by placing a feedback affordance in a clear location that doesn’t interrupt the experience. Consider offering a quick and easy way to give positive and negative feedback, like simple thumbs-up and thumbs-down buttons. You might also offer a way to share detailed feedback for complicated issues. For guidance, see [Explicit feedback](machine-learning.md#explicit-feedback) and [Implicit feedback](machine-learning.md#implicit-feedback).

**Design flexible, adaptable features.** Generative AI is a rapidly advancing technology, and models and their resource needs are constantly evolving. Consider ways your app or game can adapt as capabilities and models improve. For example, you may want to separate your model from your user experience so you can swap out the model for other models over time. Lay a foundation that allows for future adjustments like this, while still offering the same great user experience.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| June 8, 2026 | Added guidance for letting people refine results and providing feedback during content generation, and updated guidance for choosing a model type. |
| June 9, 2025 | New page. |

## Related guidelines

- [Machine learning](machine-learning.md)
- [Inclusion](inclusion.md)
- [Accessibility](accessibility.md)
- [Privacy](privacy.md)
- [Loading](loading.md)

---


<a id="icloud"></a>
## icloud

# iCloud

> Source: <https://developer.apple.com/design/human-interface-guidelines/icloud>
> Section: Technologies
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-06-09 (Added guidance for synchronizing game data through iCloud.)

iCloud is a service that lets people seamlessly access the content they care about — photos, videos, documents, and more — from any device, without performing explicit synchronization.

---

A fundamental aspect of iCloud is transparency. People don’t need to know where content resides. They can just assume they’re always accessing the latest version.

## Best practices

**Make it easy to use your app with iCloud.** People turn on iCloud in Settings and expect apps to work with it automatically. If you think people might want to choose whether to use iCloud with your app, show a simple option the first time your app opens that provides a choice between using iCloud for all data or not at all.

**Avoid asking which documents to keep in iCloud.** Most people expect all of their content to be available in iCloud and don’t want to manage the storage of individual documents. Consider how your app handles and exposes content, and try to perform more file-management tasks automatically.

**Keep content up to date when possible.** In an app that supports iCloud, it’s best when people always have access to the most recent content. However, you need to balance this experience with respect to device storage and bandwidth constraints. If your app works with very large documents, it may be better to let people control when updated content is downloaded. If your app fits in this category, design a way to indicate that a more recent version of a document is available in iCloud. When a document is updating, provide subtle feedback if the download takes more than a few seconds.

**Respect iCloud storage space.** iCloud is a finite resource for which people pay. Use iCloud to store information people create and understand, and avoid using it for app resources or content you can regenerate. Even if your app doesn’t implement iCloud support, remember that iCloud backups include the contents of every app’s Documents folder. To avoid using up too much space, be picky about the content you place in the Documents folder.

**Make sure your app behaves appropriately when iCloud is unavailable.** If someone manually turns off iCloud or turns on Airplane Mode, you don’t need to display an alert notifying them iCloud is unavailable. However, it may still be helpful to unobtrusively let people know that changes they make won’t be available on other devices until they restore iCloud access.

**Keep app state information in iCloud.** In addition to storing documents and other files, you can use iCloud to store settings and information about the state of your app. For example, a magazine app might store the last page viewed so when the app is opened on another device, someone can continue reading from where they left off. If you use iCloud to store settings, make sure it’s for ones people want applied to all of their devices. For example, some settings might be more useful at work than at home.

**Warn about the consequences of deleting a document.** When someone deletes a document in an app that supports iCloud, the document is removed from iCloud and all other devices too. Show a warning and ask for confirmation before performing the deletion.

**Make conflict resolution prompt and easy.** To the extent possible, try to detect and resolve version conflicts automatically. If this can’t be done, display an unobtrusive notification that makes it easy to differentiate and choose between the conflicting versions. Ideally, conflict resolution occurs as early as possible, so time isn’t wasted in the wrong version.

**Include iCloud content in search results.** People with iCloud accounts assume their content is universally available, and they expect search results to reflect this perspective.

**For games, consider saving player progress in iCloud.** Although you can implement this functionality yourself, the GameSave framework offers an efficient solution. It synchronizes save data across devices and offers built-in alerts you can use to help players handle syncing issues during offline play or when conflicts arise. Alternatively, you can implement custom UI that uses GameSave data to resolve these situations. For developer guidance, see [GameSave](https://developer.apple.com/documentation/gamesave).

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| June 9, 2025 | Added guidance for synchronizing game data through iCloud. |

---


<a id="machine-learning"></a>
## machine-learning

# Machine learning

> Source: <https://developer.apple.com/design/human-interface-guidelines/machine-learning>
> Section: Technologies
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2026-06-08 (Made minor updates for clarity.)

Machine learning enables apps and games to learn from data and usage patterns, letting you improve existing experiences and create engaging new ones.

---

In addition to providing familiar features like image recognition and content recommendations, your app can use machine learning to forge deep connections with people and help them accomplish more with less effort.

For related guidance on how to use machine learning models to enable intelligent experiences, see [Generative AI](generative-ai.md).

## Planning your design

Features powered by machine learning use *models* to perform tasks that make people’s experiences more unique, like curated feeds, customized trip itineraries, and personalized search suggestions. These features depend on well-designed models as much as they depend on a well-designed UI and user experience. For insights into the process of designing models, see [Create ML](https://developer.apple.com/documentation/createml).

As you design your models, keep the intended experience of your app in mind. It can take a long time to adjust the behavior of models, so be prepared to change the way you use data and metrics if the app experience needs to change.

Designing the UI and user experience of a machine learning app can be uniquely challenging. Because a machine learning app bases its behavior on the data it receives — reacting to changing information and conditions — you can’t design specific reactions to a static set of scenarios. Instead, you design the experience by teaching the app how to interpret data and react accordingly.

To help you meet this challenge, first consider the role that machine learning plays in your app. Defining the [role](#the-role-of-machine-learning-in-your-app) of machine learning in your app can help you discover areas in which you can explore the ways machine learning can affect the experience your app provides.

Use the machine learning role you identify to help you define ways your app can receive and display data. There are several patterns — grouped into *inputs* and *outputs* — that provide guidance in areas such as getting feedback, displaying data, handling mistakes, and supporting corrections. Use the guidance in these patterns to help you integrate machine learning into your app in ways that people appreciate.

## The role of machine learning in your app

Machine learning systems vary widely, and the ways an app can use machine learning vary widely, too. As you approach the design of your app, think about how its features use machine learning in each of the following areas.

### Critical or complementary

If an app can still work without the feature that machine learning supports, machine learning is complementary to the app; otherwise, it’s a critical dependency. For example:

- The keyboard uses machine learning to provide QuickType suggestions. Because the keyboard still works without these suggestions, machine learning plays a complementary role in the app.
- Face ID relies on machine learning to perform accurate face recognition. Without machine learning, Face ID would not work.

In general, the more central a feature is to your app’s purpose — like a personalized news feed for a news app — the more people expect accurate and reliable results. On the other hand, for secondary features, people are often more forgiving if the results aren’t perfectly accurate every time.

### Private or public

Machine learning results depend on data. To make good design decisions, you need to know as much as possible about the types of data your app’s feature needs. In general, the more sensitive the data, the more serious the consequences of inaccurate or unreliable results. For example:

- If a health app misinterprets data and incorrectly recommends a visit to the doctor, people are likely to experience anxiety and may lose trust in the app.
- If a music app misinterprets data and recommends an artist that people don’t like, they’re likely to view the result as an inconsequential mistake.

As with critical app features, features that use sensitive data must prioritize accuracy and reliability. Regardless of the sensitivity of the data, all apps must protect user privacy at all times.

### Proactive or reactive

A *proactive* feature provides results without people requesting it to do so. Proactive features can prompt new tasks and interactions by providing unexpected, sometimes serendipitous results. In contrast, a *reactive* feature provides results when people ask for them or when they take certain actions. Reactive features typically help people as they perform their current task. For example:

- Siri Suggestions can proactively suggest a shortcut based on people’s recent routines.
- QuickType suggests words in reaction to what people type.

Because people don’t ask for the results that a proactive feature provides, they may have less tolerance for low-quality information. To reduce the possibility that people will find proactive results intrusive or irrelevant, you may need to use additional data for the feature.

### Visible or invisible

Apps may use machine learning to support visible or invisible features. People are usually aware of visible app features because they tend to offer suggestions or choices that people view and interact with. For example, Image Playground lets people describe an image, adjust it visually, or remix results through quick edits.

As the name suggests, an invisible feature provides results that aren’t obvious to people. For example, the News app proactively suggests topics and channels based on a person’s previous engagement. Because this improves the app experience without requiring people to make choices, many people aren’t aware that the feature exists.

People’s impression of the reliability of results can differ depending on whether a feature is visible or invisible. With a visible feature, people form an opinion about the feature’s reliability as they choose from its results. It’s harder for an invisible feature to communicate its reliability — and potentially receive feedback — because people may not be aware of the feature at all.

### Dynamic or static

All machine learning models can improve, but some improve dynamically, as people interact with the feature, and others improve offline and affect the feature only when the app updates.

In addition to the frequency of app updates, static or dynamic improvements can affect other parts of the user experience, too. For example, dynamic features often incorporate forms of [calibration](#calibration) and feedback (either [implicit](#implicit-feedback) or [explicit](#explicit-feedback)), whereas static features might not.

## Explicit feedback

Explicit feedback provides actionable information your app can use to improve the content and experience it presents to people. Unlike [implicit feedback](#implicit-feedback) — which is information an app gleans from user actions — explicit feedback is information people provide in response to a specific request from the app.

*Favoriting* — marking an item for quick access in the future — and *social feedback* — expressing emotions toward others — are common user interactions that seem like mechanisms that supply explicit feedback. However, these tools actually provide implicit feedback because they don’t support app-specific requests. People use favoriting and social feedback to accomplish their own goals and apps can gather implicit feedback from these interactions.

**Request explicit feedback only when necessary.** People must take action to provide explicit feedback, so it’s best to avoid requesting it if possible. Instead, consider using implicit feedback to learn how people interact with your app without asking them to do extra work.

**Always make providing explicit feedback a voluntary task.** You want to communicate that explicit feedback can help improve the experience without making people feel that providing it is mandatory.

**Use simple, direct language to describe each explicit feedback option and its consequences.** Avoid using imprecise terms such as *dislike* because such terms don’t convey consequences and can be hard to translate. Instead, describe each option in a way that helps people understand what happens when they choose the option, such as:

- Suggest less pop music
- Suggest more thrillers
- Mute politics for a week

**Add icons to an option description if it helps people understand it.** [Icons](icons.md) can help clarify or emphasize part of an option description. Avoid using an icon by itself, because it might not be clear enough to communicate granularity or consequences.

**Consider offering multiple options when requesting explicit feedback.** Providing [multiple options](#multiple-options) can give people a sense of control and help them identify unwanted suggestions and remove them from your app. To help people provide feedback, consider offering options that become progressively more specific so that it’s easy for people to clarify their response.

**Act immediately when you receive explicit feedback and persist the resulting changes.** For example, if people identify content they don’t want to see, hide it from their view and ensure it doesn’t appear elsewhere in your app. When you react immediately to feedback and show that your app remembers it, you build people’s trust in the value of providing it.

**Consider using explicit feedback to help improve when and where you show results.** For example, people might like a result, but they may not want to see it at certain times or in certain contexts. Explicit feedback on when and where to show results can help you fine-tune the experience people have in your app.

## Implicit feedback

Implicit feedback is information that arises as people interact with your app’s features. Unlike the specific responses you get from [explicit feedback](#explicit-feedback), implicit feedback gives you a wide range of information about user behavior and preferences. Although incorporating implicit feedback isn’t required for a great machine learning app, the feedback can help you improve your app’s user experience without asking people to do any extra work.

**Always secure people’s information.** Implicit feedback can gather potentially sensitive user information, so you must be particularly careful to maintain strict controls on user privacy.

**Help people control their information.** As an app developer, you know that the more you understand about the behavior of your users — both within your app and in other apps — the more you can improve the experience your app provides. Although most people understand the benefits of making their information available to multiple apps, they may still be surprised when things they do in one app affect experiences they have in a different app. Worse, people may assume that apps are sharing their private information, which can cause them to lose trust in the apps. It’s important to tell people how your app gets and shares their information and to give people ways to restrict the flow of their information.

**Don’t let implicit feedback decrease people’s opportunities to explore.** Implicit feedback tends to reinforce people’s behavior, which can improve the user experience in the short term, but may worsen it in the long term. For example, it might seem like a good idea to give people a set of suggestions that matches all the things they’re interested in now, but doing so doesn’t encourage them to explore new things.

**When possible, use multiple feedback signals to improve suggestions and mitigate mistakes.** Implicit feedback is indirect, so it can be difficult to discern a person’s actual intent in the information you gather. For example, if someone views a photo, shares it in a message, and adds it to a shared album, it doesn’t necessarily mean they have positive feelings about the photo. Incorporate implicit feedback from multiple sources and interactions to help you avoid misinterpreting people’s intentions.

**Consider withholding private or sensitive suggestions.** People often share their accounts and devices with others, or switch from using a personal device to a communal one. If your app receives implicit feedback related to private or sensitive topics, avoid offering recommendations based on that feedback.

**Prioritize recent feedback.** People’s tastes can change frequently, so base your recommendations on recent implicit feedback. For example, Face ID prioritizes recent facial input because it’s most likely to represent what the person looks like now. If recent feedback isn’t available, you can fall back to historical feedback.

**Use feedback to update predictions on a cadence that matches the person’s mental model of the feature.** For example, people expect typing suggestions to update immediately as they’re typing. On the other hand, giving people continuously updated song recommendations makes it hard to consider individual songs and could make them feel rushed or overwhelmed.

**Be prepared for changes in implicit feedback when you make changes to your app’s UI.** Even small UI changes can lead to noticeable changes in the amount and types of implicit feedback. For example, changing the location of a button can affect how people use it, even if there’s no change in the benefit they get from the button’s action. Take such changes into account when interpreting the implicit feedback you receive from interactions in your app.

**Beware of confirmation bias.** Implicit feedback is constrained by what people can actually see and do in your app and other apps — it rarely gives you insight into new things they might like to do. Avoid relying solely on implicit feedback to inform your results.

## Calibration

Calibration is a process during which people provide information that a feature needs to function. To use Face ID, for example, a person must first scan their face.

In general, only use calibration when your feature can’t function without that initial information. If your feature can work without calibration, consider using other ways to gather the information you need, such as [implicit feedback](#implicit-feedback) or possibly [explicit feedback](#explicit-feedback).

**Always secure people’s information.** During calibration, people may provide sensitive information and you must make sure it remains secure.

**Be clear about why you need people’s information.** Typically, calibration is required before people can use a feature, so it’s essential that they understand the value of providing their information. As you briefly describe how people can benefit from your feature, emphasize what it does rather than how it works.

**Collect only the most essential information.** Designing a unique experience that requests a minimal amount of information can make people more comfortable participating in the process and increase their trust in your app.

**Avoid asking people to participate in calibration more than once.** Also, it’s best when calibration occurs early in the user experience. As people continue using your app or feature, you can use implicit or explicit feedback to evolve your information about them without asking them to participate again. An exception is a feature that needs calibration with an object instead of a person. For example, an app that helps people improve their baseball swing might need to calibrate with each new baseball field.

**Make calibration quick and easy.** Even a brief calibration experience takes time and requires effort from people. An ideal calibration experience makes it easy for people to respond, without compromising the quality of the information they provide. The following guidelines can help you create a streamlined calibration experience.

- Prioritize getting a few pieces of important information and infer the rest from other sources or by getting people’s feedback.
- Avoid asking for information that most people would have to look up.
- Avoid asking people to perform actions that might be difficult.

**Make sure people know how to perform calibration successfully.** After people decide to participate in calibration, give them an explicit goal and show their progress toward it. For example, Face ID calibration briefly describes what people need to do and changes the appearance of the tick marks encircling the face as people progress through scanning.

**Immediately provide assistance if progress stalls.** When progress stalls, people can feel stuck or powerless, and they may lose trust in your app. In this situation, it’s crucial to give people actionable recommendations that quickly get them back on track. As you provide this guidance, never imply that something’s wrong or that people are at fault, and never leave people without a clear next step.

**Confirm success.** The moment people successfully complete calibration, reward their time and effort by giving them a clear path toward using the feature. Providing an explicit completion to the calibration experience reinforces the unique nature of the experience and helps people switch their focus to your feature.

**Let people cancel calibration at any time.** Make sure you give people an easy way to cancel the experience at any point and avoid implying any judgment about their choice. There’s no need to provide any messaging that mentions the canceled calibration, because the next time people attempt to use the feature, they’ll have another chance to participate.

**Give people a way to update or remove information they provided during calibration.** Letting people edit their information gives them more control and can lead them to have greater trust in your app. Although the calibration experience can help people edit their responses, it’s a good idea to let people edit their information outside of the calibration experience so that they feel free to make changes at any time.

## Mistakes

It’s inevitable that your app will make mistakes. Although people may not expect perfection, mistakes can damage their experience and decrease their trust in your app. To help you avoid negative consequences, it’s crucial to:

- Anticipate mistakes. As much as possible, design ways to avoid mistakes and mitigate them when they happen.
- Help people handle mistakes. Mistakes can have a wide range of consequences, so the tools you provide to handle a mistake must be able to address those consequences.
- Learn from mistakes when doing so improves your app. In some cases, learning from a mistake might have undesirable effects, such as causing unpredictability in the user experience. When it makes sense, use each mistake as a data point that can refine your machine learning models and improve your app.

There are several machine learning patterns that can help you address mistakes:

- [Limitations](#limitations) help you set people’s expectations about the accuracy of your suggestions.
- [Corrections](#corrections) give people a way to be successful even when your results are wrong.
- [Attribution](#attribution) gives people insight into where suggestions come from, which can help them understand mistakes.
- [Confidence](#confidence) helps you gauge the quality of your results, which can impact how you present them.
- Feedback — both [explicit](#explicit-feedback) and [implicit](#implicit-feedback) — lets people tell you about mistakes that you might not be aware of.

**Understand the significance of a mistake’s consequences.** For example, incorrect keyboard suggestions might annoy people, but suggesting a travel route that results in a missed flight is a serious inconvenience. Show empathy by providing corrective actions or tools that match the seriousness of the mistake.

**Make it easy for people to correct frequent or predictable mistakes.** If you don’t give people an easy way to correct mistakes, they can lose trust in your app.

**Continuously update your feature to reflect people’s evolving interests and preferences and help avoid mistakes.** For example, you can use implicit feedback to discover changes in people’s tastes and habits. It’s also a good idea to update your feature with domain-specific information, such as current trends in popular entertainment. Ideally, people don’t have to do any work to benefit from improvements in your app.

**When possible, address mistakes without complicating the UI.** Some patterns, such as corrections and limitations, tend to integrate seamlessly with an app’s UI, whereas others, like attributions, can be harder to integrate. Balance a pattern’s effect on the UI with its potential for compounding the mistake. For example, if you update the UI with an attribution that turns out to be wrong, the effect of the original mistake is magnified.

**Be especially careful to avoid mistakes in proactive features.** A proactive feature — like a suggestion based on people’s behaviors — promises valuable results without asking people to do anything to get them. However, because people don’t request a proactive feature, they often have less patience with its mistakes. Mistakes made by proactive features can also cause people to feel that they have less control.

**As you work on reducing mistakes in one area, always consider the effect your work has on other areas and overall accuracy.** For example, optimizing an image-recognition app to improve how it recognizes dogs might result in a decreased ability to recognize cats. As your models evolve, be prepared for mistakes to evolve, too. Use what you know about people’s preferences to help you determine the areas to work on.

## Corrections

People use corrections to fix mistakes that apps make. For example, if a photo app automatically crops a photo in a way people don’t like, they can correct the mistake by cropping the photo in a different way.

**Give people familiar, easy ways to make corrections.** When your app makes a mistake, you don’t want people to be confused about how to correct it. You can avoid causing confusion by showing the steps your app takes as it performs the automated task. For example, Photos highlights the controls it uses to auto-crop a photograph so that people can use the same controls to refine or undo the results.

**Provide immediate value when people make a correction.** Reward people’s effort by instantly displaying corrected content, especially when the feature is critical or you’re responding to direct user input. Also, be sure to persist the updates so people don’t have to make the same corrections again.

**Let people correct their corrections.** Sometimes, people make a correction without realizing that they’ve made a mistake. As you do with all corrections, respond immediately to an updated correction and persist the update.

**Always balance the benefits of a feature with the effort required to make a correction.** People may not mind when a feature that automates a task makes a mistake, but they’re likely to stop using the feature if it seems easier to perform the task themselves.

**Never rely on corrections to make up for low-quality results.** Although corrections can reduce the impact of a mistake, depending on them may erode people’s trust in your app and reduce the value of your feature.

**Learn from corrections when it makes sense.** A correction is a type of [implicit feedback](#implicit-feedback) that can give you valuable information about ways your app doesn’t meet people’s expectations. Before you use a correction to update your models, make sure that the correction will lead to higher quality results.

**When possible, use guided corrections instead of freeform corrections.** Guided corrections suggest specific alternatives, so they require less user effort; freeform corrections don’t suggest specific alternatives, so they require more input from people. An example of guided correction is a speech-to-text feature that gives people a list of alternative text completions from which to choose. In contrast, Photos offers freeform correction so that people can adjust the auto-cropping of a photo as they see fit. If it makes sense in your app, you can support a combination of guided and freeform corrections.

## Multiple options

Depending on the design of your feature, it might work best to present a single result or multiple results from which people can choose. Providing multiple options can give people a greater sense of control and can help bridge the gap between your model’s predictions and what people actually want. Multiple options can also encourage people to have realistic expectations about the types of results your app generates.

You might present multiple options to people in the following contexts:

- Suggested options, a proactive feature that suggests content to people based on their past interactions. For example, For You recommendations from Apple Music.
- Requested options, a reactive feature that suggests potential next steps to people based on their recent actions. For example, QuickType suggestions.
- Corrections, which are actions people take to fix mistakes your app has made when it’s acting on their behalf. For example, the Photos Auto-Crop feature.

**Prefer diverse options.** When possible, balance the accuracy of a response with the diversity of multiple options. For example, Apple Maps generally suggests more than one route to a destination, such as a route without tolls, a scenic route, or a route that uses highways. Providing different types of options helps people choose the one that they prefer and can also suggest new items that might interest them.

**In general, avoid providing too many options.** People must evaluate each option before making a choice, so having more options increases cognitive load. When possible, list options on one screen so people don’t have to scroll to find the right one.

**List the most likely option first.** When you know how your [confidence](#confidence) values correlate with the quality of your results, you might use them to rank the options. You might also consider using contextual information, such as the time of day or the current location, to help you determine the most likely option. If it makes sense in your app, select the first option by default so people can quickly achieve their goals without reading through every option.

**Make options easy to distinguish and choose.** For example, in a routing app, people often need to make route choices quickly to avoid going the wrong way. When options look similar, help people distinguish between them by providing a brief description of each one and taking particular care to highlight the differences. In cases where there are too many options to display in a single view, such as with content recommendations, consider grouping options in categories that people can scan rapidly.

**Learn from selections when it makes sense.** People give you [implicit feedback](#implicit-feedback) every time they make a selection. When it doesn’t adversely affect the user experience, use this feedback to refine the options you provide and increase the chance that you’ll present the most likely option first. In general, continuing to offer incorrect results is likely to decrease people’s trust in the quality of your app’s predictions.

## Confidence

Confidence indicates the measure of certainty for a result. Not all models produce confidence values by default, so you might consider computing them if you can use them to improve the user experience of your app.

Although it might seem like higher confidence produces a higher quality result — and therefore a better user experience — it doesn’t necessarily work that way. You need to verify that your confidence values correspond to the quality of your results. For example, you might review values for multiple confidence thresholds or compare values across multiple versions of your app. If you’re not sure how your confidence values correlate with the quality of your results, it’s not a good idea to convey confidence to people.

**Know what your confidence values mean before you decide how to present them.** For example, people may forgive low-quality results from [critical or complementary](#critical-or-complementary) features — especially when results are accompanied by [attribution](#attribution) or other contextual information — but presenting low-quality results in a prominent way is likely to erode trust in your app.

**In general, translate confidence values into concepts that people already understand.** Simply displaying a confidence value doesn’t necessarily help people understand how it relates to a result. For example, a feature that suggests new music based on a person’s listening habits might calculate that there’s a 97% match between a new song and the songs they usually listen to. However, displaying “97% match” next to the new song as an attribution doesn’t communicate enough information to help people make a choice. In contrast, providing an attribution that clearly identifies the behavior — such as “Because you listen to pop music” — can be more actionable.

**In situations where attributions aren’t helpful, consider ranking or ordering the results in a way that implies confidence levels.** If you must display confidence directly, consider expressing it in terms of semantic categories. For example, a feature that predicts travel prices might replace ranges of confidence numbers with categories like “high chance” and “low chance” to give context to the values and help people understand and compare the results.

**In scenarios where people expect statistical or numerical information, display confidence values that help them interpret the results.** For example, weather predictions, sports statistics, and polling numbers are often accompanied by specific values that express the accuracy of the data as an interval or a percentage.

**Whenever possible, help people make decisions by conveying confidence in terms of actionable suggestions.** Understanding people’s goals is key to expressing confidence in ways that help them make decisions. For example, if your feature predicts when an item will be at its lowest price, you know that people want to optimize how they spend their time and money. For a feature like this, displaying percentages or other numerical confidence values would be less valuable than providing actionable suggestions like “This is a good time to buy,” or “Consider waiting for a better price.”

**Consider changing how you present results based on different confidence thresholds.** If high or low levels of confidence have a meaningful impact on the ways people can experience the results, it’s a good idea to adapt your presentation accordingly. For example, when confidence is high, the face recognition feature in Photos simply displays the photos that contain a specific person, but when confidence is lower, the feature asks people to confirm whether the photos contain the person before showing more.

**When you know that confidence values correspond to result quality, you generally want to avoid showing results when confidence is low.** Especially when a feature is proactive and can make unbidden suggestions, poor results can cause people to be annoyed and even lose trust in the feature. For suggestions and proactive features, it’s a good idea to set a confidence threshold below which you don’t offer results.

## Attribution

An attribution expresses the underlying basis or rationale for a result, without explaining exactly how a model works. Depending on the design of your app, you might want to use attributions to impart transparency and give people insight into your results. For example, if your app suggests books for people to read, you might use an attribution like “Because you’ve read mysteries” when you suggest books in the “thrillers” category.

To help you decide whether to include attributions in your app, consider how you want them to affect people. For example, you might want attributions to:

- Encourage people to change what they do in your app
- Minimize the impact of [mistakes](#mistakes)
- Help people build a mental model of your feature
- Promote trust in your app over time

**Consider using attributions to help people distinguish among results.** For example, if you present a set of results as [multiple options](#multiple-options), including attributions can help people choose an option based on their understanding of the premise that led to it, such as “New books by authors you’ve read.”

**Avoid being too specific or too general.** Overly specific attributions can make people feel like they have to do additional work to interpret the results, whereas overly general attributions typically don’t provide useful information. In apps that make content recommendations, general attributions can make people feel like your app is not treating them as individuals, but overly specific attributions can make people think that your app is watching them too closely. The best attributions strike a balance between these extremes.

**Keep attributions factual and based on objective analysis.** To be useful, an attribution needs to help people reason about a result; you don’t want to provoke an emotional response. Don’t provide an attribution that implies understanding or judgment of people’s emotions, preferences, or beliefs. For example, an app that recommends new content to people can use an attribution like “Because you’ve read nonfiction” instead of an attribution like “Because you love nonfiction.”

**In general, avoid technical or statistical jargon.** In most situations, using percentages, statistics, and other technical jargon doesn’t help people assess the results you provide. The exception to this is when the result itself is of a statistical or technical nature, such as information in the areas of weather, sports, polling and election results, or scientific data.

## Limitations

Every feature — whether it’s based on machine learning or not — has certain limitations to what it can deliver. In general, there are two types of limitations: things a feature can’t do well and things a feature can’t do at all. When there’s a mismatch between people’s expectations about a feature and what the feature can actually accomplish, a limitation can seem like a defect.

An important part of the design process is to identify the scenarios where limitations impact the user experience and design ways to help people work with them. For example:

- Set people’s expectations before they use the feature.
- Show people how to get the best results while they’re using the feature.
- When inferior results occur, explain why so that people can understand the feature better.

**Help people establish realistic expectations.** When a limitation may have a serious effect on user experience but happens rarely, consider making people aware of the limitation before they use your app or feature. You might describe the limitation in marketing materials or within the feature’s context so that people can decide how they want to rely on the feature. If the effects of a limitation aren’t serious, you can help set people’s expectations by providing [attributions](#attribution).

**Demonstrate how to get the best results.** If you don’t provide guidance for using a feature, people may assume it’ll do everything they want. When you proactively show people how to get good results, you help them benefit from the feature and establish a more accurate mental model of the feature’s capabilities. There are many ways to show people the best ways to use a feature, such as:

- Use placeholder text to suggest input. In Photos, the search bar displays the text “Photos, People, Places…” to help people understand what they can search for before they begin typing. Photos also displays a description of how it scans the photo library to offer search suggestions.
- As people interact with the feature, provide feedback on their actions to guide them toward a result without overwhelming them. For example, while people are interacting with Memoji, the feature responds to current conditions and suggests how people can improve their results by adjusting the lighting or moving closer to the camera.
- Suggest alternative ways to accomplish the goal instead of showing no results. To do this successfully, you need to understand the goal well enough to suggest alternatives that make sense.

**Explain how limitations can cause unsatisfactory results.** People can get frustrated when it seems that your feature works intermittently. Ideally, your feature can recognize and describe the reasons for poor results to make people aware of the limitations and help them to adjust their expectations. For example, Memoji tells people that it doesn’t work well in the dark.

**Consider telling people when limitations are resolved.** When people use a feature frequently, they learn to avoid the interactions that fail because of the feature’s limitations. When you update your app to remove a limitation, you might want to notify people so that they can adjust their mental model of your feature and return to interactions they’d previously avoided.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| June 8, 2026 | Made minor updates for clarity. |
| October 24, 2023 | Added art to Corrections section. |
| May 2, 2023 | Consolidated guidance into one page. |

## Related guidelines

- [Generative AI](generative-ai.md)
- [Privacy](privacy.md)

---


<a id="maps"></a>
## maps

# Maps

> Source: <https://developer.apple.com/design/human-interface-guidelines/maps>
> Section: Technologies
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2024-12-18 (Added guidance for place cards and included additional artwork.)

A map displays outdoor or indoor geographical data in your app or on your website.

---

A map uses a familiar interface that supports much of the same functionality as the system-provided Maps app, such as zooming, panning, and rotation. A map can also include annotations and overlays and show routing information, and you can configure it to use a standard graphical view, a satellite image-based view, or a view that’s a hybrid of both.

## Best practices

**In general, make your map interactive.** People expect to be able to zoom, pan, and otherwise interact with maps in familiar ways. Noninteractive elements that obscure the map can interfere with people’s expectations for how maps behave.

**Pick a map emphasis style that suits the needs of your app.** There are two emphasis styles to choose from:

- The *default* style presents a version of the map with fully saturated colors, and is a good option for most standard map applications without a lot of custom elements. This style is also useful for keeping visual alignment between your map and the Maps app, in situations when people might switch between them.
- The *muted* style, by contrast, presents a desaturated version of the map. This style is great if you have a lot of information-rich content that you want to stand out against the map.

For developer guidance, see [MKStandardMapConfiguration.EmphasisStyle](https://developer.apple.com/documentation/mapkit/mkstandardmapconfiguration/emphasisstyle-swift.enum).

**Help people find places in your map.** Consider offering a search feature combined with a way to filter locations by category. The search field for a shopping mall map, for example, might include filters that make it easy to find common store types, like clothing, housewares, electronics, jewelry, and toys.

**Clearly identify elements that people select.** When someone selects a specific area or other element on the map, use distinct styling like an outline and color variation to call attention to the selection.

**Cluster overlapping points of interest to improve map legibility.** A *cluster* uses a single pin to represent multiple points of interest within close proximity. As people zoom in on a map, clusters expand to progressively reveal individual points of interest.

**Help people see the Apple logo and legal link.** It’s fine when parts of your interface temporarily cover the logo and link, but don’t cover these elements all the time. Follow these guidelines to help keep the Apple logo and legal link visible:

- Use adequate padding to separate the logo and link from the map boundaries and your custom controls. For example, it works well to use 7 points of padding on the sides of the elements and 10 points above and below them.
- Avoid causing the logo and link to move with your interface. It’s best when the Apple logo and legal link appear to be fixed to the map.
- If your custom interface can move relative to the map, use the lowest position of the custom element to determine the placement of the logo and link. For example, if your app lets people pull up a custom card from the bottom of the screen, place the Apple logo and legal link 10 points above the lowest resting position of the card.

> **Note:** The Apple logo and legal link aren’t shown on maps that are smaller than 200x100 pixels.

## Custom information

**Use annotations that match the visual style of your app.** Annotations identify custom points of interest on your map. The default annotation marker has a red tint and a white pin icon. You can change the tint to match the color scheme of your app. You can also change the icon to a string or image, like a logo. An icon string can contain any characters, including Unicode characters, but keep it to two to three characters in length for readability. For developer guidance, see [MKAnnotationView](https://developer.apple.com/documentation/mapkit/mkannotationview).

**If you want to display custom information that’s related to standard map features, consider making them independently selectable.** When you support selectable map features, the system treats Apple-provided features (including points of interest, territories, and physical features) independently from other annotations that you add. You can configure custom appearances and information to represent these features when people select them. For developer guidance, see [MKMapFeatureOptions](https://developer.apple.com/documentation/mapkit/mkmapfeatureoptions).

**Use overlays to define map areas with a specific relationship to your content.**

- *Above roads*, the default level, places the overlay above roads but below buildings, trees, and other features. This is great for situations where you want people to have an idea of what’s below the overlay, while still clearly understanding that it’s a defined space.
- *Above labels* places the overlay above both roads and labels, hiding everything beneath it. This is useful for content that you want to be fully abstracted from the features of the map, or when you want to hide areas of the map that aren’t relevant.

For developer guidance, see [Displaying overlays on a map](https://developer.apple.com/documentation/mapkit/displaying-overlays-on-a-map) and [MKOverlayLevel](https://developer.apple.com/documentation/mapkit/mkoverlaylevel).

**Make sure there’s enough contrast between custom controls and the map.** Insufficient contrast makes controls hard to see and can cause them to blend in with the map. Consider using a thin stroke or light drop shadow to help a custom control stand out, or applying blend modes to the map area to increase its contrast with the controls atop it.

## Place cards

Place cards display rich place information in your app or website, such as operating hours, phone numbers, addresses, and more. This enables you to provide structured and up-to-date information for places that you specify, and add depth to search results.

### Displaying place cards in a map

You can present a place card that appears directly in your map anytime someone selects a place. This is a great way to provide place information in a map with multiple places that you specify, like a map of bookstores that an author plans to visit on their book signing tour. For developer guidance, see [mapItemDetailSelectionAccessory(_:)](https://developer.apple.com/documentation/mapkit/mapcontent/mapitemdetailselectionaccessory(_:)), [mapView(_:selectionAccessoryFor:)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:selectionaccessoryfor:)), and [selectionAccessory](https://developer.apple.com/documentation/mapkitjs/annotation/selectionaccessory).

You can also display place cards for other places on a map, such as points of interest, territories, and physical features, to provide valuable context to people about nearby places. For developer guidance, see [mapFeatureSelectionAccessory(_:)](https://developer.apple.com/documentation/swiftui/view/mapfeatureselectionaccessory(_:)), [mapView(_:selectionAccessoryFor:)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:selectionaccessoryfor:)), and [selectableMapFeatureSelectionAccessory](https://developer.apple.com/documentation/mapkitjs/map/selectablemapfeatureselectionaccessory).

> **Developer note:** In websites, you can embed a custom map that displays a place card by default for a single place that you specify. For developer guidance, see [Displaying place information using the Maps Embed API](https://developer.apple.com/documentation/mapkitjs/displaying-place-information-using-the-maps-embed-api).

The system defines several place card styles, which specify the size, appearance, and information included in a place card.

- The *automatic* style lets the system determine the place card style based on the size of your map view.
- The *callout* style displays a place card in a popover style next to the selected place. You can further specify the style of a callout — the *full* callout style displays a large, detailed place card, and the *compact* callout style displays a space-saving, more concise place card. If you don’t specify a callout style, the system defaults to the *automatic* callout style, which determines the callout style based on your map’s view size.
- The *caption* style displays an “Open in Apple Maps” link.
- The *sheet* style displays a place card in a [sheet](sheets.md).

For developer guidance, see [MapItemDetailSelectionAccessoryStyle](https://developer.apple.com/documentation/mapkit/mapitemdetailselectionaccessorystyle), [MKSelectionAccessory.MapItemDetailPresentationStyle](https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle), and [PlaceSelectionAccessoryStyle](https://developer.apple.com/documentation/mapkitjs/placeselectionaccessorystyle).

*Illustrated: Full callout, Compact callout, Caption, Sheet.*

Full callout style place cards appear differently depending on a person’s device. The system presents the full callout style place card in a popover style in iPadOS and macOS, and as a [sheet](sheets.md) in iOS.

**Consider your map presentation when choosing a style.** The full callout style place card offers people the richest experience, presenting them with the most information about a place directly in your map. However, be sure to choose a place card style that fits in the context of your map. For example, if your app displays a small map with many annotations, consider using the compact callout style for a space-saving presentation that shows place information while maintaining the context of the other places that you specify in your map.

**Make sure your place card looks great on different devices and window sizes.** If you choose to specify a style, ensure that the content in your place card remains viewable on different devices and as window sizes change. For full callout style place cards, you can set a minimum width to prevent text from overflowing on smaller devices.

**Avoid duplicating information.** Consider what information you already display in your app or website when you choose a place card style. For example, the full callout style place card might display information that your app already shows. In this case, the compact callout or caption style might be a better complement.

**Keep the location on your map visible when displaying a place card.** This helps people maintain a sense of where the location is on your map while getting detailed place information. You can set an offset distance for your place card and point it to the selected location. For developer guidance, see [offset(_:)](https://developer.apple.com/documentation/swiftui/view/offset(_:)), [accessoryOffset](https://developer.apple.com/documentation/mapkit/mkannotationview/accessoryoffset), and [selectionAccessoryOffset](https://developer.apple.com/documentation/mapkitjs/annotation/selectionaccessoryoffset).

### Adding place cards outside of a map

You can also display place information outside of a map in your app or website. For example, you might want to display a list of places rather than a map, like in search results or a store locator, and present a place card when people select one. For developer guidance, see [mapItemDetailSelectionAccessory(_:)](https://developer.apple.com/documentation/mapkit/mapcontent/mapitemdetailselectionaccessory(_:)), [mapItemDetail(_:)](https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetail(_:)), and [PlaceDetail](https://developer.apple.com/documentation/mapkitjs/placedetail).

> **Important:** If you don’t display a place card directly within a map view, you must include a map in the place card. For developer guidance, see [mapItemDetailSheet(item:displaysMap:)](https://developer.apple.com/documentation/swiftui/view/mapitemdetailsheet(item:displaysmap:)) and [init(mapItem:displaysMap:)](https://developer.apple.com/documentation/mapkit/mkmapitemdetailviewcontroller/init(mapitem:displaysmap:)).

**Use location-related cues in surrounding content to help communicate that people can open a place card.** For example, you can display place names and addresses alongside a button for more details to help indicate that people can interact with it to get place information. For a space-efficient design, you can include a map pin icon with a place name to help communicate that people can open a place card.

## Indoor maps

Apps connected with specific venues like shopping malls and stadiums can design custom interactive maps that help people locate and navigate to indoor points of interest. Indoor maps can include overlays that highlight specific areas, such as rooms, kiosks, and other locations. They can also include text labels, icons, and routes.

*Illustrated: Example 1, Example 2, Example 3.*

**Adjust map detail based on the zoom level.** Too much detail can cause a map to appear cluttered. Show large areas like rooms and buildings at all zoom levels. Then, progressively add more detailed features and labels as the map is zoomed in. An airport map might show only terminals and gates when zoomed out, but reveal individual stores and restrooms when zoomed in.

**Use distinctive styling to differentiate the features of your map.** Using color along with icons can help distinguish different types of areas, stores, and services, and make it easy for people to quickly find what they’re looking for.

**Offer a floor picker if your venue includes multiple levels.** A floor picker lets people quickly jump between floors. If you implement this feature, keep floor numbers concise for simplicity. In most cases, a list of floor numbers — rather than floor names — is sufficient.

**Include surrounding areas to provide context.** Adjacent streets, playgrounds, and other nearby locations can all help orient people when they use your map. If these areas are noninteractive, use dimming and a distinct color to make them appear supplemental.

**Consider supporting navigation between your venue and nearby transit points.** Make it easy to enter and exit your venue by offering routing to and from nearby bus stops, train stations, parking lots, garages, and other transit locations. You might also offer a way for people to quickly switch over to Apple Maps for additional navigation options.

**Limit scrolling outside of your venue.** This can help people avoid getting lost when they swipe too hard on your map. When possible, keep at least part of your indoor map visible onscreen at all times. To help people stay oriented, you may need to adjust the amount of scrolling you permit based on the zoom level.

**Design an indoor map that feels like a natural extension of your app.** Don’t try to replicate the appearance of Apple Maps. Instead, make sure area overlays, icons, and text match the visual style of your app. For guidance, see [Indoor Mapping Data Format](https://register.apple.com/resources/imdf/).

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.*

## Change log

| Date | Changes |
| --- | --- |
| December 18, 2024 | Added guidance for place cards and included additional artwork. |
| September 12, 2023 | Added artwork. |
| September 23, 2022 | Added guidelines for presenting custom information, refined best practices, and consolidated guidance into one page. |

---


<a id="nfc"></a>
## nfc

# NFC

> Source: <https://developer.apple.com/design/human-interface-guidelines/nfc>
> Section: Technologies
> Platforms covered: iOS, iPadOS

Near-field communication (NFC) allows devices within a few centimeters of each other to exchange information wirelessly.

---

iOS apps running on supported devices can use NFC scanning to read data from electronic tags attached to real-world objects. For example, a person can scan a toy to connect it with a video game, a shopper can scan an in-store sign to access coupons, or a retail employee can scan products to track inventory.

## In-app tag reading

An app can support single- or multiple-object scanning when the app is active, and display a scanning sheet whenever people are about to scan something.

**Don’t encourage people to make contact with physical objects.** To scan a tag, an iOS device must simply be within close proximity of the tag. It doesn’t need to actually touch the tag. Use terms like *scan* and *hold near* instead of *tap* and *touch* when asking people to scan objects.

**Use approachable terminology.** Near-field communication may be unfamiliar to some people. To make it approachable, avoid referring to technical, developer-oriented terms like *NFC*, *Core NFC*, *Near-field communication*, and *tag*. Instead, use friendly, conversational terms that most people will understand.

| Use | Don’t use |
| --- | --- |
| Scan the [*object name*]. | Scan the NFC tag. |
| Hold your iPhone near the [*object name*] to learn more about it. | To use NFC scanning, tap your phone to the [*object*]. |

**Provide succinct instructional text for the scanning sheet.** Provide a complete sentence, in sentence case, with ending punctuation. Identify the object to scan, and revise the text appropriately for subsequent scans. Keep the text short to avoid truncation.

| First scan | Subsequent scans |
| --- | --- |
| Hold your iPhone near the [*object name*] to learn more about it. | Now hold your iPhone near another [*object name*]. |

## Background tag reading

Background tag reading lets people scan tags quickly any time, without needing to first open your app and initiate scanning. On devices that support background tag reading, the system automatically looks for nearby compatible tags whenever the screen is illuminated. After detecting and matching a tag with an app, the system shows a notification that the people can tap to send the tag data to the app for processing. Note that background reading isn’t available when an NFC scanning sheet is visible, Wallet or Apple Pay are in use, cameras are in use, the device is in Airplane Mode, and the device is locked after a restart.

**Support both background and in-app tag reading.** Your app must still provide an in-app way to scan tags, for people with devices that don’t support background tag reading.

## Platform considerations

*No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.*

---


<a id="sign-in-with-apple"></a>
## sign-in-with-apple

# Sign in with Apple

> Source: <https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple>
> Section: Technologies
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)

Sign in with Apple provides a fast, private way to sign into apps and websites, giving people a consistent experience they can trust and the convenience of not having to remember multiple accounts and passwords.

---

Supporting Sign in with Apple lets people use the Apple Account they already have to sign in or sign up, and skip filling out forms, verifying email addresses, and choosing passwords. In cases where you choose to ask for a name and email address, people have the option to share a unique, random email address that automatically relays messages to their personal email address. For developer guidance, see [Authentication Services](https://developer.apple.com/documentation/authenticationservices).

You can offer Sign in with Apple in every version of your app or website across all platforms — including non-Apple platforms.

Sign in with Apple makes it easy for people to authenticate with Face ID, Touch ID, or Optic ID and has two-factor authentication built in for an added layer of security. Apple doesn’t use Sign in with Apple to profile people or their activity in apps.

## Offering Sign in with Apple

Follow these guidelines to offer Sign in with Apple when it’s most convenient for people.

**Ask people to sign in only in exchange for value.** People need to understand why you’re asking them to sign in, so it can work well to display a brief, approachable description of sign-in benefits. For example, you might want to tell people that signing in lets them personalize the app experience, access additional features, or synchronize data.

**Delay sign-in as long as possible.** People often abandon apps when they’re forced to sign in before doing anything useful. Give them a chance to familiarize themselves with your app before making a commitment. For example, a live-streaming app could let people explore available content before signing in to stream something.

**If you require an account, ask people to set it up before offering any sign-in options.** Start by explaining the reasons for requiring an account. Then, after people complete account setup, let them choose a convenient way to sign in to their new account by offering Sign in with Apple and any other sign-in methods you support.

**Consider letting people link an existing account to Sign in with Apple.** When you support this type of linking, people can get the convenience of using Sign in with Apple while maintaining access to the information in an account they’ve already set up. You can offer account linking before or after people sign in to their existing account. For example:

- If people share an email address through Sign in with Apple and it matches the address in an existing account, you can suggest that they link Sign in with Apple to that account.
- If people used an existing user name and password to sign in, you can display an account-linking suggestion in their account’s settings view or another logical place.

**In a commerce app, wait until after people make a purchase before asking them to create an account.** If you support a guest checkout system, give people a quick way to create an account after the transaction completes. For example, if you support Apple Pay, let people create an account on the order confirmation page. In cases where people have already provided their name and email address during the Apple Pay transaction, you don’t need to ask for this information.

**As soon as Sign in with Apple completes, welcome people to their new account.** Help people use their new account right away; don’t delay the experience by asking for information that isn’t required.

**Indicate when people are currently signed in.** You can help people confirm their sign-in method by displaying a phrase like “Using Sign in with Apple” in places like a settings or account interface.

## Collecting data

People appreciate Sign in with Apple for its privacy and convenience. Although some apps or websites may require additional information — such as a date of birth or a region of residence — it’s essential to minimize your requests for data as people set up an account. Build on the trust that people have in Sign in with Apple by describing why you need additional data and clearly displaying the data you receive.

**Clarify whether the additional data you request is required or just recommended.** If the data is legally or contractually required — such as an agreement to terms of service, country or region of residence, birth date, or information required by a region’s real-identity laws — make sure people understand that they must supply the additional information to complete the setup of their account. If additional data isn’t required but can improve the user experience, make sure people know the request is optional and help them understand the benefits of providing the information.

**Don’t ask people to supply a password.** A key benefit of Sign in with Apple is that people don’t have to create and memorize additional passwords. Unless people have stopped using Sign in with Apple with your app or website, don’t ask for a password.

**Avoid asking for a personal email address when people supply a private relay address.** Using Sign in with Apple, people can choose to share a private relay address that automatically forwards messages to their verified personal email account. It’s essential to respect this choice and avoid overriding it by asking for a personal email address. If you present customer service, retail, or other experiences that request identification via email address, you can:

- Make sure that people can view their private relay address in your app or website
- Direct people to Settings > Apple Account > Password & Security > Apps using Apple Account to retrieve their private relay address
- Use other identifying values, like an order number or phone number collected as part of a purchase

**Give people a chance to engage with your app before asking for optional data.** As people use your app, you can help them discover places where they can benefit from sharing more information with you. For example, you might suggest that they provide a contact phone number if they want real-time text updates, or social network information if they want to play games with friends. If people choose not to provide optional information, don’t prevent them from accessing their account or using all the features of your app.

**Be transparent about the data you collect.** People value knowing how you use the data that they share with you. One way you can be transparent is to welcome people by using the name or email address they shared. Doing this helps establish how you use this information and, for a relay address, shows people where to find it in the future. If you don’t display all the data that people provide, they are likely to wonder why you asked for it.

## Displaying buttons

Apple provides several Sign in with Apple buttons you can use to let people set up an account and sign in. If necessary, you can create a custom button to offer Sign in with Apple; for guidelines, see [Creating a custom Sign in with Apple button](#creating-a-custom-sign-in-with-apple-button).

**Prominently display a Sign in with Apple button.** Make a Sign in with Apple button no smaller than other sign-in buttons, and avoid making people scroll to see the button.

### Using the system-provided buttons

When you use the system-provided APIs to create a Sign in with Apple button, you get the following advantages.

- A button that’s guaranteed to use an Apple-approved appearance
- Assurance that the button’s contents maintain ideal proportions as you change its style
- Automatic translation of the button’s title into the language specified by the device
- Support for configuring the button’s corner radius to match the style of your UI (iOS, macOS, and web)
- A system-provided alternative text label that lets VoiceOver describe the button

For developer guidance, see [ASAuthorizationAppleIDButton](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidbutton) (iOS, macOS, and tvOS), [WKInterfaceAuthorizationAppleIDButton](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton) (watchOS), and [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web). You can also visit [Sign in with Apple button](https://appleid.apple.com/signinwithapple/button) to view and adjust live previews of web-based buttons and get the code.

The system provides several variants of the button title. Depending on the platform on which your content runs, choose the variant that fits the terminology of your sign-in experience and use it consistently throughout your interfaces.

The following button titles are available for iOS, macOS, tvOS, and the web:

For watchOS, the system provides one title:  Sign in.

Depending on the platform, the system provides up to three options for the appearance of the Sign in with Apple button: white, white with an outline, and black. Choose the appearance that works best with the background on which the button displays.

#### White

The white style is available on all platforms and the web. Use this style on dark backgrounds that provide sufficient contrast.

#### White with outline

The white outlined style is available in iOS, macOS, and the web. Use this style on white or light-color backgrounds that don’t provide sufficient contrast with the white button fill. Avoid using this style on a dark or saturated background, because the black outline can add visual clutter; instead, use the [white](#white) style to contrast with a dark background.

#### Black

The black style is available on all platforms and the web. Use this style on white or light-color backgrounds that provide sufficient contrast; don’t use it on black or dark backgrounds.

Unlike the black Sign in with Apple button for other platforms, the watchOS button uses a fill color that’s not fully black. To contrast with the pure black background of Apple Watch, the watchOS button uses the system-defined dark gray appearance.

#### Button size and corner radius

**Adjust the corner radius to match the appearance of other buttons in your app.** By default, the Sign in with Apple button has rounded corners. In iOS, macOS, and the web, you can change the corner radius to produce a button with square corners or a capsule-shape button. For developer guidance, see [cornerRadius](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidbutton/cornerradius) (iOS and macOS) and [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web).

**Maintain the minimum button size and margin around the button in iOS, macOS, and the web.** Be mindful that the button title may vary in length depending on the locale. Use the following values for guidance.

| Minimum width | Minimum height | Minimum margin |
| --- | --- | --- |
| 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |

### Creating a custom Sign in with Apple button

If your interface requires it, you can create a custom Sign in with Apple button for iOS, macOS, or the web. For example, you may want to align logos across multiple sign-in buttons, use buttons that display only a logo, or adjust the button’s font, bezel, or background appearance to coordinate with your UI.

Always make sure that people can instantly identify your custom button as a Sign in with Apple button. If your custom button differs too much from the standard one, people may not feel comfortable using it to set up an account or sign in. App Review evaluates all custom Sign in with Apple buttons.

[Apple Design Resources](https://developer.apple.com/design/resources/) provides downloadable Apple logo artwork you can use to create custom Sign in with Apple buttons that display either a logo only or a logo and text. The logo files are available in PNG, SVG, and PDF formats, and the artwork for both types of buttons includes both black and white versions. Here are examples of the black and white logo-only art files, each with a background added for visibility.

All downloadable logo files include padding that simplifies positioning the logo in a button. Logo-only logo files include horizontal and vertical padding that ensures the correct proportion of the logo relative to the button. In addition to padding that keeps the logo and button correctly proportioned, logo files for buttons with text also include horizontal padding that provides a minimum margin between the logo and the button’s leading edge and title.

Use only the logo artwork downloaded from [Apple Design Resources](https://developer.apple.com/design/resources/); never create a custom Apple logo. As you create a custom Sign in with Apple button, follow these guidelines for using the downloadable logo file:

- Use the logo file to position the Apple logo in a button; never use the Apple logo as a button.
- Match the height of the logo file to the height of the button.
- Don’t crop the logo file.
- Don’t add vertical padding.

To make sure that your custom button is visually consistent with the system-provided Sign in with Apple button, don’t change the following attributes.

- Titles. Use only *Sign in with Apple*, *Sign up with Apple*, or *Continue with Apple*.
- General shape. Buttons that combine the logo with text are always rectangular; logo-only buttons can be circular or rectangular.
- Logo and title colors. Within a button, both items must be either black or white; don’t use custom colors.

To coordinate with your app design, you can change:

- Title font. You can also adjust the font’s weight and size.
- Title case. You can capitalize every letter in the title.
- Background appearance. The overall color needs to remain black or white. If necessary, you can include a subtle texture or gradient to help the button harmonize with your interface.
- Button corner radius. You can use a corner radius value that matches the other buttons in your UI.
- Button bezel and shadow. For example, you can use a stroke to emphasize the button bezel or add a drop shadow.

#### Custom buttons with a logo and text

**Choose the format of the logo file based on the height of your button.** Because SVG and PDF are vector-based formats, you can use these files in buttons of any height. Use the PNG files only in buttons that are 44 points tall, which is the default (and recommended) button height in iOS. Logos are available in small, medium, and large sizes, so you can match logo sizes in all the sign-up buttons you display.

**Prefer the system font for the title — that is, Sign in with Apple, Sign up with Apple, or Continue with Apple.** Regardless of the font you choose, the title and button height of your custom button need to use the same proportions that the system uses. Using the system font for example, the title’s font size would be 43% of the button’s height — in other words, the button’s height would be 233% of the title’s font size, rounded to the nearest integer. Here are two examples that show these proportions using different sizes of the system font.

**In general, preserve the capitalization style of the title.** By default, all variants of the button title capitalize the first word — that is, *Sign* or *Continue* — and *Apple*; all other letters are lowercase. Avoid changing this style unless your interface uses only uppercase.

**Keep the title and logo vertically aligned within the button.** To do this, vertically align the title to the middle of the button, then add the logo image, making sure its height matches the height of the button. Because the logo image includes top and bottom padding, vertically aligning the title in the button ensures that the title, the logo, and the button stay properly aligned.

**Inset the logo if necessary.** If you need to horizontally align the Apple logo with other authentication logos, you can adjust the space between the logo and the button’s leading edge.

**Maintain a minimum margin between the title and the right edge of the button.** Ensure the margin measures at least 8% of the button’s width.

**Maintain the minimum button size and margin around the button.** Be mindful that the button title may vary in length depending on the locale. Use the following values for guidance.

| Minimum width | Minimum height | Minimum margin |
| --- | --- | --- |
| 140 pt (140 px @1x, 280 px @2x) | 30 pt (30 px @1x, 60 px @2x) | 1/10 of the button’s height |

#### Custom logo-only buttons

**Choose the format of the logo file based on the size of your button.** The downloadable artwork for logo-only buttons is available in SVG, PDF, and PNG formats. Use the vector-based SVG and PDF formats for buttons of any size; use the PNG format only in buttons that measure 44x44 pt.

**Don’t add horizontal padding to a logo-only image.** A logo-only Sign in with Apple button always has a 1:1 aspect ratio, and the artwork already includes the correct padding on all sides.

**Use a mask to change the default square shape of the logo-only image.** For example, you might want to use a circular or rounded rectangular shape to present all logo-only sign-in buttons. Never crop the Apple-provided artwork to decrease its built-in padding or use the logo by itself, and avoid including additional padding.

**Maintain a minimum margin around the button.** Ensure the margin measures at least 1/10 of the button’s height.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| September 14, 2022 | Refined guidance on supporting existing accounts, helping people set up a new account, and indicating the current sign-in status. Consolidated guidance into one page. |

---


<a id="siri"></a>
## siri

# Siri

> Source: <https://developer.apple.com/design/human-interface-guidelines/siri>
> Section: Technologies
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2026-06-08 (Revised for Siri AI.)

People use Siri to help them with the things they need to find, know, or do every day.

---

Siri is a personal assistant that helps people get information and perform quick actions throughout the system and the apps they use. People interact with Siri in a variety of ways, like using their voice, swiping down from the Dynamic Island, or in the Siri app.

On supported devices, Siri AI introduces a version of Siri powered by Apple Intelligence. When an app integrates its content and features with Apple Intelligence, people can use the natural language awareness and contextual understanding of Siri to initiate the app’s actions from anywhere in the system, interact with content on screen, and quickly reach features that would otherwise require navigating deep into the app.

For example, someone can say “Send a message to Marisa in *AppName*” from anywhere in the system, and Siri can help them complete that task in a contextually appropriate way. With a photo visible on screen, someone can say “Add this photo to my Landscapes album,” then follow up with “And email it to Josh,” which opens an email compose view and adds Josh as the recipient. Saying “Make this black and white” to convert an image to grayscale can also be faster than navigating through menus to find the same command.

## Getting your app to work with Siri

By default, the system doesn’t have specific awareness of what an app can do or the information it contains. In order for an app to work with Siri, the app has to make its features and content available to Apple Intelligence using the [App Intents](https://developer.apple.com/documentation/appintents) framework.

When an app implements intents, the system can expose the things the app can do (the app’s actions, or *intents*) and its content (the app’s *entities*) in system experiences where it makes sense. This makes the app’s actions and content available to features that build on Apple Intelligence, such as Siri, Spotlight, and the Shortcuts app. For developer guidance, see [Getting started with the App Intents framework](https://developer.apple.com/documentation/appintents/getting-started-with-the-app-intents-framework).

To get the most out of Siri, an app can additionally associate its features and content with app *[schemas](https://developer.apple.com/documentation/appintents/app-schema-domains)*: preset templates for functionality that the system already understands. Apps in common domain areas like email, music, or photos can use the system’s existing knowledge to access built-in logic for handling requests through a wider range of options with natural conversation and deeper contextual understanding. For developer guidance, see [Apple Intelligence and Siri AI](https://developer.apple.com/documentation/appintents/apple-intelligence-and-siri-ai) and [Making actions and content discoverable by Apple Intelligence](https://developer.apple.com/documentation/appintents/making-actions-and-content-discoverable-by-apple-intelligence).

### Sharing contextual information

In addition to exposing actions and content with schemas, an app can offer a more personalized experience by giving the system contextual information about its content and features.

An app can tell the system what’s onscreen by annotating its views and other content with app entities. This gives the system information Siri needs to improve contextual interaction based on what someone is interacting with. For example, when someone refers to parts of your app’s content (like buttons or onscreen graphics) during a Siri conversation, Siri can use the annotations your app provides to understand what the person means. For developer guidance, see [Providing contextual cues to Apple Intelligence and Siri](https://developer.apple.com/documentation/appintents/providing-contextual-cues-to-apple-intelligence-and-siri).

To provide content information to the system, an app can donate entities to the on-device Spotlight index, which makes the app’s information available to someone searching in Spotlight or with Siri. For developer guidance, see [Defining app entities for your custom data types](https://developer.apple.com/documentation/appintents/defining-app-entities-for-your-custom-data-types) and [Making app entities available in Spotlight](https://developer.apple.com/documentation/appintents/making-app-entities-available-in-spotlight).

An app can also tell the system about actions a person takes while using it by donating the actions as intents. This helps Siri anticipate future actions a person might want to take, and surface them through various system experiences at appropriate times. Examples of actions an app can donate include things like a person’s recent activity or items that a person has indicated an interest in. For developer guidance, see [Donating your app’s data and actions to the system](https://developer.apple.com/documentation/appintents/donating-your-apps-data-and-actions-to-the-system).

## Best practices

**Identify your app’s most popular actions, and when and where they occur.** Understanding the contexts where those actions are relevant, such as in a hands-free environment or on a particular device, can help you prioritize which actions and content to expose as app intents and entities, and inform how you design a great Siri experience.

**Use familiar terms for your content and actions.** When you create an app intent or entity, you choose the terminology that represents it. For example, you could refer to an audio file as a track, a song, or a podcast. Using language for your features and content that people are most likely to recognize makes interacting with your app through Siri more natural and intuitive.

**Offer relevant content.** Instead of telling Spotlight about all of your app’s content, consider things that are particularly relevant to someone’s personal context — things they’ve recently searched for, their favorite items or bookmarks, or the content of a wishlist. Some app categories, like email or messaging, might have a good reason to consider their entire catalog as relevant information; it can be appropriate to provide expanded access in those cases.

**Don’t advertise.** Don’t include advertisements, marketing, or in-app purchase sales pitches in content that Siri delivers.

**Only provide a custom response if built-in responses don’t meet your app’s needs.** Siri is designed to anticipate a wide variety of natural language requests and respond helpfully without additional configuration.

## Customizing your app’s experience with Siri

For apps with many common feature sets, existing [app schema domains](https://developer.apple.com/documentation/appintents/app-schema-domains) provide the built-in functionality that they need to expose their actions and content to Apple Intelligence and Siri without any additional work. If your app’s functionality falls outside of these areas, *App Shortcuts* offer a way to expose custom actions to the system for Siri to access. For design guidance, see [App Shortcuts](app-shortcuts.md). For developer guidance, see [App Shortcuts](https://developer.apple.com/documentation/appintents/app-shortcuts).

To customize the experience of an action or a piece of content associated with an existing schema, an app can define additional optional properties as part of an intent or entity that can contextually enhance the response that Siri provides. An app could present a playback control [snippet](snippets.md) that Siri can display as an audio file plays, for example. For developer guidance, see [Displaying static and interactive snippets](https://developer.apple.com/documentation/appintents/displaying-static-and-interactive-snippets).

> **Note:** Siri is powered by Apple Intelligence to provide contextually relevant responses. Because responses can appear in a wide variety of contexts, some of which aren’t visual, optional intent or entity properties that an app defines may not always appear as part of a response.

When you provide additional custom properties as part of your schema responses, consider the following guidelines.

**Write response dialogue that’s clear and descriptive.** An effective response clearly conveys what happens when Siri performs the action. If you ask follow-up questions, be sure to customize the default dialogue for clarity. For example, “Which soup?” is clearer than “Which one?”

**Keep responses as succinct as possible.** People might interact with Siri frequently, so they may hear the same response multiple times when answering follow-up questions or dealing with errors. Use the context of the current conversation to remove as many details as possible. Avoid including unnecessary words or attempts at humor, because both can become irritating over time.

**Provide responses that Siri can deliver audibly and visually.** This lets Siri decide which communication method works best for the current situation. For example, if someone using iPhone asks for the weather, the forecast appears onscreen; if they’re using AirPods, Siri speaks the forecast instead. Make sure the voice response can stand alone and that it doesn’t depend on visual elements to fill in essential information.

**Design inclusive interactions.** Create welcoming interactions for everyone by avoiding specific pronouns when they’re not necessary. For example, in response to “Send a message to my best friend,” instead of saying “What’s his or her name?” say “Who should I send it to?” or “To who?” For guidance, see [Writing](writing.md) and [Inclusion](inclusion.md).

**Ask an open-ended question when the full list of options is too long.** If the full list of options is too long for Siri to read in a timely way, follow up with an open-ended question to narrow the scope or get additional detail. For example, “What kind of shoes are you interested in?” in response to a request for the available shoes in a shopping app.

**Keep responses device-independent whenever possible.** People can initiate a Siri request on one device and have it take effect on another, so device-specific wording can easily become confusing or misleading. If you must reference a specific device in a response, make sure it’s accurate and makes sense in context.

**Omit your app name from responses.** The system already provides verbal and visual attribution for your app when responding to people.

**Use appropriate language and respect parental controls.** Don’t include offensive language in dialogue text that you provide. Many families use parental controls to restrict explicit content and other material that’s based on specific rating levels. Be aware that Siri may also respond aloud, and others nearby might hear the response.

**Help people understand errors and failures.** The system provides some default error descriptions, but it’s best to enhance error responses so that they’re specific to the current situation. For example, if the chicken noodle soup is sold out, an error like “Sorry, we’re out of chicken noodle soup” is much clearer than “Sorry, we can’t complete your order.”

## Editorial guidelines

**Refer to Siri by name.** Don’t reference Siri using pronouns like *she*, *him*, or *her*. Ideally, just use the word *Siri*. For example, “After you add a shortcut to Siri, you can run the shortcut anytime by asking Siri.” For additional guidance, see [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html).

**Be aware that the system reserves important actions and phrases for Siri.** Never impersonate Siri, attempt to reproduce the functionality that Siri provides, or provide a response that appears to come from Apple. Don’t use reserved phrases like “Call 911” or “Hey Siri.”

**In a localized context, translate only the word *Hey* in the phrase “Hey Siri.”** As an Apple trademark, *Siri* is never translated. Here is a list of acceptable translations for the phrase “Hey Siri”:

| Locale code | “Hey Siri” translation | Locale code | “Hey Siri” translation |
| --- | --- | --- | --- |
| ar_AE | يا Siri | fr_CA | Dis Siri |
| ar_SA | يا Siri | fr_CH | Dis Siri |
| da_DK | Hej Siri | fr_FR | Dis Siri |
| de_AT | Hey Siri | it_CH | Ehi Siri |
| de_CH | Hey Siri | it_IT | Ehi Siri |
| de_DE | Hey Siri | ja_JP | Hey Siri |
| en_AU | Hey Siri | ko_KR | Siri야 |
| en_CA | Hey Siri | ms_MY | Hai Siri |
| en_GB | Hey Siri | nb_NO | Hei Siri |
| en_IE | Hey Siri | nl_BE | Hé, Siri |
| en_IN | Hey Siri | nl_NL | Hé Siri |
| en_NZ | Hey Siri | no_NO | Hei Siri |
| en_SG | Hey Siri | pt_BR | E aí Siri |
| en_US | Hey Siri | ru_RU | привет Siri |
| en_ZA | Hey Siri | sv_SE | Hej Siri |
| es_CL | Oye Siri | th_TH | หวัดดี Siri |
| es_ES | Oye Siri | tr_TR | Hey Siri |
| es_MX | Oye Siri | zh_CN | 嘿Siri |
| es_US | Oye Siri | zh_HK | 喂 Siri |
| fi_FI | Hei Siri | zh_TW | 嘿 Siri |
| fr_BE | Dis Siri |  |  |

## Change log

| Date | Changes |
| --- | --- |
| June 8, 2026 | Revised for Siri AI. |
| June 5, 2023 | Removed Add to Siri guidance. Added references to the new [App Shortcuts](app-shortcuts.md) page. |
| May 2, 2023 | Consolidated guidance into one page. |

## Related guidelines

- [App Shortcuts](app-shortcuts.md)
- [Snippets](snippets.md)

---


<a id="voiceover"></a>
## voiceover

# VoiceOver

> Source: <https://developer.apple.com/design/human-interface-guidelines/voiceover>
> Section: Technologies
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-03-07 (New page.)

VoiceOver is a screen reader that lets people experience your app’s interface without needing to see the screen.

---

By supporting VoiceOver, you help people who are blind or have low vision access information in your app and navigate its interface and content when they can’t see the display.

VoiceOver is supported in apps and games built for Apple platforms. It’s also supported in apps and games developed in Unity using [Apple’s Unity plug-ins](https://github.com/apple/unityplugins). For related guidance, see [Accessibility](accessibility.md).

## Descriptions

You inform VoiceOver about your app’s content by providing alternative text that explains your app’s interface and the content it displays.

**Provide alternative labels for all key interface elements.** VoiceOver uses alternative labels (which aren’t visible onscreen) to audibly describe your app’s interface. System-provided controls have generic labels by default, but you should provide more descriptive labels that convey your app’s functionality. Add labels to any custom elements your app defines. Be sure to keep your descriptions up-to-date as your app’s interface and content change. For developer guidance, see [Accessibility modifiers](https://developer.apple.com/documentation/swiftui/view-accessibility).

**Describe meaningful images.** If you don’t describe key images in your app’s content, people can’t use VoiceOver to fully experience them within your app. Because VoiceOver helps people understand the interface surrounding images too, such as nearby captions, describe only the information the image itself conveys.

**Make charts and other infographics fully accessible.** Provide a concise description of each infographic that explains what it conveys. If people can interact with the infographic to get more or different information, make these interactions available to people using VoiceOver, too. The accessibility APIs offer ways to represent custom interactive elements so that assistive technologies can help people use them. For guidance, see [Charts](charts.md).

**Exclude purely decorative images from VoiceOver.** It’s unnecessary to describe images that are decorative and don’t convey useful or actionable information. Excluding these images shows respect for people’s time and reduces cognitive load when they use VoiceOver. For developer guidance, see [accessibilityHidden(_:)](https://developer.apple.com/documentation/swiftui/view/accessibilityhidden(_:)), [accessibilityElement](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilityelement), and [isAccessibilityElement](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/isaccessibilityelement).

## Navigation

**Use titles and headings to help people navigate your information hierarchy.** The title is the first information someone receives from an assistive technology when arriving on a page or screen in your app. Offer unique titles that succinctly describe each page’s content and purpose. Likewise, use accurate section headings that help people build a mental model of each page’s information hierarchy.

**Specify how elements are grouped, ordered, or linked.** Proximity, alignment, and other visible contextual cues help sighted people perceive the relationships between elements. Examine your app for places where relationships among elements are visual only. Then, describe these relationships to VoiceOver.

VoiceOver reads elements in the same order people read content in the their active language and locale. For example, in US English, this is top-to-bottom, left-to-right. In the ungrouped example below, VoiceOver describes each image before moving on to the captions. In the grouped example, VoiceOver describes each image with its respective caption.

For developer guidance, see [shouldGroupAccessibilityChildren](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/shouldgroupaccessibilitychildren).

**Inform VoiceOver when visible content or layout changes occur.** People may find an unexpected content or layout change confusing because it means their mental map of the content is no longer accurate. It’s crucial to report visible changes so VoiceOver and other assistive technologies can help people update their understanding of the content. For developer guidance, see [AccessibilityNotification](https://developer.apple.com/documentation/accessibility/accessibilitynotification).

**Support the VoiceOver rotor when possible.** People can use an interface element called the VoiceOver rotor to navigate a document or webpage by headings, links, and other content types. You can help people navigate content in your app by identifying these elements to the rotor. The rotor can also bring up the braille keyboard. For developer guidance, see [AccessibilityRotorEntry](https://developer.apple.com/documentation/swiftui/accessibilityrotorentry) (SwiftUI), [UIAccessibilityCustomRotor](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor) (UIKit), and [NSAccessibilityCustomRotor](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor) (AppKit).

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| March 7, 2025 | New page. |

## Related guidelines

- [Accessibility](accessibility.md)
- [Inclusion](inclusion.md)

---
