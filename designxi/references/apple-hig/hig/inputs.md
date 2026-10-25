# Apple HIG — Inputs
Bundled HIG pages for the “Inputs” group. Each page kept verbatim under an anchor heading `## <slug>`. Cite as **inputs.md › <slug> › heading**.


<a id="apple-pencil-and-scribble"></a>
## apple-pencil-and-scribble

# Apple Pencil and Scribble

> Source: <https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble>
> Section: Inputs
> Platforms covered: iPadOS
> Last change on Apple's site: 2024-05-07 (Added guidance for handling squeeze and barrel roll on Apple Pencil Pro.)

Apple Pencil helps make drawing, handwriting, and marking effortless and natural, in addition to performing well as a pointer and UI interaction tool.

---

Apple Pencil is a versatile, intuitive tool for iPad apps that offers pixel‑level precision when jotting notes, sketching, painting, marking up documents, and more. Scribble lets people use Apple Pencil to enter text in any text field through fast, private, on-device handwriting recognition.

For details on Apple Pencil features and compatibility, see [Apple Pencil](https://www.apple.com/apple-pencil/).

## Best practices

**Support behaviors people intuitively expect when using a marking instrument.** Most people have a lot of experience with real-world marking tools, and this knowledge informs their expectations when they use Apple Pencil with your app. To provide a delightful experience, think about the ways people interact with nondigital pencils, pens, and other marking instruments, and proactively support actions that people may naturally attempt. For example, people often want to write in the margins of documents or books.

**Let people choose when to switch between Apple Pencil and finger input.** For example, if your app supports Apple Pencil for marking, also ensure that your app’s controls respond to Apple Pencil so people don’t have to switch to using their finger to activate them. In this scenario, a control that doesn’t support Apple Pencil input might seem to be unresponsive, giving the impression of a malfunction or low battery. (Scribble only supports Apple Pencil input.)

**Let people make a mark the moment Apple Pencil touches the screen**. You want the experience of putting Apple Pencil to screen to mirror the experience of putting a classic pencil to paper, so it’s essential to avoid requiring people to tap a button or enter a special mode before they can make a mark.

**Help people express themselves by responding to the way they use Apple Pencil.** Apple Pencil may sense tilt (altitude), force (pressure), orientation (azimuth), and [barrel roll](#barrel-roll). Use this information to affect the strokes Apple Pencil makes, such as by varying thickness and intensity. When responding to pressure, keep things simple and intuitive. For example, it feels natural to affect continuous properties — such as ink opacity or brush size — by varying the pressure.

**Provide visual feedback to indicate a direct connection with content.** Make sure Apple Pencil appears to directly and immediately manipulate content it touches onscreen. Avoid letting Apple Pencil appear to initiate seemingly disconnected actions, or affect content on other parts of the screen.

**Design a great left- and right-handed experience.** Avoid placing controls in locations that may be obscured by either hand. If there’s a chance controls may become obscured, consider letting people reposition them.

## Hover

**Use hover to help people predict what will happen when Apple Pencil touches the screen.** For example, as people hold Apple Pencil above the screen, a hover preview can show the dimensions and color of the mark that the current tool can make. As much as possible, avoid continuously modifying the preview as people move Apple Pencil closer or farther from the screen. A preview that changes according to height is unlikely to clarify the mark Apple Pencil will make, and frequent visual variations can be very distracting to people.

**Avoid using hover to initiate an action.** Unlike tapping a button or marking the screen, hovering is a relatively imprecise motion that doesn’t require people to think about the actual distance between Apple Pencil and the display. You don’t want people to inadvertently perform an action — especially a destructive action that they might want to undo — just because they hold Apple Pencil near the screen.

**Prefer showing a preview value that’s near the middle in a range of dynamic values.** Dynamic properties like opacity or flow can be difficult to depict at the highest or lowest ends of the spectrum. For example, previewing the appearance of a brush mark made with the maximum pressure could occlude the area in which people are marking; in contrast, depicting a mark made with the minimum pressure could be hard for people to detect, making the preview an inaccurate representation of an actual mark or even invisible.

**Consider using hover to support relevant interactions close to where people are marking.** For example, you might respond to hover by displaying a contextual menu of tool sizes when people perform a gesture like [squeeze](#squeeze) or press a modifier key on an attached keyboard. Revealing a menu near where people are marking lets them make choices without moving Apple Pencil or their hands to another part of the screen.

**Prefer showing hover previews for Apple Pencil, not for a pointing device.** Although a pointing device can also respond to hover gestures, it might be confusing to provide the same visual feedback for both devices. If it makes sense in your app, you can restrict your hover preview to Apple Pencil only. For developer guidance, see [Adopting hover support for Apple Pencil](https://developer.apple.com/documentation/uikit/adopting-hover-support-for-apple-pencil).

## Double tap

**Respect people’s settings for the double-tap gesture when they make sense in your app.** By default, models of Apple Pencil that support the double-tap gesture respond by toggling between the current tool and the eraser, but people can set the gesture to toggle between the current and previous tool, show and hide the color picker, or do nothing at all. If your app supports these behaviors, let people use their preferred gestures to perform them. If the systemwide double-tap settings don’t make sense in your app, you can still use the gesture to change the interaction mode. For example, a 3D app that offers a mesh-editing tool could use double tap to toggle between the tool’s raise and lower modes.

**Give people a way to specify custom double-tap behavior if necessary.** If you offer custom double-tap behavior in addition to some or all of the default behaviors, provide a control that lets people choose the custom behavior mode. People need to know which mode they’re in; otherwise, they may get confused when your app responds differently to their interactions. In this scenario, make sure it’s easy for people to discover the custom behavior your app supports, but don’t turn it on by default.

**Avoid using the double-tap gesture to perform an action that modifies content.** In rare cases, it’s possible for people to double-tap accidentally, which means that they may not even be aware that your app has performed the action. Prefer using double tap to perform actions that are easy for people to undo. In particular, avoid using double tap to perform a potentially destructive action that might result in data loss.

## Squeeze

Using Apple Pencil Pro, people can squeeze to perform an action. You can design a custom behavior that responds to squeeze, but recognize that people may choose to configure the squeeze gesture to run an [App Shortcut](app-shortcuts.md) instead of app-specific actions.

> **Note:** The squeeze gesture is available only when the paired iPad screen is on and while the Apple Pencil Pro is not directly contacting it. Because squeeze works when there’s distance between Apple Pencil Pro and iPad, people might not always be visually aware of the gesture’s onscreen result.

**Treat squeeze as a single, quick gesture that performs a discrete — not continuous — action.** People sometimes squeeze with a lot of force, so holding a squeeze or squeezing several times quickly can be tiring. Help people remain comfortable by responding to a single squeeze and promptly displaying the result.

**If you use squeeze to reveal app UI, like a contextual menu, display it close to Apple Pencil Pro.** Displaying the result of a squeeze near the tip of Apple Pencil Pro strengthens the connection between the device and the gesture, and can help people stay engaged with their task.

**Define squeeze actions that are nondestructive and easy to undo.** As with the double-tap gesture, people can make the squeeze gesture without meaning to, so it’s essential to avoid using squeeze to perform an action that could result in data loss.

## Barrel roll

While marking with Apple Pencil Pro, people can use a barrel-roll gesture to change the type of mark they’re making. For example, while using Apple Pencil Pro to highlight content in Notes, people can barrel-roll to rotate the angle of the mark.

**Use barrel roll only to modify marking behavior, not to enable navigation or display other controls.** In contrast to double tap and squeeze, barrel roll is naturally related to marking and doesn’t make sense for performing an interface action.

## Scribble

With Scribble and Apple Pencil, people can simply write wherever text is accepted in your app — they don’t have to tap or switch modes first. Because Scribble is fully integrated into iPadOS, it’s available to all apps by default.

**Make text entry feel fluid and effortless.** By default, Scribble works in all standard text components — such as text fields, text views, search fields, and editable fields in web content — except password fields. If you use a custom text field in your app, avoid making people tap or select it before they can begin writing.

**Make Scribble available everywhere people might want to enter text.** Unlike using the keyboard, using Apple Pencil encourages people to treat the screen the way they treat a sheet of paper. Help strengthen this perception in your app by making Scribble consistently available in places where text entry seems natural. For example, in Reminders, it’s natural for people to create a new reminder by writing it in the blank space below the last item, even though the area doesn’t contain a text field. For developer guidance, see [UIIndirectScribbleInteraction](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteraction-1nfjm).

**Avoid distracting people while they write.** Some text field behaviors work well for keyboard input, but can disrupt the natural writing experience that Apple Pencil provides. For example, it’s best to avoid displaying autocompletion text as people write in a text field because the suggestions can visually interfere with their writing. It’s also a good idea to hide a field’s placeholder text the moment people begin to write so that their input doesn’t appear to overlap it.

**While people are writing in a text field, make sure it remains stationary.** In some cases, it can make sense to move a text field when it becomes focused: for example, a search field might move to make more room to display results. Such a movement is fine when people are using the keyboard, but when they’re writing it can make them feel like they’ve lost control of where their input is going. If you can’t prevent a text field from moving or resizing, consider delaying the change until people pause their writing.

**Prevent autoscrolling text while people are writing and editing in a text field.** When transcribed text autoscrolls, people might try to avoid writing on top of it. Worse, if text scrolls while people are using Apple Pencil to select it, they might select a different range of text than they want.

**Give people enough space to write.** A small text field can feel uncomfortable to write in. When you know that Apple Pencil input is likely, improve the writing experience in your app by increasing the size of the text field before people begin to write in it or when they pause writing; avoid resizing a text field while people are writing. For developer guidance, see [UIScribbleInteraction](https://developer.apple.com/documentation/uikit/uiscribbleinteraction).

## Custom drawing

Using [PencilKit](https://developer.apple.com/documentation/pencilkit), you can let people take notes, annotate documents and images, and draw with the same low-latency experience that iOS provides. PencilKit also makes it easy to create a custom drawing canvas in your app and offer a state-of-the-art tool picker and ink palette.

**Help people draw on top of existing content.** By default, the colors on your PencilKit canvas dynamically adjust to Dark Mode, so people can create content in either mode and the results will look great in both. However, when people draw on top of existing content like a PDF or a photo, you want to prevent the dynamic adjustment of colors so that the markup remains sharp and visible.

**Consider displaying custom undo and redo buttons when your app runs in a compact environment.** In a regular environment, the tool picker includes undo and redo buttons, but in a compact environment it doesn’t. In a compact environment, you could display undo and redo buttons in a toolbar. You might also consider supporting the standard 3-finger undo/redo gesture, so people can use it in any environment. For guidance, see [Undo and redo](undo-and-redo.md).

## Platform considerations

*Not supported in iOS, macOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| May 7, 2024 | Added guidance for handling squeeze and barrel roll on Apple Pencil Pro. |
| September 12, 2023 | Updated artwork. |
| November 3, 2022 | Added guidelines for using hover to enhance your app. |

## Related guidelines

- [Entering data](entering-data.md)

---


<a id="focus-and-selection"></a>
## focus-and-selection

# Focus and selection

> Source: <https://developer.apple.com/design/human-interface-guidelines/focus-and-selection>
> Section: Inputs
> Platforms covered: iPadOS, macOS (guidance specific to tvOS, visionOS omitted)
> Last change on Apple's site: 2023-10-24 (Clarified the difference between focus effects and the visionOS hover effect.)

Focus helps people visually confirm the object that their interaction targets.

---

Focus supports simplified, component-based navigation. Using inputs like a remote, game controller, or keyboard, people bring focus to the components they want to interact with.

In many cases, focusing an item also selects it. The exception is when automatic selection might cause a distracting context shift, like opening a new view. In tvOS, for example, people use the remote to move focus from item to item as they seek the one they want, but because selecting a focused item opens or activates it, selection requires a separate gesture.

Different platforms communicate focus in different ways. For example, iPadOS and macOS show focus by drawing a ring around an item or highlighting it; tvOS generally uses the [parallax effect](images.md) to give the focused item an appearance of depth and liveliness. The combination of focus effects and interactions is sometimes called a *focus system* or *focus model*.

## Best practices

**Rely on system-provided focus effects.** System-defined focus effects are precisely tuned to complement interactions with Apple devices, providing experiences that feel responsive, fluid, and lifelike. Incorporating system-provided focus behaviors gives your app consistency and predictability, helping people understand it quickly. Consider creating custom focus effects only if it’s absolutely necessary.

**Avoid changing focus without people’s interaction.** People rely on the focus system to help them know where they are in your app. If you change focus without their interaction, people have to spend time finding the newly focused item, delaying their current task. The exception is when people are moving focus using an input device that lets them make discrete, directional movements — like a keyboard, remote, or game controller — and a previously focused item disappears. In this scenario, there are only a small number of items within one discrete step of the previously focused item, so moving focus to one of these remaining items ensures that the focus indicator is in a location people can easily find. When people aren’t moving focus by using such an input device, you can’t predict the item they’ll target next, so it’s generally best to simply hide the focus indicator when the focused object disappears.

**Be consistent with the platform as you help people bring focus to items in your app.** For example, in iPadOS and macOS, a full keyboard access mode helps people use the keyboard to reach every control, so you only need to support focus for content elements like list items, text fields, and search fields, and not for controls like buttons, sliders, and toggles. In contrast, tvOS users rely on using directional gestures on a remote or game controller (or pressing the arrow keys on an attached keyboard) to reach every onscreen element, so you need to make sure that people can bring focus to every element in your app.

**Indicate focus using visual appearances that are consistent with the platform.** For example, consider a window that contains a list of items. In iPadOS and macOS, the system draws focused list items using white text and a background highlight that matches the app’s accent color, drawing unfocused items using the standard text color and a gray background highlight (for developer guidance, see [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview) and [NSTableView](https://developer.apple.com/documentation/appkit/nstableview)).

**In general, use a focus ring for a text or search field, but use a highlight in a list or collection.** Although you can use a focus ring to draw attention to an item that fills a cell, like a photo, it’s usually easier for people to view lists and collections when an entire row is highlighted.

## Platform considerations

*Not supported in iOS or watchOS.*

### Tablet (iPadOS)

iPadOS 15 and later defines a focus system that supports keyboard interactions for navigating text fields, text views, and sidebars, in addition to various types of collection views and other custom views in your app.

The iPadOS and tvOS focus systems are similar. People perform actions by moving a focus indicator to an item and then selecting it (for guidance, see tvOS). Although the underlying system is the same, the user experiences are a little different. tvOS uses *directional focus*, which means people can use the same interaction — that is, swiping the Siri Remote or using only the arrow keys on a connected keyboard — to navigate to every onscreen component. In contrast, iPadOS defines *focus groups*, which represent specific areas within an app, like a sidebar, grid, or list. Using focus groups, iPadOS can support two different keyboard interactions.

- Pressing the Tab key moves focus among focus groups, letting people navigate to sidebars, grids, and other app areas.
- Pressing an arrow key supports a directional focus interaction that’s similar to tvOS, but limited to navigation among items in the same focus group. For example, people can use an arrow key to move through the items in a list or a sidebar.

Onscreen components can indicate focus by using the halo effect or the highlighted appearance.

The *halo* focus effect — also known as the *focus ring* — displays a customizable outline around the component. You can apply the halo effect to custom views and to fully opaque content within a collection or list cell, such as an image.

**Customize the halo focus effect when necessary.** By default, the system uses an item’s shape to infer the shape of its halo. If the system-provided halo doesn’t give you the appearance you want, you can refine it to match contours like rounded corners or shapes defined by Bézier paths. You can also adjust a halo’s position if another component occludes or clips it. For example, you might need to ensure that a badge appears above the halo or that a parent view doesn’t clip it. For developer guidance, see [UIFocusHaloEffect](https://developer.apple.com/documentation/uikit/uifocushaloeffect).

The *highlighted* appearance — in which the component’s text uses the app’s accent color — also indicates focus, but it’s not a focus effect. The highlight appearance occurs automatically when people select a collection view cell on which you’ve set content configurations (for developer guidance, see [UICollectionViewCell](https://developer.apple.com/documentation/uikit/uicollectionviewcell)).

**Ensure that focus moves through your custom views in ways that make sense.** As people continue pressing the Tab key, focus moves through focus groups in reading order: leading to trailing, and top to bottom. Although focus moves through system-provided views in ways that people expect, you might need to adjust the order in which the focus system visits your custom views. For example, if you want focus to move down through a vertical stack of custom views before it moves in the trailing direction to the next view, you need to identify the stack container as a single focus group. For developer guidance, see [focusGroupIdentifier](https://developer.apple.com/documentation/uikit/uifocusenvironment/focusgroupidentifier).

**Adjust the priority of an item to reflect its importance within a focus group.** When a group receives focus, its *primary item* automatically receives focus too, making it easy for people to select the item they’re most likely to want. You can make an item primary by increasing its priority. For developer guidance, see [UIFocusGroupPriority](https://developer.apple.com/documentation/uikit/uifocusgrouppriority).

## Change log

| Date | Changes |
| --- | --- |
| October 24, 2023 | Clarified the difference between focus effects and the visionOS hover effect. |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [Keyboards](keyboards.md)

---


<a id="game-controls"></a>
## game-controls

# Game controls

> Source: <https://developer.apple.com/design/human-interface-guidelines/game-controls>
> Section: Inputs
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS omitted)
> Last change on Apple's site: 2025-06-09 (Updated touch control best practices, updated game controller mapping for UI, and added guidance for spatial game controller support in visionOS.)

Precise, intuitive game controls enhance gameplay and can increase a player’s immersion in the game.

---

On Apple platforms, a game can support input from physical game controllers or default system interactions, like touch, a remote, or a mouse and keyboard. Players might prefer to use physical game controllers, but there are two important reasons to also support a platform’s default interaction methods:

- Even though all platforms except watchOS support physical game controllers, not every player might have access to one.
- Players appreciate games that let them use the platform interaction method they’re most familiar with.

To reach the widest audience and provide the best experience for each platform, keep these factors in mind when choosing the input methods to support.

## Touch controls

For iOS and iPadOS games, supporting touch interaction means that you can provide virtual controls on top of game content while also letting players interact with game elements by touching them directly. You can use the [Touch Controller](https://developer.apple.com/documentation/touchcontroller) framework to add these virtual controls to your game. Keep the following guidelines in mind to create an enjoyable touch control experience.

**Determine whether it makes sense to display virtual controls on top of game content.** In general, virtual game controls benefit games that offer a large number of actions or require players to control movement. However, sometimes gameplay is more immersive and effective when players can interact directly with in-game objects. Look for opportunities to reduce the amount of virtual controls that overlap your game content by associating actions with in-game gestures instead. For example, consider letting players tap objects to select them instead of adding a virtual selection button.

**Place virtual buttons where they’re easy to access.** Take into account the device’s boundaries and [safe areas](layout.md#guides-and-safe-areas) as well as comfortable locations for controls. Make sure to position buttons where they don’t overlap system features like the Home indicator or Dynamic Island on iPhone. Place frequently used buttons near a player’s thumb, avoiding the circular regions where players expect movement and camera input to happen. Place secondary controls, like menus, at the top of the screen.

**Make sure controls are large enough.** Make sure frequently used controls are a minimum size of 44x44 pt, and less important controls, such as menus, are a minimum size of 28x28 pt to accommodate people’s fingers.

**Always include visible and tactile press states.** A virtual control feels unresponsive without a visual and physical press state. Help players understand when they successfully interact with a button by adding a visual press state effect, such as a glow, that they can see even when their finger is covering the control. Combine this press state with sound and haptics to enhance the feeling of feedback. For guidance, see [Playing haptics](playing-haptics.md).

**Use symbols that communicate the actions they perform.** Choose artwork that visually represents the action each button performs, such as a graphic of a weapon to represent an attack. Avoid using abstract shapes or controller-based naming like A, X, or R1 as artwork, which makes it harder for players to understand and remember what specific controls do.

**Show and hide virtual controls to reflect gameplay.** Take advantage of the dynamic nature of touch controls and adapt what controls players see onscreen depending on their context. You can hide controls when an action isn’t available or relevant, letting you reduce clutter and help players concentrate on what’s important. For example, consider hiding movement controls until a player touches the screen to reduce the amount of UI overlapping your game content.

*Illustrated: Visible control, Hidden control.*

**Combine functionality into a single control.** Consider redesigning game mechanics that require players to press multiple buttons at the same time or in a sequence. Leverage gestures such as double tap and touch and hold to provide different variations of the same action, such as touch and hold to use a special powered up version of an attack. For multiple actions, such as walking or sprinting, consider combining the actions into a single control.

**Map movement and camera controls to predictable behavior.** Typically, players expect to control movement using the left side of their screen, and control camera direction using the right side of their screen. Maximize the amount of space that players can control both movement and the camera direction by using as large of an input area as possible. For movement control, opt to show a virtual thumbstick wherever the player lands their thumb instead of a static thumbstick position. For camera control, opt to use direct touch to pan the camera instead of a virtual thumbstick.

## Physical controllers

**Support the platform’s default interaction method.** A game controller is an optional purchase, but every iPhone and iPad has a touchscreen, every Mac has a keyboard and a trackpad or mouse, every Apple TV has a remote, and every Apple Vision Pro responds to gestures people make with their eyes and hands. If you support game controllers, try to make sure there’s a fallback for using the platform’s default interaction method. For developer guidance, see [Adding virtual controls to games that support game controllers in iOS](https://developer.apple.com/documentation/gamecontroller/adding-virtual-controls-to-games-that-support-game-controllers-in-ios).

**Tell people about game controller requirements.** In tvOS and visionOS, you can require the use of a physical game controller. The App Store displays a “Game Controller Required” badge to help people identify such apps. Remember that people can open your game at any time, even without a connected controller. If your app requires a game controller, check for its presence and gracefully prompt people to connect one. For developer guidance, see [GCRequiresControllerUserInteraction](https://developer.apple.com/documentation/bundleresources/information-property-list/gcrequirescontrolleruserinteraction).

**Automatically detect whether a controller is paired.** Instead of having players manually set up a physical game controller, you can automatically detect whether a controller is paired and get its profile. For developer documentation, see [Game Controller](https://developer.apple.com/documentation/gamecontroller).

**Customize onscreen content to match the connected game controller.** To simplify your game’s code, the Game Controller framework assigns standard names to controller elements based on their placement, but the colors and symbols on an actual game controller may differ. Be sure to use the connected controller’s labeling scheme when referring to controls or displaying related content in your interface. For developer guidance, see [GCControllerElement](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement).

**Map controller buttons to expected UI behavior.** Outside of gameplay, players expect to navigate your game’s UI in a way that matches the familiar behavior of the platform they’re playing on. When not controlling gameplay, follow these conventions across all Apple platforms:

| Button | Expected behavior for UI |
| --- | --- |
| A | Activates a control |
| B | Cancels an action or returns to previous screen |
| X | — |
| Y | — |
| Left shoulder | Navigates left to a different screen or section |
| Right shoulder | Navigates right to a different screen or section |
| Left trigger | — |
| Right trigger | — |
| Left/right thumbstick | Moves selection |
| Directional pad | Moves selection |
| Home/logo | Reserved for system controls |
| Menu | Opens game settings or pauses gameplay |

**Support multiple connected controllers.** If there are multiple controllers connected, use labels and glyphs that match the one that the player is actively using. If your game supports multiplayer, use the appropriate labels and symbols when referring to a specific player’s controller. If you need to refer to buttons on multiple controllers, consider listing them together.

**Prefer using symbols, not text, to refer to game controller elements.** The Game Controller framework makes [SF Symbols](sf-symbols.md) available for most elements, including the buttons on various brands of game controllers. Using symbols instead of text descriptions can be especially helpful for players who aren’t experienced with controllers because it doesn’t require them to hunt for a specific button label during gameplay.

## Keyboards

Keyboard players appreciate using keyboard bindings to speed up their interactions with apps and games.

**Prioritize single-key commands.** Single-key commands are generally easier and faster for players to perform, especially while they’re simultaneously using a mouse or trackpad. For example, you might use the first letter of a menu item as a shortcut, such as I for Inventory or M for Map; you might also map the game’s main action to the Space bar, taking advantage of the key’s relatively large size.

**Test key binding comfort game using an Apple keyboard.** For example, if a key binding uses the Control key (^) on a non-Apple keyboard, consider remapping it to the Command key (⌘) on an Apple keyboard. On Apple keyboards, the Command key is conveniently located next to the Space bar, making it especially easy to reach when players are using the W, A, S, and D keys.

**Take the proximity of keys into account.** For example, if players navigate using the W, A, S, and D keys, consider using nearby keys to define other high-value commands. Similarly, if there’s a group of closely related actions, it can work well to map their bindings to keys that are physically close together, such as using the number keys for inventory categories.

**Let players customize key bindings.** Although players tend to expect a reasonable set of defaults, many people need to customize a game’s key bindings for personal comfort and play style.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, or tvOS. Not supported in watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| June 9, 2025 | Updated touch control best practices, updated game controller mapping for UI, and added guidance for spatial game controller support in visionOS. |
| June 10, 2024 | Added guidance for supporting touch controls and changed title from Game controllers. |

## Related guidelines

- [Designing for games](designing-for-games.md)
- [Gestures](gestures.md)
- [Keyboards](keyboards.md)
- [Playing haptics](playing-haptics.md)

---


<a id="gestures"></a>
## gestures

# Gestures

> Source: <https://developer.apple.com/design/human-interface-guidelines/gestures>
> Section: Inputs
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2024-09-09 (Added guidance for working with system overlays in visionOS and made organizational updates.)

A gesture is a physical motion that a person uses to directly affect an object in an app or game on their device.

---

Depending on the device they’re using, people can make gestures on a touchscreen, in the air, or on a range of input devices such as a trackpad, mouse, remote, or game controller that includes a touch surface.

Every platform supports basic gestures like tap, swipe, and drag. Although the precise movements that make up basic gestures can vary per platform and input device, people are familiar with the underlying functionality of these gestures and expect to use them everywhere. For a list of these gestures, see [Standard gestures](#standard-gestures).

## Best practices

**Give people more than one way to interact with your app.** People commonly prefer or need to use other inputs — such as their voice, keyboard, or Switch Control — to interact with their devices. Don’t assume that people can use a specific gesture to perform a given task. For guidance, see [Accessibility](accessibility.md).

**In general, respond to gestures in ways that are consistent with people’s expectations.** People expect most gestures to work the same regardless of their current context. For example, people expect tap to activate or select an object. Avoid using a familiar gesture like tap or swipe to perform an action that’s unique to your app; similarly, avoid creating a unique gesture to perform a standard action like activating a button or scrolling a long view.

**Handle gestures as responsively as possible.** Useful gestures enhance the experience of direct manipulation and provide immediate feedback. As people perform a gesture in your app, provide feedback that helps them predict its results and, if necessary, communicates the extent and type of movement required to complete the action.

**Indicate when a gesture isn’t available.** If you don’t clearly communicate why a gesture doesn’t work, people might think your app has frozen or they aren’t performing the gesture correctly, leading to frustration. For example, if someone tries to drag a locked object, the UI may not indicate that the object’s position has been locked; or if they try to activate an unavailable button, the button’s unavailable state may not be clearly distinct from its available state.

## Custom gestures

**Add custom gestures only when necessary.** Custom gestures work best when you design them for specialized tasks that people perform frequently and that aren’t covered by existing gestures, like in a game or drawing app. If you decide to implement a custom gesture, make sure it’s:

- Discoverable
- Straightforward to perform
- Distinct from other gestures
- Not the only way to perform an important action in your app or game

**Make custom gestures easy to learn.** Offer moments in your app to help people quickly learn and perform custom gestures, and make sure to test your interactions in real use scenarios. If you’re finding it difficult to use simple language and graphics to describe a gesture, it may mean people will find the gesture difficult to learn and perform.

**Use shortcut gestures to supplement standard gestures, not replace them.** While you may supply a custom gesture to quickly access parts of your app, people also need simple, familiar ways to navigate and perform actions, even if it means an extra tap or two. For example, in an app that supports navigation through a hierarchy of views, people expect to find a Back button in a top toolbar that lets them return to the previous view with a single tap. To help accelerate this action, many apps also offer a shortcut gesture — such as swiping from the side of a window or touchscreen — while continuing to provide the Back button.

**Avoid conflicting with gestures that access system UI.** Several platforms offer gestures for accessing system behaviors, like edge swiping in watchOS or rolling your hand over to access system overlays in visionOS. It’s important to avoid defining custom gestures that might conflict with these interactions, as people expect these controls to work consistently. In specific circumstances within games or immersive experiences, developers can work around this area by deferring the system gesture. For more information, see the platform considerations for iOS, iPadOS, watchOS, and visionOS.

## Platform considerations

### Mobile (iOS, iPadOS)

In addition to the [standard gestures](#standard-gestures) supported in all platforms, iOS and iPadOS support a few other gestures that people expect.

| Gesture | Common action |
| --- | --- |
| Three-finger swipe | Initiate undo (left swipe); initiate redo (right swipe). |
| Three-finger pinch | Copy selected text (pinch in); paste copied text (pinch out). |
| Four-finger swipe (iPadOS only) | Switch between apps. |
| Shake | Initiate undo; initiate redo. |

**Consider allowing simultaneous recognition of multiple gestures if it enhances the experience.** Although simultaneous gestures are unlikely to be useful in nongame apps, a game might include multiple onscreen controls — such as a joystick and firing buttons — that people can operate at the same time. For guidance on integrating touchscreen input with Apple Pencil input in your iPadOS app, see [Apple Pencil and Scribble](apple-pencil-and-scribble.md).

### Desktop (macOS)

People primarily interact with macOS using a [keyboard](keyboards.md) and mouse. In addition, they can make [standard gestures](#standard-gestures) on a Magic Trackpad, Magic Mouse, or a [game controller](game-controls.md) that includes a touch surface.

## Specifications

### Standard gestures

The system provides APIs that support the familiar gestures people use with their devices, whether they use a touchscreen, an indirect gesture in visionOS, or an input device like a trackpad, mouse, remote, or game controller. For developer guidance, see [Gestures](https://developer.apple.com/documentation/swiftui/gestures).

| Gesture | Supported in | Common action |
| --- | --- | --- |
| Tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Activate a control; select an item. |
| Swipe | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Reveal actions and controls; dismiss views; scroll. |
| Drag | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Move a UI element. |
| Touch (or pinch) and hold | iOS, iPadOS, tvOS, visionOS, watchOS | Reveal additional controls or functionality. |
| Double tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Zoom in; zoom out if already zoomed in; perform a primary action on Apple Watch Series 9 and Apple Watch Ultra 2. |
| Zoom | iOS, iPadOS, macOS, tvOS, visionOS | Zoom a view; magnify content. |
| Rotate | iOS, iPadOS, macOS, tvOS, visionOS | Rotate a selected item. |

For guidance on supporting additional gestures and button presses on specific input devices, see [Pointing devices](pointing-devices.md), Remotes, and [Game controls](game-controls.md).

## Change log

| Date | Changes |
| --- | --- |
| September 9, 2024 | Added guidance for working with system overlays in visionOS and made organizational updates. |
| September 15, 2023 | Updated specifications to include double tap in watchOS. |
| June 21, 2023 | Changed page title from Touchscreen gestures and updated to include guidance for visionOS. |

## Related guidelines

- [Feedback](feedback.md)
- [Playing haptics](playing-haptics.md)

---


<a id="gyro-and-accelerometer"></a>
## gyro-and-accelerometer

# Gyroscope and accelerometer

> Source: <https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer>
> Section: Inputs
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)

On-device gyroscopes and accelerometers can supply data about a device’s movement in the physical world.

---

You can use accelerometer and gyroscope data to provide experiences based on real-time, motion-based information in apps and games that run in iOS, iPadOS, and watchOS. tvOS apps can use gyroscope data from the Siri Remote. For developer guidance, see [Core Motion](https://developer.apple.com/documentation/coremotion).

## Best practices

**Use motion data only to offer a tangible benefit to people.** For example, a fitness app might use the data to provide feedback about people’s activity and general health, and a game might use the data to enhance gameplay. Avoid gathering data simply to have the data.

> **Important:** If your experience needs to access motion data from a device, you must provide copy that explains why. The first time your app or game tries to access this type of data, the system includes your copy in a permission request, where people can grant or deny access.

**Outside of active gameplay, avoid using accelerometers or gyroscopes for the direct manipulation of your interface.** Some motion-based gestures may be difficult to replicate precisely, may be physically challenging for some people to perform, and may affect battery usage.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Related guidelines

- [Feedback](feedback.md)

---


<a id="keyboards"></a>
## keyboards

# Keyboards

> Source: <https://developer.apple.com/design/human-interface-guidelines/keyboards>
> Section: Inputs
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS omitted)
> Last change on Apple's site: 2025-06-09 (Moved game-specific key bindings guidance to the Game controls page.)

A physical keyboard can be an essential input device for entering text, playing games, controlling apps, and more.

---

People can connect a physical keyboard to any device except Apple Watch. Mac users tend to use a physical keyboard all the time and iPad users often do. Many games work well with a physical keyboard, and people can prefer using one instead of a [virtual keyboard](virtual-keyboards.md) when entering a lot of text.

Keyboard users often appreciate using keyboard shortcuts to speed up their interactions with apps and games. A *keyboard shortcut* is a combination of a primary key and one or more modifier keys (Control, Option, Shift, and Command) that map to a specific command. A keyboard shortcut in a game — called a *key binding* — often consists of a single key.

Apple defines standard keyboard shortcuts to work consistently across the system and most apps, helping people transfer their knowledge to new experiences. Some apps define custom keyboard shortcuts for the app-specific commands people use most; most games define custom key bindings that make it quick and efficient to use the keyboard to control the game. For guidance, see [Game controls](game-controls.md#keyboards).

## Best practices

**Support Full Keyboard Access when possible.** Available in iOS, iPadOS, macOS, and visionOS, Full Keyboard Access lets people navigate and activate windows, menus, controls, and system features using only the keyboard. To test Full Keyboard Access in your app or game, turn it on in the Accessibility area of the system-supplied Settings app. For developer guidance, see [Support Full Keyboard Access in your iOS app](https://developer.apple.com/videos/play/wwdc2021/10120/) and [isFullKeyboardAccessEnabled](https://developer.apple.com/documentation/appkit/nsapplication/isfullkeyboardaccessenabled).

> **Important:** Although iPadOS supports keyboard navigation in text fields, text views, and sidebars, and provides APIs you can use to support it in collection views and other custom views, avoid supporting keyboard navigation for controls, such as buttons, segmented controls, and switches. Instead, let people use Full Keyboard Access to activate controls, navigate to all onscreen components, and perform gesture-based interactions like drag and drop. For guidance, see [iPadOS](focus-and-selection.md#tablet-ipados); for developer guidance, see [Focus-based navigation](https://developer.apple.com/documentation/uikit/focus-based_navigation).

**Respect standard keyboard shortcuts.** While using most apps, people generally expect to rely on the standard keyboard shortcuts that work in other apps and throughout the system. If your app offers a unique action that people perform frequently, prefer creating a [custom](#custom-keyboard-shortcuts) shortcut for it instead of repurposing a standard one that people associate with a different action. While playing a game, people may expect to use certain standard keyboard shortcuts — such as Command–Q to quit the game — but they also expect to be able to modify each game’s key bindings to fit their personal play style. For guidance, see [Game controls](game-controls.md#keyboards).

## Standard keyboard shortcuts

**In general, don’t repurpose standard keyboard shortcuts for custom actions.** People can get confused when the shortcuts they know work differently in your app or game. Only consider redefining a standard shortcut if its action doesn’t make sense in your experience. For example, if your app doesn’t support text editing, it doesn’t need a text-styling command like Italic, so you might repurpose Command–I for an action that has more relevance, like Get Info.

People expect each of the following standard keyboard shortcuts to perform the action listed in the table below.

| Primary key | Keyboard shortcut | Action |
| --- | --- | --- |
| Space | Command-Space | Show or hide the Spotlight search field. |
|  | Shift-Command-Space | Varies. |
|  | Option-Command-Space | Show the Spotlight search results window. |
|  | Control-Command-Space | Show the Special Characters window. |
| Tab | Shift-Tab | Navigate through controls in a reverse direction. |
|  | Command-Tab | Move forward to the next most recently used app in a list of open apps. |
|  | Shift-Command-Tab | Move backward through a list of open apps (sorted by recent use). |
|  | Control-Tab | Move focus to the next group of controls in a dialog or the next table (when Tab moves to the next cell). |
|  | Control-Shift-Tab | Move focus to the previous group of controls. |
| Esc | Esc | Cancel the current action or process. |
| Esc | Option-Command-Esc | Open the Force Quit dialog. |
| Eject | Control-Command-Eject | Quit all apps (after changes have been saved to open documents) and restart the computer. |
|  | Control-Option-Command-Eject | Quit all apps (after changes have been saved to open documents) and shut the computer down. |
| F1 | Control-F1 | Toggle full keyboard access on or off. |
| F2 | Control-F2 | Move focus to the menu bar. |
| F3 | Control- F3 | Move focus to the Dock. |
| F4 | Control-F4 | Move focus to the active (or next) window. |
|  | Control-Shift-F4 | Move focus to the previously active window. |
| F5 | Control-F5 | Move focus to the toolbar. |
|  | Command-F5 | Turn VoiceOver on or off. |
| F6 | Control-F6 | Move focus to the first (or next) panel. |
|  | Control-Shift-F6 | Move focus to the previous panel. |
| F7 | Control-F7 | Temporarily override the current keyboard access mode in windows and dialogs. |
| F8 |  | Varies. |
| F9 |  | Varies. |
| F10 |  | Varies. |
| F11 |  | Show desktop. |
| F12 |  | Hide or display Dashboard. |
| Grave accent (`) | Command-Grave accent | Activate the next open window in the frontmost app. |
|  | Shift-Command-Grave accent | Activate the previous open window in the frontmost app. |
|  | Option-Command-Grave accent | Move focus to the window drawer. |
| Hyphen (-) | Command-Hyphen | Decrease the size of the selection. |
|  | Option-Command-Hyphen | Zoom out when screen zooming is on. |
| Left bracket ({) | Command-Left bracket | Left-align a selection. |
| Right bracket (}) | Command-Right bracket | Right-align a selection. |
| Pipe (\|) | Command-Pipe | Center-align a selection. |
| Colon (:) | Command-Colon | Display the Spelling window. |
| Semicolon (;) | Command-Semicolon | Find misspelled words in the document. |
| Comma (,) | Command-Comma | Open the app’s settings window. |
|  | Control-Option-Command-Comma | Decrease screen contrast. |
| Period (.) | Command-Period | Cancel an operation. |
|  | Control-Option-Command-Period | Increase screen contrast. |
| Question mark (?) | Command-Question mark | Open the app’s Help menu. |
| Forward slash (/) | Option-Command-Forward slash | Turn font smoothing on or off. |
| Equal sign (=) | Shift-Command-Equal sign | Increase the size of the selection. |
|  | Option-Command-Equal sign | Zoom in when screen zooming is on. |
| 3 | Shift-Command-3 | Capture the screen to a file. |
|  | Control-Shift-Command-3 | Capture the screen to the Clipboard. |
| 4 | Shift-Command-4 | Capture a selection to a file. |
|  | Control-Shift-Command-4 | Capture a selection to the Clipboard. |
| 8 | Option-Command-8 | Turn screen zooming on or off. |
|  | Control-Option-Command-8 | Invert the screen colors. |
| A | Command-A | Select every item in a document or window, or all characters in a text field. |
|  | Shift-Command-A | Deselect all selections or characters. |
| B | Command-B | Boldface the selected text or toggle boldfaced text on and off. |
| C | Command-C | Copy the selection to the Clipboard. |
|  | Shift-Command-C | Display the Colors window. |
|  | Option-Command-C | Copy the style of the selected text. |
|  | Control-Command-C | Copy the formatting settings of the selection and store on the Clipboard. |
| D | Option-Command-D | Show or hide the Dock. |
|  | Control-Command-D | Display the definition of the selected word in the Dictionary app. |
| E | Command-E | Use the selection for a find operation. |
| F | Command-F | Open a Find window. |
|  | Option-Command-F | Jump to the search field control. |
|  | Control-Command-F | Enter full screen. |
| G | Command-G | Find the next occurrence of the selection. |
|  | Shift-Command-G | Find the previous occurrence of the selection. |
| H | Command-H | Hide the windows of the currently running app. |
|  | Option-Command-H | Hide the windows of all other running apps. |
| I | Command-I | Italicize the selected text or toggle italic text on or off. |
|  | Command-I | Display an Info window. |
|  | Option-Command-I | Display an inspector window. |
| J | Command-J | Scroll to a selection. |
| M | Command-M | Minimize the active window to the Dock. |
|  | Option-Command-M | Minimize all windows of the active app to the Dock. |
| N | Command-N | Open a new document. |
| O | Command-O | Display a dialog for choosing a document to open. |
| P | Command-P | Display the Print dialog. |
|  | Shift-Command-P | Display the Page Setup dialog. |
| Q | Command-Q | Quit the app. |
|  | Shift-Command-Q | Log out the person currently logged in. |
|  | Option-Shift-Command-Q | Log out the person currently logged in without confirmation. |
| S | Command-S | Save a new document or save a version of a document. |
|  | Shift-Command-S | Duplicate the active document or initiate a Save As. |
| T | Command-T | Display the Fonts window. |
|  | Option-Command-T | Show or hide a toolbar. |
| U | Command-U | Underline the selected text or turn underlining on or off. |
| V | Command-V | Paste the Clipboard contents at the insertion point. |
|  | Shift-Command-V | Paste as (Paste as Quotation, for example). |
|  | Option-Command-V | Apply the style of one object to the selection. |
|  | Option-Shift-Command-V | Paste the Clipboard contents at the insertion point and apply the style of the surrounding text to the inserted object. |
|  | Control-Command-V | Apply formatting settings to the selection. |
| W | Command-W | Close the active window. |
|  | Shift-Command-W | Close a file and its associated windows. |
|  | Option-Command-W | Close all windows in the app. |
| X | Command-X | Remove the selection and store on the Clipboard. |
| Z | Command-Z | Undo the previous operation. |
|  | Shift-Command-Z | Redo (when Undo and Redo are separate commands rather than toggled using Command-Z). |
| Right arrow | Command-Right arrow | Change the keyboard layout to current layout of Roman script. |
|  | Shift-Command-Right arrow | Extend selection to the next semantic unit, typically the end of the current line. |
|  | Shift-Right arrow | Extend selection one character to the right. |
|  | Option-Shift-Right arrow | Extend selection to the end of the current word, then to the end of the next word. |
|  | Control-Right arrow | Move focus to another value or cell within a view, such as a table. |
| Left arrow | Command-Left arrow | Change the keyboard layout to current layout of system script. |
|  | Shift-Command-Left arrow | Extend selection to the previous semantic unit, typically the beginning of the current line. |
|  | Shift-Left arrow | Extend selection one character to the left. |
|  | Option-Shift-Left arrow | Extend selection to the beginning of the current word, then to the beginning of the previous word. |
|  | Control-Left arrow | Move focus to another value or cell within a view, such as a table. |
| Up arrow | Shift-Command-Up arrow | Extend selection upward in the next semantic unit, typically the beginning of the document. |
|  | Shift-Up arrow | Extend selection to the line above, to the nearest character boundary at the same horizontal location. |
|  | Option-Shift-Up arrow | Extend selection to the beginning of the current paragraph, then to the beginning of the next paragraph. |
|  | Control-Up arrow | Move focus to another value or cell within a view, such as a table. |
| Down arrow | Shift-Command-Down arrow | Extend selection downward in the next semantic unit, typically the end of the document. |
|  | Shift-Down arrow | Extend selection to the line below, to the nearest character boundary at the same horizontal location. |
|  | Option-Shift-Down arrow | Extend selection to the end of the current paragraph, then to the end of the next paragraph (include the paragraph terminator, such as Return, in cut, copy, and paste operations). |
|  | Control-Down arrow | Move focus to another value or cell within a view, such as a table. |

The system also defines several keyboard shortcuts for use with localized versions of the system, localized keyboards, keyboard layouts, and input methods. These shortcuts don’t correspond directly to menu commands.

| Keyboard shortcut | Action |
| --- | --- |
| Control-Space | Toggle between the current and last input source. |
| Control-Option-Space | Switch to the next input source in the list. |
| [Modifier key]-Command-Space | Varies. |
| Command-Right arrow | Change keyboard layout to current layout of Roman script. |
| Command-Left arrow | Change keyboard layout to current layout of system script. |

## Custom keyboard shortcuts

**Define custom keyboard shortcuts for only the most frequently used app-specific commands.** People appreciate using keyboard shortcuts for actions they perform frequently, but defining too many new shortcuts can make your app seem difficult to learn.

**Use modifier keys in ways that people expect.** For example, pressing Command while dragging moves items as a group, and pressing Shift while drag-resizing constrains resizing to the item’s aspect ratio. In addition, holding an arrow key moves the selected item by the smallest app-defined unit of distance until people release the key.

Here are the modifier keys and the symbols that represent them.

| Modifier key | Symbol | Recommended usage |
| --- | --- | --- |
| Command | *image: Keyboard Command* | Prefer the Command key as the main modifier key in a custom keyboard shortcut. |
| Shift | *image: Keyboard Shift* | Prefer the Shift key as a secondary modifier that complements a related shortcut. |
| Option | *image: Keyboard Option* | Use the Option modifier sparingly for less-common commands or power features. |
| Control | *image: Keyboard Control* | Avoid using the Control key as a modifier. The system uses Control in many systemwide features and shortcuts, like moving focus or capturing screenshots. |

> **Tip:** Some languages require modifier keys to generate certain characters. For example, on a French keyboard, Option-5 generates the “{“ character. It’s usually safe to use the Command key as a modifier, but avoid using an additional modifier with characters that aren’t available on all keyboards. If you must use a modifier other than Command, prefer using it only with the alphabetic characters.

**List modifier keys in the correct order.** If you use more than one modifier key in a custom shortcut, always list them in this order: Control, Option, Shift, Command.

**Avoid adding Shift to a shortcut that uses the upper character of a two-character key.** People already understand that they must hold the Shift key to type the upper character of a two-character key, so it’s clearer to simply list the upper character in the shortcut. For example, the keyboard shortcut for Hide Status Bar is Command-Slash, whereas the keyboard shortcut for Help is Command-Question mark, not Shift-Command-Slash.

**Let the system localize and mirror your keyboard shortcuts as needed.** The system automatically localizes a shortcut’s primary and modifier keys to support the currently connected keyboard; if your app or game switches to a right-to-left layout, the system automatically mirrors the shortcut. For guidance, see [Right to left](right-to-left.md).

**Avoid creating a new shortcut by adding a modifier to an existing shortcut for an unrelated command.** For example, because people are accustomed to using Command-Z for undoing an action, it would be confusing to use Shift-Command-Z as the shortcut for a command that’s unrelated to undo and redo.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, or tvOS. Not supported in watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| June 9, 2025 | Moved game-specific key bindings guidance to the Game controls page. |
| June 10, 2024 | Added game-specific guidance and made organizational updates. |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [Virtual keyboards](virtual-keyboards.md)
- [Entering data](entering-data.md)
- [Pointing devices](pointing-devices.md)

---


<a id="pointing-devices"></a>
## pointing-devices

# Pointing devices

> Source: <https://developer.apple.com/design/human-interface-guidelines/pointing-devices>
> Section: Inputs
> Platforms covered: iOS, iPadOS, macOS (guidance specific to visionOS omitted)
> Last change on Apple's site: 2023-06-21 (Updated to include guidance for visionOS.)

People can use a pointing device like a trackpad or mouse to navigate the interface and initiate actions.

---

People appreciate the precision and flexibility that pointing devices offer. On a Mac, people typically expect to combine a pointing device with a keyboard as they navigate apps and the system. On iPad and Apple Vision Pro, a pointing device gives people an additional way to interact with apps and content, without replacing touch, eyes, or gestures.

## Best practices

**Be consistent when responding to mouse and trackpad gestures.** People expect most gestures to work the same throughout the system, regardless of the app or game they’re using. On a Mac, for example, people rely on the “Swipe between pages” gesture to behave the same way whether they’re browsing individual document pages, webpages, or images.

**Avoid redefining systemwide trackpad gestures.** Even in a game that uses app-specific gestures in a custom way, people expect systemwide gestures to be available; for example, people expect to make familiar gestures to reveal the Dock or Mission Control in macOS. Remember that Mac users can customize the gestures for performing systemwide actions.

**Provide a consistent experience in your app, whether people are using gestures, eyes, a pointing device, or a keyboard.** People expect to move fluidly between multiple types of input, and they don’t want to learn different interactions for each mode or for each app they use.

**Let people use the pointer to reveal and hide controls that automatically minimize or fade out.** In iPadOS, for example, people can reveal the minimized Safari toolbar by holding the pointer over it (the toolbar minimizes again when the pointer moves away). People can also move the pointer to reveal or hide playback controls while they watch a full-screen video.

**Provide a consistent experience when people press and hold a modifier key while interacting with objects in your app.** For example, if people can duplicate an object by pressing and holding the Option key while they drag that object, ensure the result is the same whether they drag using touch or the pointer.

## Platform considerations

*No additional considerations for iOS. Not supported in tvOS or watchOS.*

### Tablet (iPadOS)

iPadOS builds on the traditional pointer experience, automatically adapting the pointer to the current context and providing rich visual feedback at a level of precision that enhances productivity and simplifies common tasks on a touchscreen device. The iPadOS pointing system gives people an additional way to interact with apps and content — it doesn’t replace touch.

**Allow multiple selection in custom views when necessary.** In iPadOS 15 and later, people can click and drag the pointer over multiple items to select them. As people use the pointer in this way, it expands into a visible rectangle that selects the items it encompasses. Standard nonlist collection views support this interaction by default; if you want to support multiple selection in custom views, you need to implement it yourself. For developer guidance, see [UIBandSelectionInteraction](https://developer.apple.com/documentation/uikit/uibandselectioninteraction).

**Distinguish between pointer and finger input only if it provides value.** For example, a scrubber can give people an additional way to target a location in a video when they’re using the pointer. In this scenario, people can drag the playhead using either the pointer or touch, but they can use the pointer to click a precise seek destination.

#### Pointer shape and content effects

iPadOS integrates the appearance and behavior of both the pointer and the element it moves over, bringing focus to the item the pointer is targeting. You can support the system-provided pointer effects or modify them to suit your experience.

By default, the pointer’s shape is a circle, but it can display a system-defined or custom shape when people move it over specific elements or regions. For example, the pointer automatically uses the familiar I-beam shape when people move it over a text-entry area.

With a *content effect*, the UI element or region beneath the pointer can also change its appearance when people hold the pointer over it. Depending on the type of content effect, the pointer can retain its current shape or transform into a shape that integrates with the element’s new appearance.

iPadOS defines three content effects that bring focus to different types of interactive elements in your app: highlight, lift, and hover.

The *highlight* effect transforms the pointer into a translucent, rounded rectangle that acts as a background for a control and includes a gentle parallax. The subtle highlighting and movement bring focus to the control without distracting people from their task. By default, iPadOS applies the highlight effect to bar buttons, tab bars, segmented controls, and edit menus.

The *lift* effect combines a subtle parallax with the appearance of elevation to make an element seem like it’s floating above the screen. As the pointer fades out beneath the element, iPadOS creates the illusion of lift by scaling the element up while adding a shadow below it and a soft specular highlight on top of it. By default, iPadOS applies the lift effect to app icons and to buttons in Control Center.

*Hover* is a generic effect that lets you apply custom scale, tint, or shadow values to an element as the pointer moves over it. The hover effect combines your custom values to bring focus to an item, but it doesn’t transform the default pointer shape.

#### Pointer accessories

Pointer accessories are visual indicators that help people understand how they can use the pointer to interact with the current UI element. For example, a pointer approaching a resizable element might display small arrows to indicate that the element allows resizing along a certain axis.

Unlike pointer shapes and content effects, accessories are secondary items that can combine with any pointer to communicate additional information. For developer guidance, see [UIPointerAccessory](https://developer.apple.com/documentation/uikit/uipointeraccessory).

**Use clear, simple images to create custom accessories.** A pointer accessory is small, so it’s essential to create an image that communicates the pointer interaction without using too many details.

**Consider using the accessory transition to signal a change in an element’s state or behavior.** In addition to animating the appearance and disappearance of pointer accessories, the system also animates the transitions among accessory shapes and positions that can accompany content effects. For example, you could communicate that an add action has become unavailable by transitioning the pointer accessory from the `plus` symbol to the `circle.slash` symbol.

#### Pointer magnetism

iPadOS helps people use the pointer to target an element by making the element appear to attract the pointer. People can experience this magnetic effect when they move the pointer close to an element and when they flick the pointer toward an element.

When people move the pointer close to an element, the system starts transforming the pointer’s shape as soon as it reaches the element’s hit region. Because an element’s hit region typically extends beyond its visible boundaries, the pointer begins to transform before it appears to touch the element itself, creating the illusion that the element is pulling the pointer toward it.

When people flick the pointer toward an element, iPadOS examines the pointer’s trajectory to discover the element that’s the most likely target. When there’s an element in the pointer’s path, the system uses magnetism to pull the pointer toward the element’s center.

By default, iPadOS applies magnetism to elements that use the lift effect (like app icons) and the highlight effect (like bar buttons), but not to elements that use hover. Because an element that supports hover doesn’t transform the default pointer shape, adding magnetism could be jarring and might make people feel that they’ve lost control of the pointer.

The system also applies magnetism to text-entry areas, where it can help people avoid skipping to another line if they make unintended vertical movements while they’re selecting text.

#### Standard pointers and effects

**When possible, support the system-provided content effects.** People quickly become accustomed to the content effects they see throughout the system and generally expect their experience to apply to every app they use. To provide a consistent user experience, align your interactions with the design intent of each effect. Specifically:

- Use highlight for a small element that has a transparent background.
- Use lift for a small element that has an opaque background.
- Use hover for large elements and customize the scale, tint, and shadow attributes as needed (for guidance, see [Customizing pointers](#customizing-pointers)).

**Prefer the system-provided pointer appearances for standard buttons and text-entry areas.** You can help people feel more comfortable with your app when the pointer behaves in ways they expect.

**Add padding around interactive elements to create comfortable hit regions.** You might need to experiment to determine the right size for an element’s hit region. If the hit region is too small, it can make people feel that they have to be extra precise when interacting with the element. On the other hand, when an element’s hit region is too large, people can feel that it takes a lot of effort to pull the pointer away from the element. In general, it works well to add about 12 points of padding around elements that include a bezel; for elements without a bezel, it works well to add about 24 points of padding around the element’s visible edges.

**Create contiguous hit regions for custom bar buttons.** If there’s space between the hit regions of adjacent buttons in a bar, people may experience a distracting motion when the pointer reverts briefly to its default shape as it moves between buttons.

**Specify the corner radius of a nonstandard element that receives the lift effect.** With the system-provided lift effect, the pointer transforms to match the element’s shape as it fades out. By default, the pointer uses the system-defined corner radius to transform into a rounded rectangle. If your element is a different shape — if it’s a circle, for example — you need to provide the radius so the pointer can animate seamlessly into the shape of the element. For developer guidance, see [UIPointerShape.roundedRect(_:radius:)](https://developer.apple.com/documentation/uikit/uipointershape-swift.enum/roundedrect(_:radius:)).

#### Customizing pointers

**Prefer system-provided pointer effects for custom elements that behave like standard elements.** When a custom element behaves like a standard one, people generally expect to interact with it using familiar pointer interactions. For example, if buttons in a custom toolbar don’t use the standard highlight effect, people might think they’re broken.

**Use pointer effects in consistent ways throughout your app.** For example, if your app helps people draw, provide a similar pointer experience for every drawing area in your app so that people can apply the knowledge they gain in one area to the others.

**Avoid creating gratuitous pointer and content effects.** People notice when the appearance of the pointer or the UI element beneath it changes, and they expect the changes to be useful. Creating a purely decorative pointer effect can distract and even irritate people without providing any practical value.

**Keep custom pointer shapes simple.** Ideally, the pointer’s shape signals the action people can take in the current context without drawing too much attention to itself. If people don’t instantly understand your custom pointer shape, they’re likely to waste time trying to discover what the shape means.

**Consider enhancing the pointer experience by displaying custom annotations that provide useful information.** For example, you could display X and Y values when people hold the pointer over a graphing area in your app. Keynote uses annotations to display the current width and height of a resizable image.

**Avoid displaying instructional text with a pointer.** A pointer that displays instructional text can make an app seem complicated and difficult to use. Instead of providing instructions, prioritize clarity and simplicity in your interface, so that people can quickly grasp how to use your app whether they’re using the pointer or touching the screen.

**Consider the interplay of shadow, scale, and element spacing when defining custom hover effects.** In general, reserve scaling for elements that can increase in size without crowding nearby elements. For example, scaling doesn’t work well for a table row because a row can’t expand without overlapping adjacent rows. For an element that has little space around it, consider using a hover effect that includes tint, but not scale and shadow. Note that it doesn’t work well to use shadow without including scale, because an unscaled element doesn’t appear to get closer to the viewer even when its shadow implies that it’s elevated above the screen.

### Desktop (macOS)

macOS supports a wide range of standard mouse and trackpad interactions that people can customize. For example, when a click or gesture isn’t a primary way to interact with content, people can often turn it on or off based on their current workflow. People can also choose specific regions of a mouse or trackpad to invoke secondary clicks, and select specific finger combinations and movements for certain gestures.

| Click or gesture | Expected behavior | Mouse | Trackpad |
| --- | --- | --- | --- |
| Primary click | Select or activate an item, such as a file or button. | ● | ● |
| Secondary click | Reveal contextual menus. | ● | ● |
| Scrolling | Move content up, down, left, or right within a view. | ● | ● |
| Smart zoom | Zoom in or out on content, such as a web page or PDF. | ● | ● |
| Swipe between pages | Navigate forward or backward between individually displayed pages. | ● | ● |
| Swipe between full-screen apps | Navigate forward or backward between full-screen apps and spaces. | ● | ● |
| Mission Control (double-tap the mouse with two fingers or swipe up on the trackpad with three or four fingers) | Activate Mission Control. | ● | ● |
| Lookup and data detectors (force click with one finger or tap with three fingers) | Display a lookup window above selected content. |  | ● |
| Tap to click | Perform the primary click action using a tap rather than a click. |  | ● |
| Force click | Click then press firmly to display a Quick Look window or lookup window above selected content. Apply a variable amount of pressure to affect pressure-sensitive controls, such as variable speed media controls. |  | ● |
| Zoom in or out (pinch with two fingers) | Zoom in or out. |  | ● |
| Rotate (move two fingers in a circular motion) | Rotate content, such as an image. |  | ● |
| Notification Center (swipe from the edge of the trackpad) | Display Notification Center. |  | ● |
| App Exposé (swipe down with three or four fingers) | Display the current app’s windows in Exposé. |  | ● |
| Launchpad (pinch with thumb and three fingers) | Display the Launchpad. |  | ● |
| Show Desktop (spread with thumb and three fingers) | Slide all windows out of the way to reveal the desktop. |  | ● |

#### Pointers

macOS offers a variety of standard pointer styles, which your app can use to communicate the interactive state of an interface element or the result of a drag operation.

| Pointer | Name | Meaning | AppKit API |
| --- | --- | --- | --- |
| *image: pointers arrow* | Arrow | Standard pointer for selecting and interacting with content and interface elements. | [arrow](https://developer.apple.com/documentation/appkit/nscursor/arrow) |
| *image: pointers closed hand* | Closed hand | Dragging to reposition the display of content within a view—for example, dragging a map around in Maps. | [closedHand](https://developer.apple.com/documentation/appkit/nscursor/closedhand) |
| *image: pointers contextual menu* | Contextual menu | A contextual menu is available for the content below the pointer. This pointer is generally shown only when the Control key is pressed. | [contextualMenu](https://developer.apple.com/documentation/appkit/nscursor/contextualmenu) |
| *image: pointers crosshair* | Crosshair | Precise rectangular selection is possible, such as when viewing an image in Preview. | [crosshair](https://developer.apple.com/documentation/appkit/nscursor/crosshair) |
| *image: pointers disappearing item* | Disappearing item | A dragged item will disappear when dropped. If the item references an original item, the original is unaffected. For example, when dragging a mailbox out of the favorites bar in Mail, the original mailbox isn’t removed. | [disappearingItem](https://developer.apple.com/documentation/appkit/nscursor/disappearingitem) |
| *image: pointers drag copy* | Drag copy | Duplicates a dragged—not moved—item when dropped into the destination. Appears when pressing the Option key during a drag operation. | [dragCopy](https://developer.apple.com/documentation/appkit/nscursor/dragcopy) |
| *image: pointers drag link* | Drag link | During a drag and drop operation, creates an alias of the selected file when dropped. The alias points to the original file, which remains unmoved. Appears when pressing the Option and Command keys during a drag operation. | [dragLink](https://developer.apple.com/documentation/appkit/nscursor/draglink) |
| *image: pointers horizontal beam* | Horizontal I beam | Selection and insertion of text is possible in a horizontal layout, such as a TextEdit or Pages document. | [iBeam](https://developer.apple.com/documentation/appkit/nscursor/ibeam) |
| *image: pointers open hand* | Open hand | Dragging to reposition content within a view is possible. | [openHand](https://developer.apple.com/documentation/appkit/nscursor/openhand) |
| *image: pointers operation not allowed* | Operation not allowed | A dragged item can’t be dropped in the current location. | [operationNotAllowed](https://developer.apple.com/documentation/appkit/nscursor/operationnotallowed) |
| *image: pointers pointing hand* | Pointing hand | The content beneath the pointer is a URL link to a webpage, document, or other item. | [pointingHand](https://developer.apple.com/documentation/appkit/nscursor/pointinghand) |
| *image: pointers resize down* | Resize down | Resize or move a window, view, or element downward. | [resizeDown](https://developer.apple.com/documentation/appkit/nscursor/resizedown) |
| *image: pointers resize left* | Resize left | Resize or move a window, view, or element to the left. | [resizeLeft](https://developer.apple.com/documentation/appkit/nscursor/resizeleft) |
| *image: pointers resize left right* | Resize left/right | Resize or move a window, view, or element to the left or right. | [resizeLeftRight](https://developer.apple.com/documentation/appkit/nscursor/resizeleftright) |
| *image: pointers resize right* | Resize right | Resize or move a window, view, or element to the right. | [resizeRight](https://developer.apple.com/documentation/appkit/nscursor/resizeright) |
| *image: pointers resize up* | Resize up | Resize or move a window, view, or element upward. | [resizeUp](https://developer.apple.com/documentation/appkit/nscursor/resizeup) |
| *image: pointers resize up down* | Resize up/down | Resize or move a window, view, or element upward or downward. | [resizeUpDown](https://developer.apple.com/documentation/appkit/nscursor/resizeupdown) |
| *image: pointers vertical beam* | Vertical I beam | Selection and insertion of text is possible in a vertical layout. | [iBeamCursorForVerticalLayout](https://developer.apple.com/documentation/appkit/nscursor/ibeamcursorforverticallayout) |

## Change log

| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [Entering data](entering-data.md)
- [Keyboards](keyboards.md)

---
