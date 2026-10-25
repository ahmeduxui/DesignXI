# Apple HIG — Components › System experiences
Bundled HIG pages for the “Components › System experiences” group. Each page kept verbatim under an anchor heading `## <slug>`. Cite as **components-system-experiences.md › <slug> › heading**.


<a id="app-shortcuts"></a>
## app-shortcuts

# App Shortcuts

> Source: <https://developer.apple.com/design/human-interface-guidelines/app-shortcuts>
> Section: Components › System experiences
> Platforms covered: iOS, iPadOS (guidance specific to visionOS, watchOS omitted)
> Last change on Apple's site: 2026-06-08 (Added guidance for adopting app schemas.)

An App Shortcut gives people access to your app’s key functions or content throughout the system.

---

People can initiate App Shortcuts using features like Siri, Spotlight, and the Shortcuts app; using hardware features like the Action button on iPhone or Apple Watch; or by [squeezing](apple-pencil-and-scribble.md#squeeze) Apple Pencil.

Because App Shortcuts are part of your app, they are available immediately when installation finishes. For example, a journaling app could offer an App Shortcut for making a new journal entry that’s available before a person opens the app for the first time. Once someone starts using your app, its App Shortcuts can reflect their choices, like those from FaceTime for calling recent contacts.

App Shortcuts use [App Intents](https://developer.apple.com/documentation/appintents) to define actions within your app to make available to the system. Each App Shortcut includes one or more actions that represent a set of steps people might want to perform to accomplish a task. For example, a home security app might combine the two common actions of turning off the lights and locking exterior doors when a person goes to sleep at night into a single App Shortcut. Each app can include up to 10 App Shortcuts.

For developer guidance, see [App Shortcuts](https://developer.apple.com/documentation/appintents/app-shortcuts).

> **Note:** When you use App Intents to make your app’s actions available to the system, in addition to the App Shortcuts that your app provides, people can also make their own custom shortcuts by combining actions in the Shortcuts app. Custom shortcuts give people flexibility to configure the behavior of actions, and enable workflows that perform tasks across multiple apps. For additional guidance, see the [Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios).

## Best practices

**To surface common types of app functionality throughout the system, consider adopting app schemas instead.** Apps in common domain areas can adopt [app schemas](https://developer.apple.com/documentation/appintents/app-schema-domains) to make their actions and content available to Apple Intelligence. On supported devices, this lets Siri and other system experiences surface app features contextually without the need to adopt individual App Shortcuts. For guidance, see [Siri](siri.md). For developer guidance, see [Apple Intelligence and Siri AI](https://developer.apple.com/documentation/appintents/apple-intelligence-and-siri-ai) and [Making actions and content discoverable by Apple Intelligence](https://developer.apple.com/documentation/appintents/making-actions-and-content-discoverable-by-apple-intelligence).

App Shortcuts are useful for exposing unique features or custom content to the system in areas not covered by app schemas.

**Offer App Shortcuts for your app’s most common and important tasks.** Straightforward tasks that people can complete without leaving their current context work best, but you can also open your app if it helps people complete multistep tasks more easily.

**Add flexibility by letting people choose from a set of options.** An App Shortcut can include a single optional value, or parameter, if it makes sense. For example, a meditation app could offer an App Shortcut that lets someone begin a specific type of meditation: “Start [morning, daily, sleep] meditation.” Include predictable and familiar values as options, because people won’t have the list in front of them for reference. For developer guidance, see [Adding parameters to an app intent](https://developer.apple.com/documentation/appintents/adding-parameters-to-an-app-intent).

**Ask for clarification in response to a request that’s missing optional information.** For example, someone might say “Start meditation” without specifying the type (morning, daily, or sleep); you could follow up by suggesting the one they used most recently, or one based on the current time of day. If one option is most likely, consider presenting it as the default, and provide a short list of alternatives to choose from if a person doesn’t want the default choice.

**Keep voice interactions simple.** If your phrase feels too complicated when you say it aloud, it’s probably too difficult to remember or say correctly. For example, “Start [sleep] meditation with nature sounds” appears to have two possible parameters: the meditation type, and the accompanying sound. If additional information is absolutely required, ask for it in a subsequent step. For additional guidance on writing dialogue text for voice interactions, see [Siri](siri.md).

**Make App Shortcuts discoverable in your app.** People are most likely to remember and use App Shortcuts for tasks they do often, once they know the shortcut is available. Consider showing occasional tips in your app when people perform common actions to let them know an App Shortcut exists. For developer guidance, see [SiriTipUIView](https://developer.apple.com/documentation/appintents/siritipuiview).

### Responding to App Shortcuts

As a person engages with an App Shortcut, your app can respond in a variety of ways, including with dialogue that Siri speaks aloud and custom visuals like snippets and Live Activities.

- [Snippets](snippets.md) are great for custom views that display static information or dialog options, like showing the weather at a person’s location or confirming an order. For developer guidance, see [Displaying static and interactive snippets](https://developer.apple.com/documentation/appintents/displaying-static-and-interactive-snippets).
- [Live Activities](live-activities.md) offer continuous access to information that’s likely to remain relevant and change over a period of time, and are great for timers and countdowns that appear until an event is complete. For developer guidance, see [LiveActivityIntent](https://developer.apple.com/documentation/appintents/liveactivityintent).

**Provide enough detail for interaction on audio-only devices.** People can receive responses on audio-only devices such as AirPods and HomePod too, and may not always be able to see content onscreen. Include all critical information in the full dialogue text of your App Shortcuts. For developer guidance, see [init(full:supporting:systemImageName:)](https://developer.apple.com/documentation/appintents/intentdialog/init(full:supporting:systemimagename:)).

## Editorial guidelines

**Provide brief, memorable activation phrases and natural variants.** Because an App Shortcut phrase (or a variant you define) is what people say to run an App Shortcut with Siri, it’s important to keep it brief to make it easier to remember. You have to include your app name, but you can be creative with it. For example, Keynote accepts both “Create a Keynote” and “Add a new presentation in Keynote” as App Shortcut phrases for creating a new document. For developer guidance, see [AppShortcutPhrase](https://developer.apple.com/documentation/appintents/appshortcutphrase).

**When referring to App Shortcuts or the Shortcuts app, always use title case and make sure that *Shortcuts* is plural.** For example, *MyApp integrates with Shortcuts to provide a quick way to get things done with just a tap or by asking Siri, and offers App Shortcuts you can place on the Action button.*

**When referring to individual shortcuts (not App Shortcuts or the Shortcuts app), use lowercase.** For example, *Run a shortcut by asking Siri or tapping a suggestion on the Lock Screen.*

## Platform considerations

### Mobile (iOS, iPadOS)

App Shortcuts can appear in the Top Hit area of Spotlight when people search for your app, or in the Shortcuts area below. Each App Shortcut includes a symbol from [SF Symbols](sf-symbols.md) that you choose to represent its functionality, or a preview image of an item that the shortcut links to directly.

**Order shortcuts based on importance.** The order you choose determines how App Shortcuts initially appear in both Spotlight and the Shortcuts app, so it’s helpful to include the most generally useful ones first. Once people start using your App Shortcuts, the system updates to prioritize the ones they use most frequently.

### Desktop (macOS)

App Shortcuts aren’t supported in macOS. However, actions you create for your app using App Intents are supported, and people can build custom shortcuts using them with the Shortcuts app on Mac.

## Change log

| Date | Changes |
| --- | --- |
| June 8, 2026 | Added guidance for adopting app schemas. |
| January 17, 2025 | Updated and streamlined guidance. |
| June 5, 2023 | New page. |

## Related guidelines

- [Siri](siri.md)

---


<a id="controls"></a>
## controls

# Controls

> Source: <https://developer.apple.com/design/human-interface-guidelines/controls>
> Section: Components › System experiences
> Platforms covered: iOS, iPadOS, macOS
> Last change on Apple's site: 2024-06-10 (New page.)

A control provides quick access to a feature of your app from Control Center, the Lock Screen, or the Action button.

---

A control is a button or toggle that provides quick access to your app’s features from other areas of the system. Control buttons perform an action, link to a specific area of your app, or launch a [camera experience on a locked device](#camera-experiences-on-a-locked-device). Control toggles switch between two states, such as on and off.

People can add controls to Control Center by pressing and holding in an empty area of Control Center, to the Lock Screen by customizing their Lock Screen, and to the Action button by configuring the Action button in the Settings app.

## Anatomy

Controls contain a symbol image, a title, and, optionally, a value. The symbol visually represents what the control does and can be a symbol from [SF Symbols](sf-symbols.md) or a custom symbol. The title describes what the control relates to, and the value represents the state of the control. For example, the title can display the name of a light in a room, while the value can display whether it’s on or off.

Controls display their information differently depending on where they appear:

- In Control Center, a control displays its symbol and, at larger sizes, its title and value.
- On the Lock Screen, a control displays its symbol.
- On iPhone devices with a control assigned to the Action button, pressing and holding it displays the control’s symbol in the Dynamic Island, as well as its value (if present).

## Best practices

**Offer controls for actions that provide the most benefit without having to launch your app.** For example, launching a Live Activity from a control creates an easy and seamless experience that informs someone about progress without having to navigate to your app to stay up to date. For guidance, see [Live Activities](live-activities.md).

**Update controls when someone interacts with them, when an action completes, or remotely with a push notification.** Update the contents of a control to accurately reflect the state and show if an action is still in progress.

**Choose a descriptive symbol that suggests the behavior of the control.** Depending on where a person adds a control, it may not display the title and value, so the symbol needs to convey enough information about the control’s action. For control toggles, provide a symbol for both the on and off states. For example, use the SF Symbols `door.garage.open` and `door.garage.closed` to represent a control that opens and closes a garage door. For guidance, see [SF Symbols](sf-symbols.md).

**Use symbol animations to highlight state changes.** For control toggles, animate the transition between both on and off states. For control buttons with actions that have a duration, animate indefinitely while the action performs and stop animating when the action is complete. For developer guidance, see [Symbols](https://developer.apple.com/documentation/symbols) and [SymbolEffect](https://developer.apple.com/documentation/symbols/symboleffect).

**Select a tint color that works with your app’s brand.** The system applies this tint color to a control toggle’s symbol in its on state. When a person performs the action of a control from the Action button, the system also uses this tint color to display the value and symbol in the Dynamic Island. For guidance, see [Branding](branding.md).

**Help people provide additional information the system needs to perform an action.** A person may need to configure a control to perform a desired action — for example, select a specific light in a house to turn on and off. If a control requires configuration, prompt people to complete this step when they first add it. People can reconfigure the control at any time. For developer guidance, see [promptsForUserConfiguration()](https://developer.apple.com/documentation/swiftui/controlwidgetconfiguration/promptsforuserconfiguration()).

**Provide hint text for the Action button.** When a person presses the Action button, the system displays hint text to help them understand what happens when they press and hold. When someone presses and holds the Action button, the system performs the action configured to it. Use verbs to construct the hint text. For developer guidance, see [controlWidgetActionHint(_:)](https://developer.apple.com/documentation/swiftui/view/controlwidgetactionhint(_:)-5yoyh).

**If your control title or value can vary, include a placeholder.** Placeholder information tells people what your control does when the title and value are situational. The system displays this information when someone brings up the controls gallery in Control Center or the Lock Screen and chooses your control, or before they assign it to the Action button.

**Hide sensitive information when the device is locked.** When the device is locked, consider having the system redact the title and value to hide personal or security-related information. Specify if the system needs to redact the symbol state as well. If specified, the system redacts the title and value, and displays the symbol in its off state.

**Require authentication for actions that affect security.** For example, require people to unlock their device to access controls to lock or unlock the door to their house or start their car. For developer guidance, see [IntentAuthenticationPolicy](https://developer.apple.com/documentation/appintents/intentauthenticationpolicy).

## Camera experiences on a locked device

If your app supports camera capture, starting with iOS 18 you can create a control that launches directly to your app’s camera experience while the device is locked. For any task beyond capture, a person must authenticate and unlock their device to complete the task in your app. For developer guidance, see [LockedCameraCapture](https://developer.apple.com/documentation/lockedcameracapture).

**Use the same camera UI in your app and your camera experience.** Sharing UI leverages people’s familiarity with the app. By using the same UI, the transition to the app is seamless when someone captures content and taps a button to perform additional tasks, such as posting to a social network or editing a photo.

**Provide instructions for adding the control.** Help people understand how to add the control that launches this camera experience.

## Platform considerations

*No additional considerations for iOS, iPadOS, or macOS. Not supported in watchOS, tvOS, or visionOS.*

## Change log

| Date | Changes |
| --- | --- |
| June 10, 2024 | New page. |

## Related guidelines

- [Widgets](widgets.md)

---


<a id="live-activities"></a>
## live-activities

# Live Activities

> Source: <https://developer.apple.com/design/human-interface-guidelines/live-activities>
> Section: Components › System experiences
> Platforms covered: iOS, iPadOS, macOS (guidance specific to watchOS omitted)
> Last change on Apple's site: 2026-10-13 (Added guidance for limited width layouts, and updated supported platforms and specifications.)

A Live Activity lets people track the progress of an activity, event, or task at a glance.

---

Live Activities let people keep track of tasks and events in glanceable locations across devices.  They go beyond push notifications, delivering frequent content and status updates over a few hours and letting people interact with the displayed information.

For example, a Live Activity might show the remaining time until a food delivery order arrives, live in-game information for a soccer match, or real-time fitness metrics and interactive controls to pause or cancel a workout.

A Live Activity from your app starts on iPad or iPhone and automatically appears in system locations across a person’s devices:

| Platform or system experience | Location |
| --- | --- |
| iPad and iPhone | Lock Screen, Home Screen, in the Dynamic Island and StandBy on iPhone |
| Mac | The menu bar |
| Apple Watch | Smart Stack |
| CarPlay | CarPlay Dashboard |

## Anatomy

Live Activities appear across the system in various locations like the Dynamic Island and the Lock Screen. Depending on the device and system location where a Live Activity appears, the system chooses a *presentation* style or a combination of styles to compose the appearance of your Live Activity. As a result, your Live Activity must support:

- [Compact](#compact)
- [Minimal](#minimal)
- [Expanded](#expanded)
- [Lock Screen](#lock-screen)

In iOS and iPadOS, your Live Activity appears throughout the system using these presentations. Additionally, the system uses them to create default appearances for other contexts. For example, the compact presentation appears in the Dynamic Island on iPhone and consists of two elements that the system combines into a single view for Apple Watch and in CarPlay.

### Compact

In the Dynamic Island, the system uses the compact presentation when only one Live Activity is active. The presentation consists of two separate elements: one on the leading side of the TrueDepth camera and one on the trailing side. Despite its limited space, the compact presentation displays up-to-date information about your app’s Live Activity.

For design guidance, see [Compact presentation](#compact-presentation).

### Minimal

When multiple Live Activities are active, the system uses the minimal presentation to display up to three of them in the Dynamic Island. One appears attached to the Dynamic Island, while a second (and third, when supported) appear detached on one or both sides. Depending on its content size, a detached minimal presentation appears circular or oval. As with the compact presentation, people tap the minimal presentation to open its app or touch and hold it to see the expanded presentation.

For design guidance, see [Minimal presentation](#minimal-presentation).

### Expanded

When people touch and hold a Live Activity in compact or minimal presentation, the system displays the expanded presentation.

For design guidance, see [Expanded presentation](#expanded-presentation).

### Lock Screen

The system uses the Lock Screen presentation to display a banner at the bottom of the Lock Screen. In this presentation, use a layout similar to the expanded presentation.

When you alert people about Live Activity updates on devices that don’t support the Dynamic Island, the Lock Screen presentation briefly appears as a banner that overlays the Home Screen or other apps.

For design guidance, see [Lock Screen presentation](#lock-screen-presentation).

### StandBy

On iPhone in StandBy, your Live Activity appears in the minimal presentation. When someone taps it, it transitions to the Lock Screen presentation, scaled up by 2x to fill the screen. If your Lock Screen presentation uses a custom background color, the system automatically extends it to the whole screen to create a seamless, full-screen design.

For design guidance, see [StandBy presentation](#standby-presentation).

## Best practices

**Offer Live Activities for tasks and events that have a defined beginning and end.** Live Activities work best for tracking short to medium duration activities that don’t exceed eight hours.

**Focus on important information that people need to see at a glance.** Your Live Activity doesn’t need to display everything. Think about what information people find most useful and prioritize sharing it in a concise way. When a person wants to learn more, they can tap your Live Activity to open your app where you can provide additional detail.

**Don’t use a Live Activity to display ads or promotions**. Live Activities help people stay informed about ongoing events and tasks, so it’s important to display only information that’s related to those events and tasks.

**Avoid displaying sensitive information.** Live Activities are prominently visible and could be viewed by casual observers; for example, on the Lock Screen or in the Always-On display. For content people might consider sensitive or private, display an innocuous summary and let people tap the Live Activity to view the sensitive information in your app. Alternatively, redact views that may contain sensitive information and let people configure whether to show sensitive data. For developer guidance, see [Creating a widget extension](https://developer.apple.com/documentation/widgetkit/creating-a-widget-extension).

**Create a Live Activity that matches your app’s visual aesthetic and personality in both dark and light appearances.** This makes it easier for people to recognize your Live Activity and creates a visual connection to your app.

**If you include a logo mark, display it without a container.** This better integrates the logo mark with your Live Activity layout. Don’t use the entire app icon.

**Don’t add elements to your app that draw attention to the Dynamic Island.** Your Live Activity appears in the Dynamic Island while your app isn’t in use, and other items can appear in the Dynamic Island when your app is open.

**Ensure text is easy to read.** Use large, heavier-weight text — a medium weight or higher. Use small text sparingly and make sure key information is legible at a glance.

### Creating Live Activity layouts

**Adapt to different screen sizes and presentations.** Live Activities scale to fit various device screens. Create layouts and assets for various devices and scale factors, recognizing that the actual size on screen may vary or change. Ensure they look great everywhere by using the values in [Specifications](#specifications) as guidance and providing appropriately sized content.

**Adjust element size and placement for efficient use of space.** Create a layout that only uses the space you need to clearly display its content. Adapt the size and placement of elements in your Live Activity so they fit well together.

**Support limited width presentations.** To avoid truncated text in contexts with limited width like the Dynamic Island on iPhone in landscape, adapt your compact and minimal presentations to fit inside a 28pt-diameter circle. Use a short abbreviation or graphic representation instead of a full text string. If limited width versions of both the leading and trailing compact views don’t make sense for your design, adopt a leading view only and leave the trailing view empty; the system automatically hides the trailing view. For developer guidance, see [isDynamicIslandLimitedInWidth](https://developer.apple.com/documentation/swiftui/environmentvalues/isdynamicislandlimitedinwidth).

**Use familiar layouts for custom views.** Templates with default system margins and recommended text sizes are available in [Apple Design Resources](https://developer.apple.com/design/resources/). Using them helps your Live Activity remain legible at a glance and fit in with the visual language of its surroundings; for example, the Smart Stack on Apple Watch.

**Use consistent margins and concentric placement.** Use even, matching margins between rounded shapes and the edges of the Live Activity to ensure a harmonious fit. This prevents elements from poking into the rounded shape of the Live Activity and creating visual tension. When you place a rounded element near the corner of a Live Activity, use [ContainerRelativeShape](https://developer.apple.com/documentation/swiftui/containerrelativeshape) to match the corner radius of the Live Activity instead of hard-coding a value for it.

Keep content compact and snug within a margin that’s concentric to the outer edge of the Live Activity.

**When separating a block of content, place it in an inset container shape or use a thick line.** Don’t draw content all the way to the edge of the Dynamic Island.

> **Tip:** To align nonrounded content in the rounded corners of the Live Activity view, it may be helpful to blur the nonrounded content in your drawing tool. When the content is blurred, it may be easier to find the positioning that best aligns with the outer perimeter of the view.

**Dynamically change the height of your Live Activity on the Lock Screen or in the expanded presentation.** When there’s less information to show, reduce the height of the Live Activity to only use the space needed for the content. When more information becomes available, increase the height to display additional content. For example, a rideshare app might display a more compact Live Activity without additional details while it locates a driver. The app’s height extends as more information is available to display the estimated pickup time, driver details, and so on.

### Choosing colors

**Carefully consider using a custom background color and opacity.** You can’t customize background colors for compact, minimal, and expanded presentations. However, you can use a custom background color for the Lock Screen presentation. If you set a custom background color or image for the Lock Screen presentation, ensure sufficient contrast — especially for tint colors on devices that feature an Always-On display with reduced luminance.

**Use color to express the character and identity of your app.** Live Activities in the Dynamic Island use a black opaque background. Consider using bold colors for text and objects to convey the personality and brand of your app. Bold colors make your Live Activity recognizable at a glance, stand out from other Live Activities, and feel like a small, glanceable part of your app. Additionally, bold colors can help reinforce the relationship between elements in the Live Activity itself.

**Tint your Live Activity’s key line color so that it matches your content.** When the background is dark — for example, in Dark Mode — a key line appears around the Dynamic Island to distinguish it from other content. Choose a key line color that’s consistent with the color of other elements in your Live Activity. For developer guidance, see [Creating custom views for Live Activities](https://developer.apple.com/documentation/activitykit/creating-custom-views-for-live-activities).

### Adding transitions and animating content updates

In addition to extending and contracting transitions, Live Activities use system and custom animations with a maximum duration of two seconds. Note that the system doesn’t perform animations on Always-On displays with reduced luminance.

**Use animations to reinforce the information you’re communicating and to bring attention to updates.** In addition to moving the position of elements, you can animate elements in and out with the default content-replace transition, or create custom transitions using scale, opacity, and movement. For example, a sports app might use numeric content transitions for score changes or fade a timer in and out when it reaches zero.

**Animate layout changes.** Content updates can require a change to your Live Activity layout — for example, when it expands to fill the screen in StandBy or when more information becomes available. During the transition to a new layout, preserve as much of the existing layout as possible by animating existing elements to their new positions rather than removing and animating them back in.

**Try to avoid overlapping elements.** Sometimes, it’s best to animate out certain elements and then re-animate them in at a new position to avoid colliding with other parts of your transition. For example, when animating items in lists, only animate the element that moves to a new position and use fade-in-and-out transitions for the other list items.

For developer guidance, see [Animating data updates in widgets and Live Activities](https://developer.apple.com/documentation/widgetkit/animating-data-updates-in-widgets-and-live-activities).

### Offering interactivity

**Make sure tapping the Live Activity opens your app at the right location.** Take people directly to related details and actions  — don’t make them navigate to find relevant information. For developer guidance on SwiftUI views that support deep linking to specific screens, see [Linking to specific app scenes from your widget or Live Activity](https://developer.apple.com/documentation/widgetkit/linking-to-specific-app-scenes-from-your-widget-or-live-activity).

**Focus on simple, direct actions.** Buttons or toggles take up space that might otherwise display useful information. Only include interactive elements for essential functionality that’s directly related to your Live Activity and that people activate once or temporarily pause and resume, like music playback, workouts, or apps that access the microphone to record live audio. If you offer interactivity, prefer limiting it to a single element to help people avoid accidentally tapping the wrong control.

**Consider letting people respond to event or progress updates.** If an update to your Live Activity is something that a person could respond to, consider offering a button or toggle to let people take action. For example, the Live Activity of a rideshare app could include a button to contact the driver while waiting for a ride to arrive.

### Starting, updating, and ending a Live Activity

**Start Live Activities at appropriate times, and make it easy for people to turn them off in your app.** People expect Live Activities to start and provide important updates for a task at hand or at specific times, even automatically. For example, they might expect a Live Activity to start after a food order, making a rideshare request, or when their favorite sports team’s match begins. However, Live Activities that appear unexpectedly can be surprising or even unwanted. Consider offering controls that allow people to turn off a Live Activity in the app view that corresponds to the activity. For example, a sports app may offer a button that lets people unfollow a game or team. When people can’t easily control the appearance of Live Activities from your app, they may choose to turn off Live Activities in Settings altogether.

**Offer an App Shortcut that starts your Live Activity.** App Shortcuts expose functionality to the system, allowing access in various contexts. For example, create an App Shortcut that allows people to start your Live Activity using the Action button on iPhone. For more information, see [App Shortcuts](app-shortcuts.md).

**Update a Live Activity only when new content is available.** If the underlying content or status remains the same, maintain the same display until the underlying content or status changes.

**Alert people only for essential updates that require their attention.** Live Activity alerts light up the screen and by default play the notification sound to alert people about updates they shouldn’t miss. Alerts also show the expanded presentation in the Dynamic Island or a banner on devices that don’t support the Dynamic Island. To ensure your Live Activities provide the most value, avoid alerting people too often or with updates that aren’t crucial, and don’t use push notifications alongside Live Activities for the same updates.

**Let people track multiple events efficiently with a single Live Activity.** Instead of creating separate Live Activities people need to jump between to track different events, prefer a single Live Activity that uses a dynamic layout and rotates through events. For example, a sports app could offer a single Live Activity that cycles through scored points, substitutions, and fouls across multiple matches.

**Always end a Live Activity immediately when the task or event ends, and consider setting a custom dismissal time.** When a Live Activity ends, the system immediately removes it from the Dynamic Island and in CarPlay. On the Lock Screen, in the Mac menu bar, and the watchOS Smart Stack, it remains for up to four hours. Depending on the Live Activity, showing a summary may only be relevant for a brief time after it ends. Consider choosing a custom dismissal time that’s proportional to the duration of your Live Activity. In most cases, 15 to 30 minutes is adequate. For example, a rideshare app could end its Live Activity when a ride completes and remain visible for 30 minutes to allow people to view the ride summary and leave a tip. For developer guidance, refer to [Displaying live data with Live Activities](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities).

## Presentation

Your Live Activity needs to support all locations, devices, and their corresponding appearances. Because it appears across systems at different dimensions, create Live Activity layouts that best support each place they appear.

**Start with the iPhone design, then refine it for other contexts.** Create standard designs for each presentation first. Then, depending on the functionality that your Live Activity provides, design additional custom layouts for specific contexts like iPhone in StandBy, CarPlay, or Apple Watch. For more information about custom layouts, refer to [StandBy](#standby), [CarPlay](#carplay), and watchOS.

### Compact presentation

**Focus on the most important information.** Use the compact presentation to show dynamic, up-to-date information that’s essential to the Live Activity and easy to understand. For example, a sports app could display two team logos and the score.

**Ensure unified information and design of the compact presentations in the Dynamic Island.** Though the TrueDepth camera separates the leading and trailing elements, design them to read as a single piece of information, and use consistent color and typography to help create a connection between both elements.

**Keep content as narrow as possible and ensure it’s snug against the TrueDepth camera.** Try not to obscure key information in the status bar, and don’t add padding between content and the TrueDepth camera. Maintain a balanced layout with similarly sized views for both leading and trailing elements; for example, use shortened units or less precise data to maintain appropriate width and balance.

**Link to relevant app content.** When people tap a compact Live Activity, open your app directly to the related details. Ensure both leading and trailing elements link to the same screen.

### Minimal presentation

**Ensure that your Live Activity is recognizable in the minimal presentation.** If possible, display updated information rather than just a logo, while ensuring people can quickly recognize your app. For example, the Timer app’s minimal Live Activity presentation displays the remaining time instead of a static icon.

### Expanded presentation

**Maintain the relative placement of elements to create a coherent layout between presentations.** The expanded presentation is an enlarged version of the compact or minimal presentation. Ensure information and layouts expand predictably when the Live Activity expands.

**Wrap content tightly around the TrueDepth camera.** Arrange content close to the TrueDepth camera, and try to avoid leaving too much room around it to use space more efficiently and to help diminish the camera’s presence.

### Lock Screen presentation

**Don’t replicate notification layouts.** Create a unique layout that’s specific to the information that appears in the Live Activity.

**Choose colors that work well on a personalized Lock Screen.** People customize their Lock Screen with wallpapers, custom tint colors, and widgets. To make a Live Activity fit a custom Lock Screen aesthetic while remaining legible, use custom background or tint colors and opacity sparingly.

**Make sure your design, assets, and colors look great and offer enough contrast in Dark Mode and on an Always-On display.** By default, a Live Activity on the Lock Screen uses a light background color in the light appearance and a dark background color in the dark appearance. If you use a custom background color, choose a color that works well in both modes or a different color for each appearance. Verify your choices on a device with an Always-On display with reduced luminance because the system adapts colors as needed in this appearance. For guidance, see [Dark Mode](dark-mode.md) and Always On; for developer guidance, see [About asset catalogs](https://help.apple.com/xcode/mac/current/#/dev10510b1f7).

**Verify the generated color of the dismiss button.** The system automatically generates a matching dismiss button based on the background and foreground colors of your Live Activity.  Verify that the generated color matches your design and adjust it if needed using [activitySystemActionForegroundColor(_:)](https://developer.apple.com/documentation/swiftui/view/activitysystemactionforegroundcolor(_:)).

**Use standard margins to align your design with notifications.** The standard layout margin for Live Activities on the Lock Screen is 14 points. While tighter margins may be appropriate for elements like graphics or buttons, avoid crowding the edges and creating a cluttered appearance. For developer guidance, see [padding(_:_:)](https://developer.apple.com/documentation/swiftui/view/padding(_:_:)).

### StandBy presentation

**Update your layout for StandBy.** Make sure assets look great at the larger scale, and consider creating a custom layout that makes use of the extra space. For developer guidance, see [Creating custom views for Live Activities](https://developer.apple.com/documentation/activitykit/creating-custom-views-for-live-activities).

**Consider using the default background color in StandBy.** The default background color seamlessly blends your Live Activity with the device bezel, achieves a softer look that integrates with a person’s surroundings, and allows the system to scale the Live Activity slightly larger because it doesn’t need to account for the margins around the TrueDepth camera.

**Use standard margins and avoid extending graphic elements to the edge of the screen.** Without standard margins, content gets cut off as the Live Activity extends, making it feel broken.

**Verify your design in Night Mode.** In Night Mode, the system applies a red tint to your Live Activity. Check that your Live Activity design uses colors that provide enough contrast in Night Mode.

## CarPlay

In CarPlay, the system automatically combines the leading and trailing elements of the compact presentation into a single layout that appears on CarPlay Dashboard.

Your Live Activity design applies to both CarPlay and Apple Watch, so design for both contexts. While Live Activities on Apple Watch can be interactive, the system deactivates interactive elements in CarPlay. For more information, refer to watchOS below. For developer guidance, refer to [Creating custom views for Live Activities](https://developer.apple.com/documentation/activitykit/creating-custom-views-for-live-activities).

**Consider creating a custom layout if your Live Activity would benefit from larger text or additional information.** Instead of using the default appearance in CarPlay, declare support for a [ActivityFamily.small](https://developer.apple.com/documentation/widgetkit/activityfamily/small) supplemental activity family.

**Carefully consider including buttons or toggles in your custom layout.** In CarPlay, the system deactivates interactive elements in your Live Activity. If people are likely to start or observe your Live Activity while driving, prefer displaying timely content rather than buttons and toggles.

## Platform considerations

*No additional considerations for iOS or iPadOS. Not supported in tvOS or visionOS.*

### Desktop (macOS)

Active Live Activities automatically appear in the Menu bar of a paired Mac using the compact, minimal, and expanded presentations. Clicking the Live Activity launches iPhone Mirroring to display your app.

## Specifications

When you design your Live Activities, use the following values for guidance. All values listed in the tables below are in points.

### CarPlay dimensions

The system may scale your Live Activity to best fit a vehicle’s screen size and resolution. Use the listed values to verify your design:

| Live Activity size (pt) |
| --- |
| 240x78 |
| 240x100 |
| 170x78 |

Test your designs with the CarPlay simulator and the following configurations for Smart Display Zoom  — available in in Settings > Display in CarPlay:

| Configuration | Resolution (pt) |
| --- | --- |
| Widescreen | 1920x720 |
| Portrait | 900x1200 |
| Standard | 800x480 |

### iOS dimensions

| Screen dimensions (portrait) | Compact (leading and trailing) | Minimal (width given as a range) | Expanded (height given as a range) | Lock Screen (height given as a range) | Limited width |
| --- | --- | --- | --- | --- | --- |
| 430x932 | 62.33x36.67 | 36.67–45x36.67 | 408x84–160 | 408x84–160 | 28x28 |
| 393x852 | 52.33x36.67 | 36.67–45x36.67 | 371x84–160 | 371x84–160 | 28x28 |

### iPadOS dimensions

| Screen dimensions (portrait) | Lock Screen (height given as a range) |
| --- | --- |
| 1366x1024 | 500x84–160 |
| 1194x834 | 425x84–160 |
| 1012x834 | 425x84–160 |
| 1080x810 | 425x84–160 |
| 1024x768 | 425x84–160 |

### macOS dimensions

Use the provided iOS dimensions.

## Change log

| Date | Changes |
| --- | --- |
| October 13, 2026 | Added guidance for limited width layouts, and updated supported platforms and specifications. |
| December 16, 2025 | Updated guidance for all platforms, and added guidance for macOS and CarPlay. |
| June 10, 2024 | Added guidance for Live Activities in watchOS. |
| October 24, 2023 | Expanded and updated guidance and added new artwork. |
| June 5, 2023 | Updated guidance to include features of iOS 17 and iPadOS 17. |
| November 3, 2022 | Updated artwork and specifications. |
| September 23, 2022 | New page. |

---


<a id="notifications"></a>
## notifications

# Notifications

> Source: <https://developer.apple.com/design/human-interface-guidelines/notifications>
> Section: Components › System experiences
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2023-10-24 (Updated watchOS platform considerations with guidance for presenting notification responses to double tap.)

A notification gives people timely, high-value information they can understand at a glance.

---

Before you can send any notifications to people, you have to get their consent (for developer guidance, see [Asking permission to use notifications](https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications)). After agreeing, people generally use settings to specify the styles of notification they want to receive, and to specify delivery times for notifications that have different levels of urgency. To learn more about the ways people can customize the notification experience, see [Managing notifications](managing-notifications.md).

## Anatomy

Depending on the platform, a notification can use various styles, such as:

- A banner or view on a Lock Screen, Home Screen, Home View, or desktop
- A badge on an app icon
- An item in Notification Center

In addition, a notification related to direct communication — like a phone call or message — can provide an interface that’s distinct from noncommunication notifications, featuring prominent contact images (or *avatars*) and group names instead of the app icon.

## Best practices

**Provide concise, informative notifications.** People turn on notifications to get quick updates, so you want to provide valuable information succinctly.

**Avoid sending multiple notifications for the same thing, even if someone hasn’t responded.** People attend to notifications at their convenience. If you send multiple notifications for the same thing, you fill up Notification Center, and people may turn off all notifications from your app.

**Avoid sending a notification that tells people to perform specific tasks within your app.** If it makes sense to offer simple tasks that people can perform without opening your app, you can provide [notification actions](#notification-actions). Otherwise, avoid telling people what to do because it’s hard for people to remember such instructions after they dismiss the notification.

**Use an alert — not a notification — to display an error message.** People are familiar with both alerts and notifications, so you don’t want to cause confusion by using the wrong component. For guidance, see [Alerts](alerts.md).

**Handle notifications gracefully when your app is in the foreground.** Your app’s notifications don’t appear when your app is in the front, but your app still receives the information. In this scenario, present the information in a way that’s discoverable but not distracting or invasive, such as incrementing a badge or subtly inserting new data into the current view. For example, when a new message arrives in a mailbox that people are currently viewing, Mail simply adds it to the list of unread messages because sending a notification about it would be unnecessary and distracting.

**Avoid including sensitive, personal, or confidential information in a notification.** You can’t predict what people will be doing when they receive a notification, so it’s essential to avoid including private information that could be visible to others.

## Content

When a notification includes a title, the system displays it at the top where it’s most visible. In a notification related to direct communication, the system automatically displays the sender’s name in the title area; in a noncommunication notification, the system displays your app name if you don’t provide a title.

**Create a short title if it provides context for the notification content.** Prefer brief titles that people can read at a glance, especially on Apple Watch, where space is limited. When possible, take advantage of the prominent notification title area to provide useful information, like a headline, event name, or email subject. If you can only provide a generic title for a noncommunication notification — like New Document — it can be better to let the system display your app name instead. Use title-style [capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64) and no ending punctuation.

**Write succinct, easy-to-read notification content.** Use complete sentences, sentence case, and proper punctuation, and don’t truncate your message — the system does this automatically when necessary.

**Provide generically descriptive text to display when notification previews aren’t available.** In Settings, people can choose to hide notification previews for all apps. In this situation, the system shows only your app icon and the default title *Notification*. To give people sufficient context to know whether they want to view the full notification, write body text that succinctly describes the notification content without revealing too many details, like “Friend request,” “New comment,” “Reminder,” or “Shipment” (for developer guidance, see [hiddenPreviewsBodyPlaceholder](https://developer.apple.com/documentation/usernotifications/unnotificationcategory/hiddenpreviewsbodyplaceholder)). Use sentence-style [capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64) for this text.

**Avoid including your app name or icon.** The system automatically displays a large version of your app icon at the leading edge of each notification; in a communication notification, the system displays the sender’s contact image badged with a small version of your icon.

**Consider providing a sound to supplement your notifications.** Sound can be a great way to distinguish your app’s notifications and get someone’s attention when they’re not looking at the device. You can create a custom sound that coordinates with the style of your app or use a system-provided alert sound. If you use a custom sound, make sure it’s short, distinctive, and professionally produced. A notification sound can enhance the user experience, but don’t rely on it to communicate important information, because people may not hear it. Although people might also want a vibration to accompany alert sounds, you can’t provide such a vibration programmatically. For developer guidance, see [UNNotificationSound](https://developer.apple.com/documentation/usernotifications/unnotificationsound).

## Notification actions

A notification can present a customizable detail view that contains up to four buttons people use to perform actions without opening your app. For example, a Calendar event notification provides a Snooze button that postpones the event’s alarm for a few minutes. For developer guidance, see [Handling notifications and notification-related actions](https://developer.apple.com/documentation/usernotifications/handling-notifications-and-notification-related-actions).

**Provide beneficial actions that make sense in the context of your notification.** Prefer actions that let people perform common, time-saving tasks that eliminate the need to open your app. For each button, use a short, title-case term or phrase that clearly describes the result of the action. Don’t include your app name or any extraneous information in the button label, keep the text brief to avoid truncation, and take localization into account as you write it.

**Avoid providing an action that merely opens your app.** When people tap a notification or its preview, they expect your app to display related content, so presenting an action button that does the same thing clutters the detail view and can be confusing.

**Prefer nondestructive actions.** If you must provide a destructive action, make sure people have enough context to avoid unintended consequences. The system gives a distinct appearance to the actions you identify as destructive.

**Provide a simple, recognizable interface icon for each notification action.** An interface icon reinforces an action’s meaning, helping people instantly understand what it does. The system displays your interface icon on the trailing side of the action title. When you use [SF Symbols](sf-symbols.md), you can choose an existing symbol that represents your command or edit a related symbol to create a custom icon.

## Badging

A badge is a small, filled oval containing a number that can appear on an app icon to indicate the number of unread notifications that are available. After people address unread notifications, the badge disappears from the app icon, reappearing when new notifications arrive. People can choose whether to allow an app to display badges in their notification settings.

**Use a badge only to show people how many unread notifications they have.** Don’t use a badge to convey numeric information that isn’t related to notifications, such as weather-related data, dates and times, stock prices, or game scores.

**Make sure badging isn’t the only method you use to communicate essential information.** People can turn off badging for your app, so if you rely on it to show people when there’s important information, people can miss the message. Always make sure that you make important information easy for people to find as soon as they open your app.

**Keep badges up to date.** Update your app’s badge as soon as people open the corresponding notifications. You don’t want people to think there are new notifications available, only to find that they’ve already viewed them all. Note that reducing a badge’s count to zero removes all related notifications from Notification Center.

**Avoid creating a custom image or component that mimics the appearance or behavior of a badge.** People can turn off notification badges if they choose, and will become frustrated if they have done so and then see what appears to be a badge.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.*

## Change log

| Date | Changes |
| --- | --- |
| October 24, 2023 | Updated watchOS platform considerations with guidance for presenting notification responses to double tap. |

## Related guidelines

- [Managing notifications](managing-notifications.md)
- [Alerts](alerts.md)

---


<a id="snippets"></a>
## snippets

# Snippets

> Source: <https://developer.apple.com/design/human-interface-guidelines/snippets>
> Section: Components › System experiences
> Platforms covered: iOS, iPadOS, macOS
> Last change on Apple's site: 2026-06-08 (New page.)

When someone performs a task with Siri or an App Shortcut, a snippet shows the result or asks for confirmation.

---

Snippets are compact views that appear in response to an action that someone takes using [Siri](siri.md), Spotlight, or the Shortcuts app.

You can present a snippet related to one of your app’s actions by including it with an [app intent](https://developer.apple.com/documentation/appintents) that you design to meet the specific needs of a task. For example, you might design a snippet for checking the weather forecast or updating progress toward a daily goal.

There are two snippet types: confirmation and result. A *confirmation* snippet lets people confirm or cancel an action, and may include options that affect the result. By contrast, a *result* snippet provides information — possibly as the outcome of a confirmation — that doesn’t require further action. An app intent that displays a snippet always shows a result, while the confirmation step is optional.

For developer guidance, see [Displaying static and interactive snippets](https://developer.apple.com/documentation/appintents/displaying-static-and-interactive-snippets).

## Anatomy

A snippet consists of the following elements:

- **Dialogue.** The app intent dialogue that Siri speaks to communicate the snippet’s information. The system includes the dialogue text by default and places it above the custom view.
- **Custom view.** A view that visually communicates the snippet’s information. A custom view can include one or more buttons for modifying the content of the snippet, getting more information, or taking another action.
- **System-provided button(s).** A confirmation snippet includes two system-provided buttons under the custom view: a secondary Cancel button and a primary button with a customizable label. A result snippet includes a single Done button that dismisses the view.

## Best practices

**Ensure legibility.** Check for sufficient contrast between the snippet’s custom content and the system-provided background in both light and dark appearances, and keep consistent margins for the content within the view. This clarifies the layout and helps people interpret the snippet quickly and reliably.

**Keep content concise.** Snippets exist to facilitate lightweight, quick interactions, so it’s important to keep their content short and easily legible. To ensure all content is visible, create custom views that are no taller than the 400-point maximum height. When considering the amount of text to include, be mindful that fonts draw at various sizes based on a person’s preferred text size setting. For a result snippet, if you need to provide more detail, deep-link to the content in your app instead of including it in the custom view.

**Choose a descriptive label for a confirmation snippet’s primary button.** You can choose an appropriate label from among those that the [system provides](https://developer.apple.com/documentation/appintents/confirmationactionname), or you can supply a custom label. For example, when designing a snippet to order coffee, labeling the primary button Order is clearer than labeling it OK or Proceed. If you don’t specify a label, the system default is Continue.

**Communicate a snippet’s purpose visually.** Don’t rely on showing the dialogue text to convey a snippet’s purpose. While the spoken app intent dialogue is essential for interactions when someone isn’t looking at the screen, prefer to omit it from a snippet’s visual representation and use the custom view to convey its information instead.

## Platform considerations

*No additional considerations for iOS, iPadOS, or macOS. Not supported in tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| June 8, 2026 | New page. |

## Related guidelines

- [Siri](siri.md)
- [App Shortcuts](app-shortcuts.md)
- [Live Activities](live-activities.md)

---


<a id="status-bars"></a>
## status-bars

# Status bars

> Source: <https://developer.apple.com/design/human-interface-guidelines/status-bars>
> Section: Components › System experiences
> Platforms covered: iOS, iPadOS

A status bar appears along the upper edge of the screen and displays information about the device’s current state, like the time, cellular carrier, and battery level.

---

## Best practices

**Obscure content under the status bar.** By default, the background of the status bar is transparent, allowing content beneath to show through. This transparency can make it difficult to see information presented in the status bar. If controls are visible behind the status bar, people may attempt to interact with them and be unable to do so. Be sure to keep the status bar readable, and don’t imply that content behind it is interactive. Prefer using a scroll edge effect to place a blurred view behind the status bar. For developer guidance, see [ScrollEdgeEffectStyle](https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle) and [UIScrollEdgeEffect](https://developer.apple.com/documentation/uikit/uiscrolledgeeffect).

**Consider temporarily hiding the status bar when displaying full-screen media.** A status bar can be distracting when people are paying attention to media. Temporarily hide these elements to provide a more immersive experience. The Photos app, for example, hides the status bar and other interface elements when people browse full-screen photos.

**Avoid permanently hiding the status bar.** Without a status bar, people have to leave your app to check the time or see if they have a Wi-Fi connection. Let people redisplay a hidden status bar with a simple, discoverable gesture. For example, when browsing full-screen photos in the Photos app, a single tap shows the status bar again.

## Platform considerations

*No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.*

---


<a id="widgets"></a>
## widgets

# Widgets

> Source: <https://developer.apple.com/design/human-interface-guidelines/widgets>
> Section: Components › System experiences
> Platforms covered: iOS, iPadOS, macOS (guidance specific to watchOS, visionOS omitted)
> Last change on Apple's site: 2026-10-13 (Added guidance for Apple HomeView, and updated watchOS specifications.)

A widget provides quick access to essential information and focused interactions from your app or game in additional contexts.

---

Widgets help people organize and personalize their devices by displaying timely, glanceable content and offering specific functionality. They appear in various contexts for a consistent experience across platforms. For example, a person might place a Weather widget:

- On the Home Screen and Lock Screen of their iPhone and iPad
- On the desktop and Notification Center of their Mac
- On a horizontal or vertical surface when they wear Apple Vision Pro
- At a fixed position in the Smart Stack of Apple Watch
- On the Home Screen and Modular face of Apple HomeView

## Anatomy

Widgets come in different sizes, ranging from small accessory widgets on iPad, iPhone, and Apple Watch to system family widgets that include an extra large size on iPad, Mac, and Apple Vision Pro. Additionally, widgets adapt their appearance to the context in which they appear and respond to a person’s device customization. Consider the following when designing widgets:

- The widget size to support
- The context — devices and system experiences — in which the widget may appear
- The rendering modes and color treatment that the widget receives based on the size and context

The WidgetKit framework provides default appearances and treatments for each widget size to fit the system experience or device where it appears. However, it’s important to consider creating a custom widget design that can provide the best experience for your content in each specific context.

### System family widgets

System family widgets offer a broad range of sizes and may include one or more interactive elements.

*Illustrated: Small, Medium, Large, Extra large, Extra large portrait.*

The following table shows supported contexts for each system family widget size:

| Widget size | iPhone | iPad | Mac | Apple Vision Pro |
| --- | --- | --- | --- | --- |
| System small | Home Screen, Today View, StandBy, CarPlay, and Apple HomeView | Home Screen, Today View, and Lock Screen | Desktop and Notification Center | Horizontal and vertical surfaces |
| System medium | Home Screen and Today View | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System large | Home Screen and Today View | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System extra large | Not supported | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System extra large portrait | Not supported | Not supported | Not supported | Horizontal and vertical surfaces |

### Accessory widgets

Accessory widgets display a very limited amount of information because of their size.

*Illustrated: Accessory circular, Accessory corner, Accessory inline, Accessory rectangular.*

They appear on the following devices:

| Widget size | iPhone | iPad | Apple Watch |
| --- | --- | --- | --- |
| Accessory circular | Lock Screen | Lock Screen | Watch complications and in the Smart Stack |
| Accessory corner | Not supported | Not supported | Watch complications |
| Accessory inline | Lock Screen | Lock Screen | Watch complications |
| Accessory rectangular | Lock Screen | Lock Screen | Watch complications and in the Smart Stack |

### Appearances

A widget can appear in full-color, in monochrome with a tint color, or in a clear, translucent style. Depending on the location, device, and a person’s customization, the system may apply a tinted or clear appearance to the widget and its included full-color images, symbols, and glyphs.

For example, a small system widget appears differently depending on the device and location:

- On the Home Screen of iPad, iPhone, and Apple HomeView, people choose from different appearances for widgets: light, dark, clear, and tinted. In light and dark appearances, widgets have a full-color design. In a clear appearance, the system desaturates the widget and adds translucency, highlights, and the Liquid Glass material. In a tinted appearance, the system desaturates the widget and its content, then applies a person’s selected tint color.

- On Apple Vision Pro, the widget appears as a 3D object, surrounded by a frame. It takes on a full-color appearance with a glass- or paper-like coating layer that responds to lighting conditions. Additionally, people can choose a tinted appearance that applies a color from a set of system-provided color palettes.

- On the Lock Screen of iPad, the widget takes on a monochromatic appearance without a tint color.

- On the Lock Screen of iPhone in StandBy and the Modular face of Apple HomeView, the widget appears scaled up in size with the background removed. When the ambient light falls below a threshold, the system renders the widget with a monochromatic red tint.

Similarly, a rectangular accessory widget appears as follows:

- On the Lock Screen of iPhone and iPad, it takes on a monochromatic appearance without a tint color.
- On Apple Watch, the widget can appear as a watch complication in both full-color and tinted appearances, and it can also appear in the Smart Stack.

*Illustrated: iPhone Lock Screen, Watch complication, Smart Stack on Apple Watch.*

Each appearance described above includes a [rendering mode](#rendering-modes) that depends on the platform and a person’s appearance settings:

- The system uses the [full color](https://developer.apple.com/documentation/widgetkit/widgetrenderingmode/fullcolor) rendering mode for system family widgets across all platforms to display your widget in full color. It doesn’t change the color of your views.
- The system uses the [accented](https://developer.apple.com/documentation/widgetkit/widgetrenderingmode/accented) rendering mode for system family widgets across all platforms and for accessory widgets on Apple Watch. In the accented rendering mode, the system removes the background and replaces it with a tinted color effect for a tinted appearance and a Liquid Glass background for a clear appearance. Additionally, it divides the widget’s views into an accent group and a primary group, and then applies a solid color to each group.
- The system uses the [vibrant](https://developer.apple.com/documentation/widgetkit/widgetrenderingmode/vibrant) rendering mode for widgets on the Lock Screen of iPhone and iPad, and on iPhone in StandBy in low-light conditions. It desaturates text, images, and gauges, and creates a vibrant effect by coloring your content appropriately for the Lock Screen background or a macOS desktop. Note that people can customize the Lock Screen with a tint color, and the system applies a red tint for widgets that appear on iPhone in StandBy in low-light conditions.

The following table lists the occurrences for each rendering mode per platform:

| Platform | Full-color | Accented | Vibrant |
| --- | --- | --- | --- |
| iPhone | Home Screen, Today view, StandBy and CarPlay (with the background removed) | Home Screen and Today view | Lock Screen, StandBy in Night Mode |
| iPad | Home Screen and Today view | Home Screen and Today view | Lock Screen |
| Apple Watch | Smart Stack, complications | Smart Stack, complications | Not supported |
| Mac | Desktop and Notification Center | Not supported | Desktop |
| Apple Vision Pro | Horizontal and vertical surfaces | Horizontal and vertical surfaces | Not supported |
| Apple HomeView | Home Screen, Modular face (with the background removed) | Home Screen, Modular face (with the background removed) | Modular face in Night Mode |

For additional design guidance, see [Rendering modes](#rendering-modes). For developer guidance, see [Preparing widgets for additional platforms, contexts, and appearances](https://developer.apple.com/documentation/widgetkit/preparing-widgets-for-additional-contexts-and-appearances) and [WidgetRenderingMode](https://developer.apple.com/documentation/widgetkit/widgetrenderingmode).

## Best practices

**Choose simple ideas that relate to your app’s main purpose.** Include timely content and relevant functionality. For example, people who use the Weather app are often most interested in the current high and low temperatures and weather conditions, so the Weather widgets prioritize this information.

**Aim to create a widget that gives people quick access to the content they want.** People appreciate widgets that display meaningful content and offer useful actions and deep links to key areas of your app. Replicating an app icon offers little additional value, and people may be less likely to keep it on their screens.

**Prefer dynamic information that changes throughout the day.** If a widget’s content never appears to change, people may not keep it in a prominent position. Although widgets don’t update from minute to minute, it’s important to find ways to keep their content fresh to invite frequent viewing.

**Look for opportunities to surprise and delight.** For example, you might design a unique visual treatment for your calendar widget to display on meaningful occasions, like birthdays or holidays.

**Offer widgets in multiple sizes when doing so adds value.** Small widgets use their limited space to typically show a single piece of information while larger sizes support additional layers of information and actions. Avoid expanding a smaller widget’s content to simply fill a larger area. It’s more important to create one widget in the size that best represents the content than providing the widget in all sizes.

**Balance information density.** Sparse layouts can make the widget seem unnecessary, while overly dense layouts are less glanceable. Create a layout that provides essential information at a glance and allows people to view additional details by taking a longer look. If your layout is too dense, consider improving its clarity by using a larger widget size or replacing text with graphics.

**Display only the information that’s directly related to the widget’s main purpose.** In larger widgets, you can display more data — or more detailed visualizations of the data — but you don’t want to lose sight of the widget’s primary purpose. For example, all Calendar widgets display a person’s upcoming events. In each size, the widget remains centered on events while expanding the range of information as the size increases.

**Use brand elements thoughtfully.** Incorporate brand colors, typefaces, and stylized glyphs to make your widget recognizable but don’t overpower useful information or make your widget look out of place. When you include brand elements, people seldom need your logo or app icon to help them recognize your widget. If your widget benefits from including a small logo — for example, if your widget displays content from multiple sources — a small logo in the top-right corner is sufficient.

**Choose between automatically displaying content and letting people customize displayed information.** In some cases, people need to configure a widget to ensure it displays the information that’s most useful for them. For example, the Stocks widget lets people select the stocks they wish to track. In contrast, some widgets — like the Podcasts widget — automatically display recent content, so people don’t need to customize them. For developer guidance, see [Making a configurable widget](https://developer.apple.com/documentation/widgetkit/making-a-configurable-widget).

**Avoid mirroring your widget’s appearance within your app.** Including an element in your app that looks like your widget but doesn’t behave like it can confuse people. Additionally, people may be less likely to try other ways to interact with such an element in your app because they expect it to behave like a widget.

**Let people know when authentication adds value.** If your widget provides additional functionality when someone is signed in to your app, make sure people know that. For example, an app that shows upcoming reservations might include a message like “Sign in to view reservations” when people are signed out.

### Updating widget content

To remain relevant and useful, widgets periodically refresh their information but don’t support continuous, real-time updates, and the system may adjust the limits for updates depending on various factors.

**Keep your widget up to date.** Finding the appropriate update frequency for your widget depends on knowing how often the data changes and estimating when people need to see new data. For example, a widget that provides information about tidal conditions at a beach is useful if it updates on an hourly basis even though conditions change constantly. If people are likely to check your widget more frequently than you can update it, consider displaying text that describes when the data was last updated.

**Use system functionality to refresh dates and times in your widget.** Because widget update frequency is limited, let the system automatically refresh date and time information to preserve update opportunities. Determine the update frequency that fits with the data you display and show content quickly without hiding stale data behind placeholder content. For developer guidance about widget updates, see [Keeping a widget up to date](https://developer.apple.com/documentation/widgetkit/keeping-a-widget-up-to-date).

**Use animated transitions to bring attention to data updates.** By default, many SwiftUI views animate content updates. Additionally, use standard and custom animations with a duration of up to two seconds to let people know when new information is available or when content displays differently. For developer guidance, see [Animating data updates in widgets and Live Activities](https://developer.apple.com/documentation/widgetkit/animating-data-updates-in-widgets-and-live-activities).

### Adding interactivity

People tap or click a widget to launch its corresponding app. It can also include buttons and toggles to offer additional functionality without launching the app. For example, the Reminders widget includes toggles to mark a task as completed.  When people interact with your widget in areas that aren’t buttons or toggles, the interaction launches your app.

**Offer simple, relevant functionality and reserve complexity for your app.** Useful widgets offer an easy way to complete a task or action that’s directly related to its content.

**Ensure that a widget interaction opens your app at the right location.** Deep link to details and actions that directly relate to the widget’s content, and don’t make people navigate to the relevant area in the app. For example, when people click or tap a medium Stocks widget, the Stocks app opens to a page that displays information about the symbol.

**Offer interactivity while remaining glanceable and uncluttered.** Multiple interaction targets — SwiftUI links, buttons, and toggles — might make sense for your content, but avoid creating app-like layouts in your widgets. Pay attention to the size of targets and make sure people can tap or click them with confidence and without accidentally performing unintended interactions. Note that inline accessory widgets offer only one tap target.

### Choosing margins and padding

Widgets scale to adapt to the screen sizes of different devices and onscreen areas. Supply content at appropriate sizes to make sure that your widget looks great on every device and let the system resize or scale it as necessary. In iOS, the system ensures that your widget looks good on small devices by resizing the content you design for large devices. In iPadOS, the system renders your widget at a large size before scaling it down for display on the Home Screen.

As you design for various devices and scale factors, use the values listed in [Specifications](#specifications) and the [Apple Design Resources](https://developer.apple.com/design/resources/) for guidance; for your production widget, use [SwiftUI](https://developer.apple.com/documentation/swiftui) to ensure flexibility.

**In general, use standard margins to ensure legibility.** Use the standard margin width for widgets — 16 points for most widgets — to avoid crowding their edges and creating a cluttered appearance. If you need to use tighter margins — for example, to create content groupings for graphics, buttons, or background shapes — setting margins of 11 points can work well. Additionally, note that widgets use smaller margins on the desktop on Mac and on the Lock Screen, including in StandBy. For developer guidance, see [padding(_:_:)](https://developer.apple.com/documentation/swiftui/view/padding(_:_:)).

**Coordinate the corner radius of your content with the corner radius of the widget.** To ensure that your content looks good within a widget’s rounded corners, use a SwiftUI container to apply the correct corner radius. For developer guidance, see [ContainerRelativeShape](https://developer.apple.com/documentation/swiftui/containerrelativeshape).

### Displaying text in widgets

**Prefer using the system font, text styles, and SF Symbols.** Using the system font helps your widget look at home on any platform, while making it easier for you to display great-looking text in a variety of weights, styles, and sizes. Use SF Symbols to align and scale symbols with text that uses the system font. If you use a custom font, do so sparingly, and be sure it’s easy for people to read at a glance. It often works well to use a custom font for the large text in a widget and SF Pro for the smaller text. For guidance, see [Typography](typography.md) and [SF Symbols](sf-symbols.md).

**Avoid very small font sizes.** In general, display text using fonts at 11 points or larger. Text in a font that’s smaller than 11 points can be too hard for many people to read.

**Avoid rasterizing text.** Always use text elements and styles to ensure that your text scales well and to allow VoiceOver to speak your content.

> **Note:** In iOS, iPadOS, and visionOS, widgets support Dynamic Type sizes from Large to AX5 when you use [Font](https://developer.apple.com/documentation/swiftui/font) to choose a system font or [custom(_:size:)](https://developer.apple.com/documentation/swiftui/font/custom(_:size:)) to choose a custom font. For more information about Dynamic Type sizes, see [Supporting Dynamic Type](typography.md#supporting-dynamic-type).

### Using color

**Use color to enhance a widget’s appearance without competing with its content.** Beautiful colors draw the eye, but they’re best when they don’t prevent people from absorbing a widget’s information at a glance. In your asset catalog, you can also specify the colors you want the system to use as it generates your widget’s editing-mode user interface.

**Convey meaning without relying on specific colors to represent information.** Widgets can appear monochromatic (with or without a custom tint color), and in watchOS, the system may invert colors depending on the watch face a person chooses. Use text and iconography in addition to color to express meaning.

**Use full-color images judiciously.** When a person chooses a tinted or clear appearance for their widgets, the system by default desaturates full-color images. You can choose to render images in full-color, even when a person chooses a tinted or clear widget appearance. However, full-color images in these appearances draw special attention to the widget, which might make it feel as if the widget doesn’t belong to the platform. For example, a full-color image in a widget might appear out of place when a person chooses a clear widget appearance. Consider reserving full-color images to represent media content, such as album art for a music app’s widget, and use full-color images with smaller dimensions than the size of the widget.

## Rendering modes

### Full-color

**Support light and dark appearances.** Prefer light backgrounds for the light appearance and dark backgrounds for the dark appearance, and consider using the semantic system colors for text and backgrounds to let the colors dynamically adapt to the current appearance. You can also support different appearances by putting color variants in your asset catalog. For guidance, see [Dark Mode](dark-mode.md); for developer guidance, see [Asset management](https://developer.apple.com/documentation/xcode/asset-management) and [Supporting Dark Mode in your interface](https://developer.apple.com/documentation/uikit/supporting-dark-mode-in-your-interface).

### Accented

**Group widget components into an accented and a primary group.**  The accented rendering mode divides the widget’s view hierarchy into an accent group and a primary group. On iPhone, iPad, and Mac, the system tints primary and accented content white. On Apple Watch, the system tints primary content white and accented content in the color of the watch face.

For developer guidance, see [widgetAccentable(_:)](https://developer.apple.com/documentation/swiftui/view/widgetaccentable(_:)) and [Optimizing your widget for accented rendering mode and Liquid Glass](https://developer.apple.com/documentation/widgetkit/optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass).

### Vibrant

**Offer enough contrast to ensure legibility.** In the vibrant rendering mode, the opacity of pixels within an image determines the strength of the blurred background material effect. Fully transparent pixels let the background material pass through as is. The brightness of pixels determines how vibrant they appear on the Lock Screen. Brighter gray values provide more contrast, and darker values provide less contrast.

**Create optimized assets for the best vibrant effect.** Render content like images, numbers, and text at full opacity. Use white or light gray for the most prominent content and darker grayscale values for secondary elements to establish hierarchy. Confirm that image content has sufficient contrast in grayscale, and use opaque grayscale values, rather than opacities of white, to achieve the best vibrant material effect.

## Previews and placeholders

**Design a realistic preview to display in the widget gallery.** Highlighting your widget’s capabilities — and clearly representing the experiences each widget type or size can provide — helps people make an informed decision. You can display real data in your widget preview, but if the data takes too long to generate or load, display realistic simulated data instead.

**Design placeholder content that helps people recognize your widget.** An installed widget displays placeholder content while its data loads. Create an effective placeholder appearance by combining static interface components with semi-opaque shapes that stand in for dynamic content. For example, use rectangles of different widths to suggest lines of text, and circles or squares in place of glyphs and images.

**Write a succinct widget description.** The widget gallery displays descriptions that help people understand what each widget does. Begin a description with an action verb — for example, “See the current weather conditions and forecast for a location” or “Keep track of your upcoming events and meetings.” Avoid including unnecessary phrases that reference the widget itself, like “This widget shows…,” “Use this widget to…,” or “Add this widget.” Use approachable language and [sentence-style capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64).

**Group your widget’s sizes together, and provide a single description.** If your widget is available in multiple sizes, group them together so people don’t think each size is a different widget. Provide a single description of your widget — regardless of how many sizes you offer — to avoid repetition and to help people understand how each size provides a slightly different perspective on the same content and functionality.

**Consider coloring the Add button.** After people choose your app in the widget gallery, an Add button appears below the group of widgets you offer. You can specify a color for this button to help remind people of your brand.

## Platform considerations

*No additional considerations for macOS. Not supported in tvOS.*

### Mobile (iOS, iPadOS)

Widgets on the Lock Screen are functionally similar to watch complications and follow design principles for Complications in addition to design principles for widgets. Provide useful information in your Lock Screen widget, and don’t treat it as an additional way for people to launch into your app. In many cases, a design for complications also works well for widgets on the Lock Screen (and vice versa), so consider creating them in tandem.

Your app can offer widgets on the Lock Screen in three different styles: as inline text that appears above the clock, and as circular and rectangular shapes that appear below the clock.

**Support the Always-On display on iPhone.** Devices with the Always-On display render widgets on the Lock Screen with reduced luminance. Use levels of gray that provide enough contrast in the Always-On display, and make sure your content remains legible.

For developer guidance, see [Creating accessory widgets and watch complications](https://developer.apple.com/documentation/widgetkit/creating-accessory-widgets-and-watch-complications).

**Offer Live Activities to show real-time updates.** Widgets don’t show real-time information. If your app allows people to track the progress of a task or event for a limited amount of time with frequent updates, consider offering Live Activities. Widgets and Live Activities use the same underlying frameworks and share design similarities. Develop widgets and Live Activities in tandem and reuse code and design components for both features. For design guidance on Live Activities, see [Live Activities](live-activities.md); for developer guidance, see [ActivityKit](https://developer.apple.com/documentation/activitykit).

#### StandBy and CarPlay

On iPhone in StandBy, the system displays two small system family widgets side-by-side, scaled up so they fill the Lock Screen. By supporting StandBy, you also ensure your widgets work well in CarPlay. CarPlay and StandBy widgets both use the small system family widget with the background removed and scaled up to best fit the grid on the Widgets screen. Glanceable information and large text are especially important in CarPlay to make your widget easy to read on a car’s display.

**Limit usage of rich images or color to convey meaning in StandBy.** Instead, make use of the additional space by scaling up and rearranging text so people can glance at the widget content from a greater distance. Mark your widget’s background as removable to ensure it can appear in StandBy. For developer guidance, see [Displaying the right widget background](https://developer.apple.com/documentation/widgetkit/displaying-the-right-widget-background).

*Illustrated: Correct usage, Incorrect usage.*

On iPhone in StandBy in low-light conditions, the system renders widgets in a monochromatic look with a red tint.

#### Apple HomeView

On Apple HomeView, people can place widgets on the Modular face and the Home Screen. Widgets on HomeView are from the small system family, and share the appearance of iPhone widgets. A person chooses widgets from among those already installed on HomeView, like Weather or World Clock, or from their individually connected iPad or iPhone.

- The Modular face can include up to four widgets, which can be from the iPhone devices of different household members. For example, if someone places a Calendar widget on the Modular face, that person’s calendar appears there for everyone. There is one Modular face per household.
- The Home Screen contains a personalized set of widgets and apps, which can include the defaults that come with HomeView along with those that a person chooses to display from their connected device. Each enrolled household member has their own personalized Home Screen.

## Specifications

As you design your widgets, use the following values for guidance.

### iOS dimensions

| Screen size (portrait, pt) | Small (pt) | Medium (pt) | Large (pt) | Circular (pt) | Rectangular (pt) | Inline (pt) |
| --- | --- | --- | --- | --- | --- | --- |
| 430×932 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |
| 428x926 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |
| 414x896 | 169x169 | 360x169 | 360x379 | 76x76 | 160x72 | 248x26 |
| 414x736 | 159x159 | 348x157 | 348x357 | 76x76 | 170x76 | 248x26 |
| 393x852 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |
| 390x844 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |
| 375x812 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |
| 375x667 | 148x148 | 321x148 | 321x324 | 68x68 | 153x68 | 225x26 |
| 360x780 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |
| 320x568 | 141x141 | 292x141 | 292x311 | N/A | N/A | N/A |

### iPadOS dimensions

| Screen size (portrait, pt) | Target | Small (pt) | Medium (pt) | Large (pt) | Extra large (pt) |
| --- | --- | --- | --- | --- | --- |
| 768x1024 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |
| 768x1024 | Device | 120x120 | 260x120 | 260x260 | 540x260 |
| 744x1133 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |
| 744x1133 | Device | 120x120 | 260x120 | 260x260 | 540x260 |
| 810x1080 | Canvas | 146x146 | 320.5x146 | 320.5x320.5 | 669x320.5 |
| 810x1080 | Device | 124x124 | 272x124 | 272x272 | 568x272 |
| 820x1180 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |
| 820x1180 | Device | 136x136 | 300x136 | 300x300 | 628x300 |
| 834x1112 | Canvas | 150x150 | 327.5x150 | 327.5x327.5 | 682x327.5 |
| 834x1112 | Device | 132x132 | 288x132 | 288x288 | 600x288 |
| 834x1194 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |
| 834x1194 | Device | 136x136 | 300x136 | 300x300 | 628x300 |
| 954x1373 * | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |
| 954x1373 * | Device | 162x162 | 350x162 | 350x350 | 726x350 |
| 970x1389 * | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |
| 970x1389 * | Device | 162x162 | 350x162 | 350x350 | 726x350 |
| 1024x1366 | Canvas | 170x170 | 378.5x170 | 378.5x378.5 | 795x378.5 |
| 1024x1366 | Device | 160x160 | 356x160 | 356x356 | 748x356 |
| 1192x1590 * | Canvas | 188x188 | 412x188 | 412x412 | 860x412 |
| 1192x1590 * | Device | 188x188 | 412x188 | 412x412 | 860x412 |

** When Display Zoom is set to More Space.*

## Change log

| Date | Changes |
| --- | --- |
| October 13, 2026 | Added guidance for Apple HomeView, and updated watchOS specifications. |
| December 16, 2025 | Updated guidance for all platforms, and added guidance for visionOS and CarPlay. |
| January 17, 2025 | Corrected watchOS widget dimensions. |
| June 10, 2024 | Updated to include guidance for accented widgets in iOS 18 and iPadOS 18. |
| June 5, 2023 | Updated guidance to include widgets in watchOS, widgets on the iPad Lock Screen, and updates for iOS 17, iPadOS 17, and macOS 14. |
| November 3, 2022 | Added guidance for widgets on the iPhone Lock Screen and updated design comprehensives for iPhone 14, iPhone 14 Pro, and iPhone 14 Pro Max. |

## Related guidelines

- [Layout](layout.md)

---
