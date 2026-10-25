# Apple HIG — Foundations
Bundled HIG pages for the “Foundations” group. Each page kept verbatim under an anchor heading `## <slug>`. Cite as **foundations.md › <slug> › heading**.


<a id="accessibility"></a>
## accessibility

# Accessibility

> Source: <https://developer.apple.com/design/human-interface-guidelines/accessibility>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-06-09 (Added guidance and links for Assistive Access, Switch Control, and Accessibility Nutrition Labels.)

Accessible user interfaces empower everyone to have a great experience with your app or game.

---

When you design for accessibility, you reach a larger audience and create a more inclusive experience. An accessible interface allows people to experience your app or game regardless of their capabilities or how they use their devices. Accessibility makes information and interactions available to everyone. An accessible interface is:

- **Intuitive.** Your interface uses familiar and consistent interactions that make tasks straightforward to perform.
- **Perceivable.** Your interface doesn’t rely on any single method to convey information. People can access and interact with your content, whether they use sight, hearing, speech, or touch.
- **Adaptable.** Your interface adapts to how people want to use their device, whether by supporting system accessibility features or letting people personalize settings.

As you design your app, audit the accessibility of your interface. Use [Accessibility Inspector](https://developer.apple.com/documentation/accessibility/accessibility-inspector) to highlight accessibility issues with your interface and to understand how your app represents itself to people using system accessibility features. You can also communicate how accessible your app is on the App Store using Accessibility Nutrition Labels. To learn more about how to evaluate and indicate accessibility feature support, see [Accessibility Nutrition Labels](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels) in App Store Connect help.

## Vision

The people who use your interface may be blind, color blind, or have low vision or light sensitivity. They may also be in situations where lighting conditions and screen brightness affect their ability to interact with your interface.

**Support larger text sizes.** Make sure people can adjust the size of your text or icons to make them more legible, visible, and comfortable to read. Ideally, give people the option to enlarge text by at least 200 percent (or 140 percent in watchOS apps). Your interface can support font size enlargement either through custom UI, or by adopting Dynamic Type. Dynamic Type is a systemwide setting that lets people adjust the size of text for comfort and legibility. For more guidance, see [Supporting Dynamic Type](typography.md#supporting-dynamic-type).

**Use recommended defaults for custom type sizes.** Each platform has different default and minimum sizes for system-defined type styles to promote readability. If you’re using custom type styles, follow the recommended defaults.

| Platform | Default size | Minimum size |
| --- | --- | --- |
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |

**Bear in mind that font weight can also impact how easy text is to read.** If you’re using a custom font with a thin weight, aim for larger than the recommended sizes to increase legibility. For more guidance, see [Typography](typography.md).

**Strive to meet color contrast minimum standards.** To ensure all information in your app is legible, it’s important that there’s enough contrast between foreground text and icons and background colors. Two popular standards of measure for color contrast are the [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/TR/WCAG/) and the Accessible Perceptual Contrast Algorithm (APCA). Use standard contrast calculators to ensure your UI meets acceptable levels. [Accessibility Inspector](https://developer.apple.com/documentation/accessibility/accessibility-inspector) uses the following values from WCAG Level AA as guidance in determining whether your app’s colors have an acceptable contrast.

| Text size | Text weight | Minimum contrast ratio |
| --- | --- | --- |
| Up to 17 pts | All | 4.5:1 |
| 18 pts | All | 3:1 |
| All | Bold | 3:1 |

If your app doesn’t provide this minimum contrast by default, ensure it at least provides a higher contrast color scheme when the system setting Increase Contrast is turned on. If your app supports [Dark Mode](dark-mode.md), make sure to check the minimum contrast in both light and dark appearances.

**Prefer system-defined colors.** These colors have their own accessible variants that automatically adapt when people adjust their color preferences, such as enabling Increase Contrast or toggling between the light and dark appearances. For guidance, see [Color](color.md).

**Convey information with more than color alone.** Some people have trouble differentiating between certain colors and shades. For example, people who are color blind may have particular difficulty with pairings such as red-green and blue-orange. Offer visual indicators, like distinct shapes or icons, in addition to color to help people perceive differences in function and changes in state. Consider allowing people to customize color schemes such as chart colors or game characters so they can personalize your interface in a way that’s comfortable for them.

**Describe your app’s interface and content for VoiceOver.** VoiceOver is a screen reader that lets people experience your app’s interface without needing to see the screen. For more guidance, see [VoiceOver](voiceover.md).

## Hearing

The people who use your interface may be deaf or hard of hearing. They may also be in noisy or public environments.

**Support text-based ways to enjoy audio and video.** It’s important that dialogue and crucial information about your app or game isn’t communicated through audio alone. Depending on the context, give people different text-based ways to experience their media, and allow people to customize the visual presentation of that text:

- **Captions** give people the textual equivalent of audible information in video or audio-only content. Captions are great for scenarios like game cutscenes and video clips where text synchronizes live with the media.
- **Subtitles** allow people to read live onscreen dialogue in their preferred language. Subtitles are great for TV shows and movies.
- **Audio descriptions** are interspersed between natural pauses in the main audio of a video and supply spoken narration of important information that’s presented only visually.
- **Transcripts** provide a complete textual description of a video, covering both audible and visual information. Transcripts are great for longer-form media like podcasts and audiobooks where people may want to review content as a whole or highlight the transcript as media is playing.

For developer guidance, see [Selecting subtitles and alternative audio tracks](https://developer.apple.com/documentation/avfoundation/selecting-subtitles-and-alternative-audio-tracks).

**Use haptics in addition to audio cues.** If your interface conveys information through audio cues — such as a success chime, error sound, or game feedback — consider pairing that sound with matching haptics for people who can’t perceive the audio or have their audio turned off. In iOS and iPadOS, you can also use [Music Haptics](https://developer.apple.com/documentation/mediaaccessibility/music-haptics) and [Audio graphs](https://developer.apple.com/documentation/accessibility/audio-graphs) to let people experience music and infographics through vibration and texture. For guidance, see [Playing haptics](playing-haptics.md).

**Augment audio cues with visual cues.** This is especially important for games and spatial apps where important content might be taking place off screen. When using audio to guide people towards a specific action, also add in visual indicators that point to where you want people to interact.

## Mobility

Ensure your interface offers a comfortable experience for people with limited dexterity or mobility.

**Offer sufficiently sized controls.** Controls that are too small are hard for many people to interact with and select. Strive to meet the recommended minimum control size for each platform to ensure controls and menus are comfortable for all when tapping and clicking.

| Platform | Default control size | Minimum control size |
| --- | --- | --- |
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |

**Consider spacing between controls as important as size.** Include enough padding between elements to reduce the chance that someone taps the wrong control. In general, it works well to add about 12 points of padding around elements that include a bezel. For elements without a bezel, about 24 points of padding works well around the element’s visible edges.

**Support simple gestures for common interactions.** For many people, with or without disabilities, complex gestures can be challenging. For interactions people do frequently in your app or game, use the simplest gesture possible — avoid custom multifinger and multihand gestures — so repetitive actions are both comfortable and easy to remember.

**Offer alternatives to gestures.** Make sure your UI’s core functionality is accessible through more than one type of physical interaction. Gestures can be less comfortable for people who have limited dexterity, so offer onscreen ways to achieve the same outcome. For example, if you use a swipe gesture to dismiss a view, also make a button available so people can tap or use an assistive device.

**Let people use Voice Control to give guidance and enter information verbally.** With Voice Control, people can interact with their devices entirely by speaking commands. They can perform gestures, interact with screen elements, dictate and edit text, and more. To ensure a smooth experience, label interface elements appropriately. For developer guidance, see [Voice Control](https://developer.apple.com/documentation/accessibility/voice-control).

**Integrate with Siri and Shortcuts to let people perform tasks using voice alone.** When your app supports Siri and Shortcuts, people can automate the important and repetitive tasks they perform regularly. They can initiate these tasks from Siri, the Action button on their iPhone or Apple Watch, and shortcuts on their Home Screen or in Control Center. For guidance, see [Siri](siri.md).

**Support mobility-related assistive technologies.** Features like [VoiceOver](voiceover.md), AssistiveTouch, Full Keyboard Access, Pointer Control, and [Switch Control](https://developer.apple.com/documentation/accessibility/switch-control) offer alternative ways for people with low mobility to interact with their devices. Conduct testing and verify that your app or game supports these technologies, and that your interface elements are appropriately labeled to ensure a great experience. For more information, see [Performing accessibility testing for your app](https://developer.apple.com/documentation/accessibility/performing-accessibility-testing-for-your-app).

## Speech

Apple’s accessibility features help people with speech disabilities and people who prefer text-based interactions to communicate effectively using their devices.

**Let people use the keyboard alone to navigate and interact with your app.** People can turn on Full Keyboard Access to navigate apps using their physical keyboard. The system also defines accessibility keyboard shortcuts and a wide range of other [keyboard shortcuts](https://support.apple.com/en-us/102650) that many people use all the time. Avoid overriding system-defined keyboard shortcuts and evaluate your app to ensure it works well with Full Keyboard Access. For additional guidance, see [Keyboards](keyboards.md). For developer guidance, see [Support Full Keyboard Access in your iOS app](https://developer.apple.com/videos/play/wwdc2021/10120).

**Support Switch Control.** Switch Control is an assistive technology that lets people control their devices through separate hardware, game controllers, or sounds such as a click or a pop. People can perform actions like selecting, tapping, typing, and drawing when your app or game supports the ability to navigate using Switch Control. For developer guidance, see [Switch Control](https://developer.apple.com/documentation/accessibility/switch-control).

## Cognitive

When you minimize complexity in your app or game, all people benefit.

**Keep actions simple and intuitive.** Ensure that people can navigate your interface using easy-to-remember and consistent interactions. Prefer system gestures and behaviors people are already familiar with over creating custom gestures people must learn and retain.

**Minimize use of time-boxed interface elements.** Views and controls that auto-dismiss on a timer can be problematic for people who need longer to process information, and for people who use assistive technologies that require more time to traverse the interface. Prefer dismissing views with an explicit action.

**Consider offering difficulty accommodations in games.** Everyone has their own way of playing and enjoying games. To support a variety of cognitive abilities, consider adding the ability to customize the difficulty level of your game, such as offering options for people to reduce the criteria for successfully completing a level, adjust reaction time, or enable control assistance.

**Let people control audio and video playback.** Avoid autoplaying audio and video content without also providing controls to start and stop it. Make sure these controls are discoverable and easy to act upon, and consider global settings that let people opt out of auto-playing all audio and video. For developer guidance, see [Animated images](https://developer.apple.com/documentation/accessibility/animated-images) and [isVideoAutoplayEnabled](https://developer.apple.com/documentation/uikit/uiaccessibility/isvideoautoplayenabled).

**Allow people to opt out of flashing lights in video playback.** People might want to avoid bright, frequent flashes of light in the media they consume. A Dim Flashing Lights setting allows the system to calculate, mitigate, and inform people about flashing lights in a piece of media. If your app supports video playback, ensure that it responds appropriately to the Dim Flashing Lights setting. For developer guidance, see [Flashing lights](https://developer.apple.com/documentation/mediaaccessibility/flashing-lights).

**Be cautious with fast-moving and blinking animations.** When you use these effects in excess, it can be distracting, cause dizziness, and in some cases even result in epileptic episodes. People who are prone to these effects can turn on the Reduce Motion accessibility setting. When this setting is active, ensure your app or game responds by reducing automatic and repetitive animations, including zooming, scaling, and peripheral motion. Other best practices for reducing motion include:

- Tightening animation springs to reduce bounce effects
- Tracking animations directly with people’s gestures
- Avoiding animating depth changes in z-axis layers
- Replacing transitions in x-, y-, and z-axes with fades to avoid motion
- Avoiding animating into and out of blurs

**Optimize your app’s UI for Assistive Access.** Assistive Access is an accessibility feature in iOS and iPadOS that allows people with cognitive disabilities to use a streamlined version of your app. Assistive Access sets a default layout and control presentation for apps that reduces cognitive load, such as the following layout of the Camera app.

To optimize your app for this mode, use the following guidelines when Assistive Access is turned on:

- Identify the core functionality of your app and consider removing noncritical workflows and UI elements.
- Break up multistep workflows so people can focus on a single interaction per screen.
- Always ask for confirmation twice whenever people perform an action that’s difficult to recover from, such a deleting a file.

For developer guidance, see [Assistive Access](https://developer.apple.com/documentation/accessibility/assistive-access).

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| June 9, 2025 | Added guidance and links for Assistive Access, Switch Control, and Accessibility Nutrition Labels. |
| March 7, 2025 | Expanded and refined all guidance. Moved Dynamic Type guidance to the Typography page, and moved VoiceOver guidance to a new VoiceOver page. |
| June 10, 2024 | Added a link to Apple’s Unity plug-ins for supporting Dynamic Type. |
| December 5, 2023 | Updated visionOS Zoom lens artwork. |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [Inclusion](inclusion.md)
- [Typography](typography.md)
- [VoiceOver](voiceover.md)

---


<a id="app-icons"></a>
## app-icons

# App icons

> Source: <https://developer.apple.com/design/human-interface-guidelines/app-icons>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2026-06-08 (Refined guidance for Liquid Glass.)

A unique, memorable icon expresses your app’s or game’s purpose and personality and helps people recognize it at a glance.

---

Your app icon is a crucial aspect of your app’s or game’s branding and user experience. It appears on the Home Screen and in key locations throughout the system, including search results, notifications, system settings, and share sheets. A well-designed app icon conveys your app’s or game’s identity clearly and consistently across all Apple platforms.

## Layer design

Although you can provide a flattened image for your icon, layers give you the most control over how your icon design is represented. A layered app icon comes together to produce a sense of depth and vitality. On each platform, the system applies visual effects that respond to the environment and people’s interactions.

iOS, iPadOS, macOS, and watchOS app icons include a background layer and one or more foreground layers that coalesce to create dimensionality. These icons take on Liquid Glass attributes like specular highlights, refraction, and translucency. These effects automatically adapt with the size of your icon, apply consistently across platforms, and can appear differently between system versions.

tvOS app icons use between two and five layers to create a sense of dynamism as people bring them into focus. When focused, the app icon elevates to the foreground in response to someone’s finger movement on their remote, and gently sways while the surface illuminates. The separation between layers and the use of transparency produce a feeling of depth during the parallax effect.

A visionOS app icon includes a background layer and one or two layers on top, producing a three-dimensional object that subtly expands when people view it. The system enhances the icon’s visual dimensionality by adding shadows that convey a sense of depth between layers and by using the alpha channel of the upper layers to create an embossed appearance.

You use your favorite design tool to craft the individual foreground layers of your app icon. For iOS, iPadOS, macOS, and watchOS icons, you then import your icon layers into Icon Composer, a design tool included with Xcode and available from the [Apple Developer website](https://developer.apple.com/icon-composer). In Icon Composer, you define the background layer for your icon, adjust your foreground layer placement, apply visual effects like specular highlights and refraction, annotate for default, dark, and mono appearance variants, test and preview your icon across system versions, and export your icon for use in Xcode. For additional guidance, see [Creating your app icon using Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer).

For tvOS and visionOS app icons, you add your icon layers directly to an image stack in Xcode to form your complete icon. You can download Parallax Previewer and Parallax Exporter plug-in from [Apple Design Resources](https://developer.apple.com/design/resources/) to preview and test parallax visual effects. For developer guidance, see [Configuring your app icon using an asset catalog](https://developer.apple.com/documentation/xcode/configuring-your-app-icon).

**Prefer clearly defined edges in foreground layers.** To ensure system-drawn highlights and shadows look best, avoid soft and feathered edges on foreground layer shapes.

**Vary opacity in foreground layers to increase the sense of depth and liveliness.** For example, the Photos icon separates its centerpiece into multiple layers that contain translucent pieces, bringing greater dynamism to the design. Importing fully opaque layers and adjusting transparency in Icon Composer lets you preview and make adjustments to your design based on how transparency and system effects impact one another.

**Design a background that both stands out and emphasizes foreground content.** If you choose a gradient for your background layer, ensure that it responds well to system lighting effects. Icon Composer supports solid colors and gradients for background layers, making it unnecessary to import custom background images in most cases. If you do import a background layer, make sure it’s full-bleed and opaque.

**Prefer vector graphics when bringing layers into Icon Composer.** Unlike raster images, vector graphics (such as SVG or PDF) scale gracefully and appear crisp at any size. Outline artwork and convert text to outline in your design. For mesh gradients and raster artwork, prefer PNG format because it’s a lossless image format.

## Icon shape

An app icon’s shape varies based on a platform’s visual language. In iOS, iPadOS, and macOS, icons are square, and the system applies masking to produce rounded corners that precisely match the curvature of other rounded interface elements throughout the system and the bezel of the physical device itself. In tvOS, icons are rectangular, also with concentric edges. In visionOS and watchOS, icons are square and the system applies circular masking.

**Produce appropriately shaped, unmasked layers.** The system masks all layer edges to produce an icon’s final shape. For iOS, iPadOS, and macOS icons, provide square layers so the system can apply rounded corners. For visionOS and watchOS, provide square layers so the system can create the circular icon shape. For tvOS, provide rectangular layers so the system can apply rounded corners. Providing layers with pre-defined masking negatively impacts specular highlight effects and makes edges look jagged.

**Keep primary content centered to avoid truncation when the system adjusts corners or applies masking.** Pay particular attention to centering content in visionOS and watchOS icons. To help with icon placement, use the grids in the app icon production templates, which you can find in [Apple Design Resources](https://developer.apple.com/design/resources/).

## Design

Embrace simplicity in your icon design. Simple icons tend to be easiest for people to understand and recognize. An icon with fine visual features might look busy when rendered with system-provided shadows and highlights, and details may be hard to discern at smaller sizes. Find a concept or element that captures the essence of your app or game, make it the core idea of your icon, and express it in a simple, unique way with a minimal number of shapes. Prefer a simple background, such as a solid color or gradient, that puts the emphasis on your primary design — you don’t need to fill the entire icon canvas with content.

**Provide a visually consistent icon design across all the platforms your app supports.** A consistent design helps people quickly find your app wherever it appears and prevents people from mistaking your app for multiple apps.

**Consider basing your icon design around filled, overlapping shapes.** Overlapping solid shapes in the foreground, particularly when paired with transparency and blurring, can give an icon a sense of depth.

**Include text only when it’s essential to your experience or brand.** Text in icons doesn’t support accessibility or localization, is often too small to read easily, and can make an icon appear cluttered. In some contexts, your app name already appears nearby, making it redundant to display the name within the icon itself. Although displaying a mnemonic like the first letter of your app’s name can help people recognize your app or game, avoid including nonessential words that tell people what to do with it — like “Watch” or “Play” — or context-specific terms like “New” or “For visionOS.” If you include text in a tvOS app icon, make sure it’s above other layers so it’s not cropped by the parallax effect.

**Prefer illustrations to photos and avoid replicating UI components.** Photos are full of details that don’t work well when displayed in different appearances, viewed at small sizes, or split into layers. Instead of using photos, create a graphic representation of the content that emphasizes the features you want people to notice. Make sure to avoid extremely thin line weights and sharp corners, because they tend to lose detail and crispness in smaller icon sizes at lower resolutions. If your app has an interface that people recognize, don’t just replicate standard UI components or use app screenshots in your icon.

**Don’t use replicas of Apple hardware products.** Apple products are copyrighted and can’t be reproduced in your app icons.

## Visual effects

**Let the system handle blurring and other visual effects.** The system dynamically applies visual effects to your app icon layers, so there’s no need to include specular highlights, drop shadows between layers, beveled edges, blurs, glows, and other effects. In addition to interfering with system-provided effects, custom effects are static, whereas the system supplies dynamic ones. If you do include custom visual effects on your icon layers, use them intentionally and test carefully with Icon Composer, on a simulated device in Device Hub, or on a physical device to make sure they appear as expected and don’t conflict with system effects.

**Create layer groupings to apply effects to multiple layers at once.** System effects typically occur on individual layers. If it makes sense for your design, however, you can group several layers together in Icon Composer or your design tool so effects occur at the group level. For a group, Icon Composer provides additional customization options for Liquid Glass effects, so you can configure attributes like specular highlights, refraction, and translucency.

## Appearances

In iOS, iPadOS, and macOS, people can choose whether their Home Screen app icons are default, dark, clear, or tinted in appearance. For example, someone may want to personalize their app icon appearance to complement their wallpaper. You can design app icon variants for every appearance variant, and the system automatically generates variants you don’t provide.

**Keep your icon’s features consistent across appearances.** To create a seamless experience, keep your icon’s core visual features the same in the default, dark, clear, and tinted appearances. Avoid creating custom icon variants that swap elements in and out with each variant, which may make it harder for people to find your app when they switch appearances.

**Design dark and tinted icons that feel at home beside system app icons and widgets.** You can preserve the color palette of your default icon, but be mindful that dark icons are more subdued, and clear and tinted icons are even more so. A great app icon is visible, legible, and recognizable, regardless of its appearance variant.

**Use your light app icon as the basis for your dark icon.** Choose complementary colors that reflect the default design, and avoid excessively bright images. Color backgrounds generally offer the greatest contrast in dark icons. For guidance, see [Dark Mode](dark-mode.md).

**Consider offering alternate app icons.** In iOS, iPadOS, tvOS, and compatible apps running in visionOS, it’s possible to let people visit your app’s settings to choose an alternate version of your app icon. For example, a sports app might offer icons for different teams, letting someone choose their favorite. If you offer this capability, make sure each icon you design remains closely related to your content and experience. Avoid creating one someone might mistake for another app.

> **Note:** Alternate app icons in iOS and iPadOS require their own dark, clear, and tinted variants. As with your default app icon, all alternate and variant icons are subject to app review and must adhere to the [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/#design).

## Platform considerations

*No additional considerations for iOS, iPadOS, or macOS.*

## Specifications

The layout, size, style, and appearances of app icons vary by platform.

| Platform | Layout shape | Icon shape after system masking | Layout size | Style | Appearances |
| --- | --- | --- | --- | --- | --- |
| iOS, iPadOS, macOS | Square | Rounded rectangle (square) | 1024x1024 px | Layered | Default, dark, clear light, clear dark, tinted light, tinted dark |

The system automatically scales your icon to produce smaller variants that appear in certain locations, such as Settings and notifications.

App icons support the following color spaces:

- sRGB (color)
- Gray Gamma 2.2 (grayscale)
- Display P3 (wide-gamut color in iOS, iPadOS, macOS, tvOS, and watchOS only)

## Change log

| Date | Changes |
| --- | --- |
| June 8, 2026 | Refined guidance for Liquid Glass. |
| June 9, 2025 | Updated guidance to reflect layered icons, consistency across platforms, and best practices for Liquid Glass. |
| June 10, 2024 | Added guidance for creating dark and tinted app icon variants for iOS and iPadOS. |
| January 31, 2024 | Clarified platform availability for alternate app icons. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Added specifications for Apple Watch Ultra. |

## Related guidelines

- [Icons](icons.md)
- [Images](images.md)
- [Dark Mode](dark-mode.md)

---


<a id="branding"></a>
## branding

# Branding

> Source: <https://developer.apple.com/design/human-interface-guidelines/branding>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2026-09-09 (Refined guidance for using brand color.)

Apps and games express their unique brand identity in ways that make them instantly recognizable while feeling at home on the platform and giving people a consistent experience.

---

In addition to expressing your brand in your [app icon](app-icons.md) and throughout your experience, you have several opportunities to highlight it within the App Store. For guidance, see [App Store Marketing Guidelines](https://developer.apple.com/app-store/marketing/guidelines/).

## Best practices

**Use your brand’s unique voice and tone in all the written communication you display.** For example, your brand might convey feelings of encouragement and optimism by using plain words, occasional exclamation marks and emoji, and simple sentence structures.

**Apply your app’s accent color judiciously.** Using your brand color too broadly can overwhelm your interface and dilute its impact. Minimize its use on controls and instead use it intentionally for primary actions or status indicators, like badges for unread content or an icon for the selected tab in a tab bar. To express your brand through color, consider moving it into the content layer, where it scrolls beneath Liquid Glass controls and gets picked up dynamically. For guidance, see [Color](color.md).

**Consider using a custom font.** If your brand is strongly associated with a specific font, be sure that it’s legible at all sizes and supports accessibility features like bold text and Dynamic Type. It can work well to use a custom font for headlines and subheadings while using system fonts for body copy and captions, because the system fonts are designed for optimal legibility at small sizes. For guidance, see [Typography](typography.md).

**Express your brand with familiar components.** When you use components that people already know, the experience feels immediately reliable and familiar, and people can focus on the unique content and features that make your app stand apart. If you need to customize a component’s appearance to reflect your brand, ensure that details like sizing, placement, and behavior continue to preserve a familiar experience that’s appropriate for the platform.

**Ensure branding always defers to content.** Using screen space for an element that does nothing but display a brand asset can mean there’s less room for the content people care about. Aim to incorporate branding in refined, unobtrusive ways that don’t distract people from your experience.

**Help people feel comfortable by using standard patterns consistently.** Even a highly stylized interface can be approachable if it maintains familiar behaviors and patterns. Place UI in expected locations, use standard symbols to represent common actions, and rely on established conventions for navigation and modality.

**Resist the temptation to display your logo throughout your app or game unless it’s essential for providing context.** People seldom need to be reminded which app they’re using, and it’s usually better to use the space to give people valuable information and controls.

**Avoid using a launch screen as a branding opportunity.** Some platforms use a launch screen to minimize the startup experience, while simultaneously giving the app or game a little time to load resources (for guidance, see [Launch screens](launching.md#launch-screens)). A launch screen disappears too quickly to convey any information, but you might consider displaying a welcome or onboarding screen that incorporates your branding content at the beginning of your experience. For guidance, see [Onboarding](onboarding.md).

**Follow Apple’s trademark guidelines.** Apple trademarks must not appear in your app name or images. See [Apple Trademark List](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html) and [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html).

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| September 9, 2026 | Refined guidance for using brand color. |

## Related guidelines

- [Color](color.md)

---


<a id="color"></a>
## color

# Color

> Source: <https://developer.apple.com/design/human-interface-guidelines/color>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-12-16 (Updated guidance for Liquid Glass.)

Judicious use of color can enhance communication, evoke your brand, provide visual continuity, communicate status and feedback, and help people understand information.

---

The system defines colors that look good on various backgrounds and appearance modes, and can automatically adapt to vibrancy and accessibility settings. Using system colors is a convenient way to make your experience feel at home on the device.

You may also want to use custom colors to enhance the visual experience of your app or game and express its unique personality. The following guidelines can help you use color in ways that people appreciate, regardless of whether you use system-defined or custom colors.

## Best practices

**Avoid using the same color to mean different things.** Use color consistently throughout your interface, especially when you use it to help communicate information like status or interactivity. For example, if you use your brand color to indicate that a borderless button is interactive, using the same or similar color to stylize noninteractive text is confusing.

**Make sure all your app’s colors work well in light, dark, and increased contrast contexts.** iOS, iPadOS, macOS, and tvOS offer both light and [dark](dark-mode.md) appearance settings. [System colors](#system-colors) vary subtly depending on the system appearance, adjusting to ensure proper color differentiation and contrast for text, symbols, and other elements. With the Increase Contrast setting turned on, the color differences become far more apparent. When possible, use system colors, which already define variants for all these contexts. If you define a custom color, make sure to supply light and dark variants, and an increased contrast option for each variant that provides a significantly higher amount of visual differentiation. Even if your app ships in a single appearance mode, provide both light and dark colors to support Liquid Glass adaptivity in these contexts.

**Test your app’s color scheme under a variety of lighting conditions.** Colors can look different when you view your app outside on a sunny day or in dim light. In bright surroundings, colors look darker and more muted. In dark environments, colors appear bright and saturated. In visionOS, colors can look different depending on the colors of a wall or object in a person’s physical surroundings and how it reflects light. Adjust app colors to provide an optimal viewing experience in the majority of use cases.

**Test your app on different devices.** For example, the True Tone display — available on certain iPhone, iPad, and Mac models — uses ambient light sensors to automatically adjust the white point of the display to adapt to the lighting conditions of the current environment. Apps that primarily support reading, photos, video, and gaming can strengthen or weaken this effect by specifying a white point adaptivity style (for developer guidance, see [UIWhitePointAdaptivityStyle](https://developer.apple.com/documentation/bundleresources/information-property-list/uiwhitepointadaptivitystyle)). Test tvOS apps on multiple brands of HD and 4K TVs, and with different display settings. You can also test the appearance of your app using different color profiles on a Mac — such as P3 and Standard RGB (sRGB) — by choosing a profile in System Settings > Displays. For guidance, see [Color management](#color-management).

**Consider how artwork and translucency affect nearby colors.** Variations in artwork sometimes warrant changes to nearby colors to maintain visual continuity and prevent interface elements from becoming overpowering or underwhelming. Maps, for example, displays a light color scheme when in map mode but switches to a dark color scheme when in satellite mode. Colors can also appear different when placed behind or applied to a translucent element like a toolbar.

**If your app lets people choose colors, prefer system-provided color controls where available.** Using built-in color pickers provides a consistent user experience, in addition to letting people save a set of colors they can access from any app. For developer guidance, see [ColorPicker](https://developer.apple.com/documentation/swiftui/colorpicker).

## Inclusive color

**Avoid relying solely on color to differentiate between objects, indicate interactivity, or communicate essential information.** When you use color to convey information, be sure to provide the same information in alternative ways so people with color blindness or other visual disabilities can understand it. For example, you can use text labels or glyph shapes to identify objects or states.

**Avoid using colors that make it hard to perceive content in your app.** For example,  insufficient contrast can cause icons and text to blend with the background and make content hard to read, and people who are color blind might not be able to distinguish some color combinations. For guidance, see [Accessibility](accessibility.md).

**Consider how the colors you use might be perceived in other countries and cultures.** For example, red communicates danger in some cultures, but has positive connotations in other cultures. Make sure the colors in your app send the message you intend.

## System colors

**Avoid hard-coding system color values in your app.** Documented color values are for your reference during the app design process. The actual color values may fluctuate from release to release, based on a variety of environmental variables. Use APIs like [Color](https://developer.apple.com/documentation/swiftui/color) to apply system colors.

iOS, iPadOS, macOS, and visionOS also define sets of *dynamic system colors* that match the color schemes of standard UI components and automatically adapt to both light and dark contexts. Each dynamic color is semantically defined by its purpose, rather than its appearance or color values. For example, some colors represent view backgrounds at different levels of hierarchy and other colors represent foreground content, such as labels, links, and separators.

**Avoid redefining the semantic meanings of dynamic system colors.** To ensure a consistent experience and ensure your interface looks great when the appearance of the platform changes, use dynamic system colors as intended. For example, don’t use the [separator](https://developer.apple.com/documentation/uikit/uicolor/separator) color as a text color, or [secondary text label](https://developer.apple.com/documentation/uikit/uicolor/secondarylabel) color as a background color.

## Liquid Glass color

By default, [Liquid Glass](materials.md#liquid-glass) has no inherent color, and instead takes on colors from the content directly behind it. You can apply color to some Liquid Glass elements, giving them the appearance of colored or stained glass. This is useful for drawing emphasis to a specific control, like a primary call to action, and is the approach the system uses for prominent button styling. Symbols or text labels on Liquid Glass controls can also have color.

For smaller elements like toolbars and tab bars, the system can adapt Liquid Glass between a light and dark appearance in response to the underlying content. By default, symbols and text on these elements follow a monochromatic color scheme, becoming darker when the underlying content is light, and lighter when it’s dark. Liquid Glass appears more opaque in larger elements like sidebars to preserve legibility over complex backgrounds and accommodate richer content on the material’s surface.

**Apply color sparingly to the Liquid Glass material, and to symbols or text on the material.** If you apply color, reserve it for elements that truly benefit from emphasis, such as status indicators or primary actions. To emphasize primary actions, apply color to the background rather than to symbols or text. For example, the system applies the app accent color to the background in prominent buttons — such as the Done button — to draw attention and elevate their visual prominence. Refrain from adding color to the background of multiple controls.

**Avoid using similar colors in control labels if your app has a colorful background.** While color can make apps more visually appealing, playful, or reflective of your brand, too much color can be overwhelming and make control labels more difficult to read. If your app features colorful backgrounds or visually rich content, prefer a monochromatic appearance for toolbars and tab bars, or choose an accent color with sufficient visual differentiation. By contrast, in apps with primarily monochromatic content or backgrounds, choosing your brand color as the app accent color can be an effective way to tailor your app experience and reflect your company’s identity.

**Be aware of the placement of color in the content layer.** Make sure your interface maintains sufficient contrast by avoiding overlap of similar colors in the content layer and controls when possible. Although colorful content might intermittently scroll underneath controls, make sure its default or resting state — like the top of a screen of scrollable content — maintains clear legibility.

## Color management

A *color space* represents the colors in a *color model* like RGB or CMYK. Common color spaces — sometimes called *gamuts* — are sRGB and Display P3.

A *color profile* describes the colors in a color space using, for example, mathematical formulas or tables of data that map colors to numerical representations. An image embeds its color profile so that a device can interpret the image’s colors correctly and reproduce them on a display.

**Apply color profiles to your images.** Color profiles help ensure that your app’s colors appear as intended on different displays. The sRGB color space produces accurate colors on most displays.

**Use wide color to enhance the visual experience on compatible displays.** Wide color displays support a P3 color space, which can produce richer, more saturated colors than sRGB. As a result, photos and videos that use wide color are more lifelike, and visual data and status indicators that use wide color can be more meaningful. When appropriate, use the Display P3 color profile at 16 bits per pixel (per channel) and export images in PNG format. Note that you need to use a wide color display to design wide color images and select P3 colors.

**Provide color space–specific image and color variations if necessary.** In general, P3 colors and images appear fine on sRGB displays. Occasionally, it may be hard to distinguish two very similar P3 colors when viewing them on an sRGB display. Gradients that use P3 colors can also sometimes appear clipped on sRGB displays. To avoid these issues and to ensure visual fidelity on both wide color and sRGB displays, you can use the asset catalog of your Xcode project to provide different versions of images and colors for each color space.

## Platform considerations

### Mobile (iOS, iPadOS)

iOS defines two sets of dynamic background colors — *system* and *grouped* — each of which contains primary, secondary, and tertiary variants that help you convey a hierarchy of information. In general, use the grouped background colors ([systemGroupedBackground](https://developer.apple.com/documentation/uikit/uicolor/systemgroupedbackground), [secondarySystemGroupedBackground](https://developer.apple.com/documentation/uikit/uicolor/secondarysystemgroupedbackground), and [tertiarySystemGroupedBackground](https://developer.apple.com/documentation/uikit/uicolor/tertiarysystemgroupedbackground)) when you have a grouped table view; otherwise, use the system set of background colors ([systemBackground](https://developer.apple.com/documentation/uikit/uicolor/systembackground), [secondarySystemBackground](https://developer.apple.com/documentation/uikit/uicolor/secondarysystembackground), and [tertiarySystemBackground](https://developer.apple.com/documentation/uikit/uicolor/tertiarysystembackground)).

With both sets of background colors, you generally use the variants to indicate hierarchy in the following ways:

- Primary for the overall view
- Secondary for grouping content or elements within the overall view
- Tertiary for grouping content or elements within secondary elements

For foreground content, iOS defines the following dynamic colors:

| Color | Use for… | UIKit API |
| --- | --- | --- |
| Label | A text label that contains primary content. | [label](https://developer.apple.com/documentation/uikit/uicolor/label) |
| Secondary label | A text label that contains secondary content. | [secondaryLabel](https://developer.apple.com/documentation/uikit/uicolor/secondarylabel) |
| Tertiary label | A text label that contains tertiary content. | [tertiaryLabel](https://developer.apple.com/documentation/uikit/uicolor/tertiarylabel) |
| Quaternary label | A text label that contains quaternary content. | [quaternaryLabel](https://developer.apple.com/documentation/uikit/uicolor/quaternarylabel) |
| Placeholder text | Placeholder text in controls or text views. | [placeholderText](https://developer.apple.com/documentation/uikit/uicolor/placeholdertext) |
| Separator | A separator that allows some underlying content to be visible. | [separator](https://developer.apple.com/documentation/uikit/uicolor/separator) |
| Opaque separator | A separator that doesn’t allow any underlying content to be visible. | [opaqueSeparator](https://developer.apple.com/documentation/uikit/uicolor/opaqueseparator) |
| Link | Text that functions as a link. | [link](https://developer.apple.com/documentation/uikit/uicolor/link) |

### Desktop (macOS)

macOS defines the following dynamic system colors (you can also view them in the Developer palette of the standard Color panel):

| Color | Use for… | AppKit API |
| --- | --- | --- |
| Alternate selected control text color | The text on a selected surface in a list or table. | [alternateSelectedControlTextColor](https://developer.apple.com/documentation/appkit/nscolor/alternateselectedcontroltextcolor) |
| Alternating content background colors | The backgrounds of alternating rows or columns in a list, table, or collection view. | [alternatingContentBackgroundColors](https://developer.apple.com/documentation/appkit/nscolor/alternatingcontentbackgroundcolors) |
| Control accent | The accent color people select in System Settings. | [controlAccentColor](https://developer.apple.com/documentation/appkit/nscolor/controlaccentcolor) |
| Control background color | The background of a large interface element, such as a browser or table. | [controlBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/controlbackgroundcolor) |
| Control color | The surface of a control. | [controlColor](https://developer.apple.com/documentation/appkit/nscolor/controlcolor) |
| Control text color | The text of a control that is available. | [controlTextColor](https://developer.apple.com/documentation/appkit/nscolor/controltextcolor) |
| Current control tint | The system-defined control tint. | [currentControlTint](https://developer.apple.com/documentation/appkit/nscolor/currentcontroltint) |
| Unavailable control text color | The text of a control that’s unavailable. | [disabledControlTextColor](https://developer.apple.com/documentation/appkit/nscolor/disabledcontroltextcolor) |
| Find highlight color | The color of a find indicator. | [findHighlightColor](https://developer.apple.com/documentation/appkit/nscolor/findhighlightcolor) |
| Grid color | The gridlines of an interface element, such as a table. | [gridColor](https://developer.apple.com/documentation/appkit/nscolor/gridcolor) |
| Header text color | The text of a header cell in a table. | [headerTextColor](https://developer.apple.com/documentation/appkit/nscolor/headertextcolor) |
| Highlight color | The virtual light source onscreen. | [highlightColor](https://developer.apple.com/documentation/appkit/nscolor/highlightcolor) |
| Keyboard focus indicator color | The ring that appears around the currently focused control when using the keyboard for interface navigation. | [keyboardFocusIndicatorColor](https://developer.apple.com/documentation/appkit/nscolor/keyboardfocusindicatorcolor) |
| Label color | The text of a label containing primary content. | [labelColor](https://developer.apple.com/documentation/appkit/nscolor/labelcolor) |
| Link color | A link to other content. | [linkColor](https://developer.apple.com/documentation/appkit/nscolor/linkcolor) |
| Placeholder text color | A placeholder string in a control or text view. | [placeholderTextColor](https://developer.apple.com/documentation/appkit/nscolor/placeholdertextcolor) |
| Quaternary label color | The text of a label of lesser importance than a tertiary label, such as watermark text. | [quaternaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/quaternarylabelcolor) |
| Secondary label color | The text of a label of lesser importance than a primary label, such as a label used to represent a subheading or additional information. | [secondaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/secondarylabelcolor) |
| Selected content background color | The background for selected content in a key window or view. | [selectedContentBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/selectedcontentbackgroundcolor) |
| Selected control color | The surface of a selected control. | [selectedControlColor](https://developer.apple.com/documentation/appkit/nscolor/selectedcontrolcolor) |
| Selected control text color | The text of a selected control. | [selectedControlTextColor](https://developer.apple.com/documentation/appkit/nscolor/selectedcontroltextcolor) |
| Selected menu item text color | The text of a selected menu. | [selectedMenuItemTextColor](https://developer.apple.com/documentation/appkit/nscolor/selectedmenuitemtextcolor) |
| Selected text background color | The background of selected text. | [selectedTextBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/selectedtextbackgroundcolor) |
| Selected text color | The color for selected text. | [selectedTextColor](https://developer.apple.com/documentation/appkit/nscolor/selectedtextcolor) |
| Separator color | A separator between different sections of content. | [separatorColor](https://developer.apple.com/documentation/appkit/nscolor/separatorcolor) |
| Shadow color | The virtual shadow cast by a raised object onscreen. | [shadowColor](https://developer.apple.com/documentation/appkit/nscolor/shadowcolor) |
| Tertiary label color | The text of a label of lesser importance than a secondary label. | [tertiaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/tertiarylabelcolor) |
| Text background color | The background color behind text. | [textBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/textbackgroundcolor) |
| Text color | The text in a document. | [textColor](https://developer.apple.com/documentation/appkit/nscolor/textcolor) |
| Under page background color | The background behind a document’s content. | [underPageBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/underpagebackgroundcolor) |
| Unemphasized selected content background color | The selected content in a non-key window or view. | [unemphasizedSelectedContentBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/unemphasizedselectedcontentbackgroundcolor) |
| Unemphasized selected text background color | A background for selected text in a non-key window or view. | [unemphasizedSelectedTextBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/unemphasizedselectedtextbackgroundcolor) |
| Unemphasized selected text color | Selected text in a non-key window or view. | [unemphasizedSelectedTextColor](https://developer.apple.com/documentation/appkit/nscolor/unemphasizedselectedtextcolor) |
| Window background color | The background of a window. | [windowBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/windowbackgroundcolor) |
| Window frame text color | The text in the window’s title bar area. | [windowFrameTextColor](https://developer.apple.com/documentation/appkit/nscolor/windowframetextcolor) |

#### App accent colors

Beginning in macOS 11, you can specify an *accent color* to customize the appearance of your app’s buttons, selection highlighting, and sidebar icons. The system applies your accent color when the current value in General > Accent color settings is *multicolor*.

If people set their accent color setting to a value other than multicolor, the system applies their chosen color to the relevant items throughout your app, replacing your accent color. The exception is a sidebar icon that uses a fixed color you specify. Because a fixed-color sidebar icon uses a specific color to provide meaning, the system doesn’t override its color when people change the value of accent color settings. For guidance, see [Sidebars](sidebars.md).

## Specifications

### System colors

| Name | SwiftUI API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
| --- | --- | --- | --- | --- | --- |
| Red | [red](https://developer.apple.com/documentation/swiftui/color/red) | *image: colors unified red light* | *image: colors unified red dark* | *image: colors unified accessible red light* | *image: colors unified accessible red dark* |
| Orange | [orange](https://developer.apple.com/documentation/swiftui/color/orange) | *image: colors unified orange light* | *image: colors unified orange dark* | *image: colors unified accessible orange light* | *image: colors unified accessible orange dark* |
| Yellow | [yellow](https://developer.apple.com/documentation/swiftui/color/yellow) | *image: colors unified yellow light* | *image: colors unified yellow dark* | *image: colors unified accessible yellow light* | *image: colors unified accessible yellow dark* |
| Green | [green](https://developer.apple.com/documentation/swiftui/color/green) | *image: colors unified green light* | *image: colors unified green dark* | *image: colors unified accessible green light* | *image: colors unified accessible green dark* |
| Mint | [mint](https://developer.apple.com/documentation/swiftui/color/mint) | *image: colors unified mint light* | *image: colors unified mint dark* | *image: colors unified accessible mint light* | *image: colors unified accessible mint dark* |
| Teal | [teal](https://developer.apple.com/documentation/swiftui/color/teal) | *image: colors unified teal light* | *image: colors unified teal dark* | *image: colors unified accessible teal light* | *image: colors unified accessible teal dark* |
| Cyan | [cyan](https://developer.apple.com/documentation/swiftui/color/cyan) | *image: colors unified cyan light* | *image: colors unified cyan dark* | *image: colors unified accessible cyan light* | *image: colors unified accessible cyan dark* |
| Blue | [blue](https://developer.apple.com/documentation/swiftui/color/blue) | *image: colors unified blue light* | *image: colors unified blue dark* | *image: colors unified accessible blue light* | *image: colors unified accessible blue dark* |
| Indigo | [indigo](https://developer.apple.com/documentation/swiftui/color/indigo) | *image: colors unified indigo light* | *image: colors unified indigo dark* | *image: colors unified accessible indigo light* | *image: colors unified accessible indigo dark* |
| Purple | [purple](https://developer.apple.com/documentation/swiftui/color/purple) | *image: colors unified purple light* | *image: colors unified purple dark* | *image: colors unified accessible purple light* | *image: colors unified accessible purple dark* |
| Pink | [pink](https://developer.apple.com/documentation/swiftui/color/pink) | *image: colors unified pink light* | *image: colors unified pink dark* | *image: colors unified accessible pink light* | *image: colors unified accessible pink dark* |
| Brown | [brown](https://developer.apple.com/documentation/swiftui/color/brown) | *image: colors unified brown light* | *image: colors unified brown dark* | *image: colors unified accessible brown light* | *image: colors unified accessible brown dark* |

visionOS system colors use the default dark color values.

### iOS, iPadOS system gray colors

| Name | UIKit API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
| --- | --- | --- | --- | --- | --- |
| Gray | [systemGray](https://developer.apple.com/documentation/uikit/uicolor/systemgray) | *image: ios default systemgray* | *image: ios default systemgraydark* | *image: ios accessible systemgray* | *image: ios accessible systemgraydark* |
| Gray (2) | [systemGray2](https://developer.apple.com/documentation/uikit/uicolor/systemgray2) | *image: ios default systemgray2* | *image: ios default systemgray2dark* | *image: ios accessible systemgray2* | *image: ios accessible systemgray2dark* |
| Gray (3) | [systemGray3](https://developer.apple.com/documentation/uikit/uicolor/systemgray3) | *image: ios default systemgray3* | *image: ios default systemgray3dark* | *image: ios accessible systemgray3* | *image: ios accessible systemgray3dark* |
| Gray (4) | [systemGray4](https://developer.apple.com/documentation/uikit/uicolor/systemgray4) | *image: ios default systemgray4* | *image: ios default systemgray4dark* | *image: ios accessible systemgray4* | *image: ios accessible systemgray4dark* |
| Gray (5) | [systemGray5](https://developer.apple.com/documentation/uikit/uicolor/systemgray5) | *image: ios default systemgray5* | *image: ios default systemgray5dark* | *image: ios accessible systemgray5* | *image: ios accessible systemgray5dark* |
| Gray (6) | [systemGray6](https://developer.apple.com/documentation/uikit/uicolor/systemgray6) | *image: ios default systemgray6* | *image: ios default systemgray6dark* | *image: ios accessible systemgray6* | *image: ios accessible systemgray6dark* |

In SwiftUI, the equivalent of `systemGray` is [gray](https://developer.apple.com/documentation/swiftui/color/gray).

## Change log

| Date | Changes |
| --- | --- |
| December 16, 2025 | Updated guidance for Liquid Glass. |
| June 9, 2025 | Updated system color values, and added guidance for Liquid Glass. |
| February 2, 2024 | Distinguished UIKit and SwiftUI gray colors in iOS and iPadOS, and added guidance for balancing brightness levels in visionOS apps. |
| September 12, 2023 | Enhanced guidance for using background color in watchOS views, and added color swatches for tvOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance for using background color in watchOS. |
| December 19, 2022 | Corrected RGB values for system mint color (Dark Mode) in iOS and iPadOS. |

## Related guidelines

- [Dark Mode](dark-mode.md)
- [Accessibility](accessibility.md)
- [Materials](materials.md)

---


<a id="dark-mode"></a>
## dark-mode

# Dark Mode

> Source: <https://developer.apple.com/design/human-interface-guidelines/dark-mode>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS omitted)
> Last change on Apple's site: 2024-08-06 (Added art contrasting the light and dark appearances.)

Dark Mode is a systemwide appearance setting that uses a dark color palette to provide a comfortable viewing experience tailored for low-light environments.

---

In iOS, iPadOS, macOS, and tvOS, people often choose Dark Mode as their default interface style, and they generally expect all apps and games to respect their preference. In Dark Mode, the system uses a dark color palette for all screens, views, menus, and controls, and may also use greater perceptual contrast to make foreground content stand out against the darker backgrounds.

## Best practices

**Avoid offering an app-specific appearance setting.** An app-specific appearance mode option creates more work for people because they have to adjust more than one setting to get the appearance they want. Worse, they may think your app is broken because it doesn’t respond to their systemwide appearance choice.

**Ensure that your app looks good in both appearance modes.** In addition to using one mode or the other, people can choose the Auto appearance setting, which switches between the light and dark appearances as conditions change throughout the day, potentially while your app is running.

**Test your content to make sure that it remains comfortably legible in both appearance modes.** For example, in Dark Mode with Increase Contrast and Reduce Transparency turned on (both separately and together), you may find places where dark text is less legible when it’s on a dark background. You might also find that turning on Increase Contrast in Dark Mode can result in reduced visual contrast between dark text and a dark background. Although people with strong vision might still be able to read lower contrast text, such text could be illegible for many. For guidance, see [Accessibility](accessibility.md).

**In rare cases, consider using only a dark appearance in the interface.** For example, it can make sense for an app that supports immersive media viewing to use a permanently dark appearance that lets the UI recede and helps people focus on the media.

## Dark Mode colors

The color palette in Dark Mode includes dimmer background colors and brighter foreground colors. It’s important to realize that these colors aren’t necessarily inversions of their light counterparts: while many colors are inverted, some are not. For more information, see [Specifications](color.md#specifications).

**Embrace colors that adapt to the current appearance.** Semantic colors (like [labelColor](https://developer.apple.com/documentation/appkit/nscolor/labelcolor) and [controlColor](https://developer.apple.com/documentation/appkit/nscolor/controlcolor) in macOS or [separator](https://developer.apple.com/documentation/uikit/uicolor/separator) in iOS and iPadOS) automatically adapt to the current appearance. When you need a custom color, add a Color Set asset to your app’s asset catalog in Xcode, and specify the bright and dim variants of the color. Avoid using hard-coded color values or colors that don’t adapt.

**Aim for sufficient color contrast in all appearances.** Using system-defined colors can help you achieve a good contrast ratio between your foreground and background content. At a minimum, make sure the contrast ratio between colors is no lower than 4.5:1. For custom foreground and background colors, strive for a contrast ratio of 7:1, especially in small text. This ratio ensures that your foreground content stands out from the background, and helps your content meet recommended accessibility guidelines.

**Soften the color of white backgrounds.** If you display a content image that includes a white background, consider slightly darkening the image to prevent the background from glowing in the surrounding Dark Mode context.

### Icons and images

The system uses [SF Symbols](sf-symbols.md) (which automatically adapt to Dark Mode) and full-color images that are optimized for both the light and dark appearances.

**Use SF Symbols wherever possible.** Symbols work well in both appearance modes when you use dynamic colors to tint them or when you add vibrancy. For guidance, see [Color](color.md).

**Design separate interface icons for the light and dark appearances if necessary.** For example, an icon that depicts a full moon might need a subtle dark outline to contrast well with a light background, but need no outline when it displays on a dark background. Similarly, an icon that represents a drop of oil might need a slight border to make the edge visible against a dark background.

**Make sure full-color images and icons look good in both appearances.** Use the same asset if it looks good in both the light and dark appearances. If an asset looks good in only one mode, modify the asset or create separate light and dark assets. Use asset catalogs to combine your assets into a single named image.

### Text

The system uses vibrancy and increased contrast to maintain the legibility of text on darker backgrounds.

**Use the system-provided label colors for labels.** The primary, secondary, tertiary, and quaternary label colors adapt automatically to the light and dark appearances.

**Use system views to draw text fields and text views.** System views and controls make your app’s text look good on all backgrounds, adjusting automatically for the presence or absence of vibrancy. When possible, use a system-provided view to display text instead of drawing the text yourself.

## Platform considerations

### Mobile (iOS, iPadOS)

In Dark Mode, the system uses two sets of background colors — called *base* and *elevated* — to enhance the perception of depth when one dark interface is layered above another. The base colors are dimmer, making background interfaces appear to recede, and the elevated colors are brighter, making foreground interfaces appear to advance.

**Prefer the system background colors.** Dark Mode is dynamic, which means that the background color automatically changes from base to elevated when an interface is in the foreground, such as a popover or modal sheet. The system also uses the elevated background color to provide visual separation between apps in a multitasking environment and between windows in a multiple-window context. Using a custom background color can make it harder for people to perceive these system-provided visual distinctions.

### Desktop (macOS)

When people choose the graphite accent color in General settings, macOS causes window backgrounds to pick up color from the current desktop picture. The result — called *desktop tinting* — is a subtle effect that helps windows blend more harmoniously with their surrounding content.

**Include some transparency in custom component backgrounds when appropriate.** Transparency lets your components pick up color from the window background when desktop tinting is active, creating a visual harmony that can persist even when the desktop picture changes. To help achieve this harmony, add transparency only to a custom component that has a visible background or bezel, and only when the component is in a neutral state, such as state that doesn’t use color. You don’t want to add transparency when the component is in a state that uses color, because doing so can cause the component’s color to fluctuate when the window background adjusts to a different location on the desktop or when the desktop picture changes.

## Change log

| Date | Changes |
| --- | --- |
| August 6, 2024 | Added art contrasting the light and dark appearances. |

## Related guidelines

- [Color](color.md)
- [Materials](materials.md)
- [Typography](typography.md)

---


<a id="icons"></a>
## icons

# Icons

> Source: <https://developer.apple.com/design/human-interface-guidelines/icons>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-06-09 (Added a table of SF Symbols that represent common actions.)

An effective icon is a graphic asset that expresses a single concept in ways people instantly understand.

---

Apps and games use a variety of simple icons to help people understand the items, actions, and modes they can choose. Unlike [app icons](app-icons.md), which can use rich visual details like shading, texturing, and highlighting to evoke the app’s personality, an *interface icon* typically uses streamlined shapes and touches of color to communicate a straightforward idea.

You can design interface icons — also called *glyphs* — or you can choose symbols from the SF Symbols app, using them as-is or customizing them to suit your needs. Both interface icons and symbols use black and clear colors to define their shapes; the system can apply other colors to the black areas in each image. For guidance, see [SF Symbols](sf-symbols.md).

## Best practices

**Create a recognizable, highly simplified design.** Too many details can make an interface icon confusing or unreadable. Strive for a simple, universal design that most people will recognize quickly. In general, icons work best when they use familiar visual metaphors that are directly related to the actions they initiate or content they represent.

**Maintain visual consistency across all interface icons in your app.** Whether you use only custom icons or mix custom and system-provided ones, all interface icons in your app need to use a consistent size, level of detail, stroke thickness (or weight), and perspective. Depending on the visual weight of an icon, you may need to adjust its dimensions to ensure that it appears visually consistent with other icons.

**In general, match the weights of interface icons and adjacent text.** Unless you want to emphasize either the icons or the text, using the same weight for both gives your content a consistent appearance and level of emphasis.

**If necessary, add padding to a custom interface icon to achieve optical alignment.** Some icons — especially asymmetric ones — can look unbalanced when you center them geometrically instead of optically. For example, the download icon shown below has more visual weight on the bottom than on the top, which can make it look too low if it’s geometrically centered.

In such cases, you can slightly adjust the position of the icon until it’s optically centered. When you create an asset that includes your adjustments as padding around an interface icon (as shown below on the right), you can optically center the icon by geometrically centering the asset.

Adjustments for optical centering are typically very small, but they can have a big impact on your app’s appearance.

**Provide a selected-state version of an interface icon only if necessary.** You don’t need to provide selected and unselected appearances for an icon that’s used in standard system components such as toolbars, tab bars, and buttons. The system updates the visual appearance of the selected state automatically.

**Use inclusive images.** Consider how your icons can be understandable and welcoming to everyone. Prefer depicting gender-neutral human figures and avoid images that might be hard to recognize across different cultures or languages. For guidance, see [Inclusion](inclusion.md).

**Include text in your design only when it’s essential for conveying meaning.** For example, using a character in an interface icon that represents text formatting can be the most direct way to communicate the concept. If you need to display individual characters in your icon, be sure to localize them. If you need to suggest a passage of text, design an abstract representation of it, and include a flipped version of the icon to use when the context is right-to-left. For guidance, see [Right to left](right-to-left.md).

**If you create a custom interface icon, use a vector format like PDF or SVG.** The system automatically scales a vector-based interface icon for high-resolution displays, so you don’t need to provide high-resolution versions of it. In contrast, PNG — used for app icons and other images that include effects like shading, textures, and highlighting — doesn’t support scaling, so you have to supply multiple versions for each PNG-based interface icon. Alternatively, you can create a custom SF Symbol and specify a scale that ensures the symbol’s emphasis matches adjacent text. For guidance, see [SF Symbols](sf-symbols.md).

**Provide alternative text labels for custom interface icons.** Alternative text labels — or accessibility descriptions — aren’t visible, but they let VoiceOver audibly describe what’s onscreen, simplifying navigation for people with visual disabilities. For guidance, see [VoiceOver](voiceover.md).

**Avoid using replicas of Apple hardware products.** Hardware designs tend to change frequently and can make your interface icons and other content appear dated. If you must display Apple hardware, use only the images available in [Apple Design Resources](https://developer.apple.com/design/resources/) or the SF Symbols that represent various Apple products.

## Standard icons

For icons to represent common actions in [menus](menus.md), [toolbars](toolbars.md), [buttons](buttons.md), and other places in interfaces across Apple platforms, you can use these [SF Symbols](sf-symbols.md).

### Editing

| Action | Icon | Symbol name |
| --- | --- | --- |
| Cut | *image: icons symbols meaning cut* | `scissors` |
| Copy | *image: icons symbols meaning copy* | `document.on.document` |
| Paste | *image: icons symbols meaning paste* | `document.on.clipboard` |
| Done | *image: icons symbols meaning done save* | `checkmark ` |
| Save | *image: icons symbols meaning done save* | `checkmark ` |
| Cancel | *image: icons symbols meaning close cancel* | `xmark` |
| Close | *image: icons symbols meaning close cancel* | `xmark` |
| Delete | *image: icons symbols meaning delete* | `trash` |
| Undo | *image: icons symbols meaning undo* | `arrow.uturn.backward` |
| Redo | *image: icons symbols meaning redo* | `arrow.uturn.forward` |
| Compose | *image: icons symbols meaning compose* | `square.and.pencil` |
| Duplicate | *image: icons symbols meaning duplicate* | `plus.square.on.square` |
| Rename | *image: icons symbols meaning rename* | `pencil` |
| Move to | *image: icons symbols meaning move to folder* | `folder` |
| Folder | *image: icons symbols meaning move to folder* | `folder` |
| Attach | *image: icons symbols meaning attach* | `paperclip` |
| Add | *image: icons symbols meaning add* | `plus` |
| More | *image: icons symbols meaning more* | `ellipsis` |

### Selection

| Action | Icon | Symbol name |
| --- | --- | --- |
| Select | *image: icons symbols meaning select all* | `checkmark.circle` |
| Deselect | *image: icons symbols meaning deselect close* | `xmark` |
| Close | *image: icons symbols meaning deselect close* | `xmark` |
| Delete | *image: icons symbols meaning delete* | `trash` |

### Text formatting

| Action | Icon | Symbol name |
| --- | --- | --- |
| Superscript | *image: icons symbols meaning superscript* | `textformat.superscript` |
| Subscript | *image: icons symbols meaning subscript* | `textformat.subscript` |
| Bold | *image: icons symbols meaning bold* | `bold` |
| Italic | *image: icons symbols meaning italic* | `italic` |
| Underline | *image: icons symbols meaning underline* | `underline` |
| ​​Align Left | *image: icons symbols meaning align left* | `text.alignleft` |
| Center | *image: icons symbols meaning align center* | `text.aligncenter` |
| Justified | *image: icons symbols meaning align justified* | `text.justify` |
| Align Right | *image: icons symbols meaning align right* | `text.alignright` |

### Search

| Action | Icon | Symbol name |
| --- | --- | --- |
| Search | *image: icons symbols meaning search* | `magnifyingglass` |
| Find | *image: icons symbols meaning find* | `text.page.badge.magnifyingglass` |
| Find and Replace | *image: icons symbols meaning find* | `text.page.badge.magnifyingglass` |
| Find Next | *image: icons symbols meaning find* | `text.page.badge.magnifyingglass` |
| Find Previous | *image: icons symbols meaning find* | `text.page.badge.magnifyingglass` |
| Use Selection for Find | *image: icons symbols meaning find* | `text.page.badge.magnifyingglass` |
| Filter | *image: icons symbols meaning filter* | `line.3.horizontal.decrease` |

### Sharing and exporting

| Action | Icon | Symbol name |
| --- | --- | --- |
| Share | *image: icons symbols meaning sharing* | `square.and.arrow.up` |
| Export | *image: icons symbols meaning sharing* | `square.and.arrow.up` |
| Print | *image: icons symbols meaning print* | `printer` |

### Users and accounts

| Action | Icon | Symbol name |
| --- | --- | --- |
| Account | *image: icons symbols meaning account user* | `person.crop.circle` |
| User | *image: icons symbols meaning account user* | `person.crop.circle` |
| Profile | *image: icons symbols meaning account user* | `person.crop.circle` |

### Ratings

| Action | Icon | Symbol name |
| --- | --- | --- |
| Dislike | *image: icons symbols meaning dislike* | `hand.thumbsdown` |
| Like | *image: icons symbols meaning like* | `hand.thumbsup` |

### Layer ordering

| Action | Icon | Symbol name |
| --- | --- | --- |
| Bring to Front | *image: icons symbols meaning bring to front* | `square.3.layers.3d.top.filled` |
| Send to Back | *image: icons symbols meaning send to back* | `square.3.layers.3d.bottom.filled` |
| Bring Forward | *image: icons symbols meaning bring forward* | `square.2.layers.3d.top.filled` |
| Send Backward | *image: icons symbols meaning send backwards* | `square.2.layers.3d.bottom.filled` |

### Other

| Action | Icon | Symbol name |
| --- | --- | --- |
| Alarm | *image: icons symbols meaning alarm* | `alarm` |
| Archive | *image: icons symbols meaning archive* | `archivebox` |
| Calendar | *image: icons symbols meaning calendar* | `calendar` |

## Platform considerations

*No additional considerations for iOS, iPadOS, tvOS, visionOS, or watchOS.*

### Desktop (macOS)

#### Document icons

If your macOS app can use a custom document type, you can create a document icon to represent it. Traditionally, a document icon looks like a piece of paper with its top-right corner folded down. This distinctive appearance helps people distinguish documents from apps and other content, even when icon sizes are small.

If you don’t supply a document icon for a file type you support, macOS creates one for you by compositing your app icon and the file’s extension onto the canvas. For example, Preview uses a system-generated document icon to represent JPG files.

In some cases, it can make sense to create a set of document icons to represent a range of file types your app handles. For example, Xcode uses custom document icons to help people distinguish projects, AR objects, and Swift code files.

To create a custom document icon, you can supply any combination of background fill, center image, and text. The system layers, positions, and masks these elements as needed and composites them onto the familiar folded-corner icon shape.

**Design simple images that clearly communicate the document type.** Whether you use a background fill, a center image, or both, prefer uncomplicated shapes and a reduced palette of distinct colors. Your document icon can display as small as 16x16 px, so you want to create designs that remain recognizable at every size.

**Designing a single, expressive image for the background fill can be a great way to help people understand and recognize a document type.** For example, Xcode and TextEdit both use rich background images that don’t include a center image.

**Consider reducing complexity in the small versions of your document icon.** Icon details that are clear in large versions can look blurry and be hard to recognize in small versions. For example, to ensure that the grid lines in the custom heart document icon remain clear in intermediate sizes, you might use fewer lines and thicken them by aligning them to the reduced pixel grid. In the 16x16 px size, you might remove the lines altogether.

**Avoid placing important content in the top-right corner of your background fill.** The system automatically masks your image to fit the document icon shape and draws the white folded corner on top of the fill. Create a set of background images in the sizes listed below.

- 512x512 px @1x, 1024x1024 px @2x
- 256x256 px @1x, 512x512 px @2x
- 128x128 px @1x, 256x256 px @2x
- 32x32 px @1x, 64x64 px @2x
- 16x16 px @1x, 32x32 px @2x

**If a familiar object can convey a document’s type or its connection with your app, consider creating a center image that depicts it.** Design a simple, unambiguous image that’s clear and recognizable at every size. The center image measures half the size of the overall document icon canvas. For example, to create a center image for a 32x32 px document icon, use an image canvas that measures 16x16 px. You can provide center images in the following sizes:

- 256x256 px @1x, 512x512 px @2x
- 128x128 px @1x, 256x256 px @2x
- 32x32 px @1x, 64x64 px @2x
- 16x16 px @1x, 32x32 px @2x

**Define a margin that measures about 10% of the image canvas and keep most of the image within it.** Although parts of the image can extend into this margin for optical alignment, it’s best when the image occupies about 80% of the image canvas. For example, most of the center image in a 256x256 px canvas would fit in an area that measures 205x205 px.

**Specify a succinct term if it helps people understand your document type.** By default, the system displays a document’s extension at the bottom edge of the document icon, but if the extension is unfamiliar you can supply a more descriptive term. For example, the document icon for a SceneKit scene file uses the term *scene* instead of the file extension *scn*. The system automatically scales the extension text to fit in the document icon, so be sure to use a term that’s short enough to be legible at small sizes. By default, the system capitalizes every letter in the text.

## Change log

| Date | Changes |
| --- | --- |
| June 9, 2025 | Added a table of SF Symbols that represent common actions. |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [App icons](app-icons.md)
- [SF Symbols](sf-symbols.md)

---


<a id="images"></a>
## images

# Images

> Source: <https://developer.apple.com/design/human-interface-guidelines/images>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-12-16 (Added guidance for spatial photos and spatial scenes in visionOS.)

To make sure your artwork looks great on all devices you support, learn how the system displays content and how to deliver art at the appropriate scale factors.

---

## Resolution

Different devices can display images at different resolutions. For example, a 2D device displays images according to the resolution of its screen.

A *point* is an abstract unit of measurement that helps visual content remain consistent regardless of how it’s displayed. In 2D platforms, a point maps to a number of pixels that can vary according to the resolution of the display; in visionOS, a point is an angular value that allows visual content to scale according to its distance from the viewer.

When creating bitmap images, you specify a *scale factor* which determines the resolution of an image. You can visualize scale factor by considering the density of pixels per point in 2D displays of various resolutions. For example, a scale factor of 1 (also called @1x) describes a 1:1 pixel density, where one pixel is equal to one point. High-resolution 2D displays have higher pixel densities, such as 2:1 or 3:1. A 2:1 density (called @2x) has a scale factor of 2, and a 3:1 density (called @3x) has a scale factor of 3. Because of higher pixel densities, high-resolution displays demand images with more pixels.

**Provide high-resolution assets for all bitmap images in your app, for every device you support.** As you add each image to your project’s asset catalog, identify its scale factor by appending “@1x,” “@2x,” or “@3x” to its filename. Use the following values for guidance; for additional scale factors, see [Layout](layout.md).

| Platform | Scale factors |
| --- | --- |
| iPadOS, watchOS | @2x |
| iOS | @2x and @3x |
| macOS, tvOS | @1x and @2x |

**In general, design images at the lowest resolution and scale them up to create high-resolution assets.** When you use resizable vectorized shapes, you might want to position control points at whole values so that they’re cleanly aligned at 1x. This positioning allows the points to remain cleanly aligned to the raster grid at higher resolutions, because 2x and 3x are multiples of 1x.

## Formats

As you create different types of images, consider the following recommendations.

| Image type | Format |
| --- | --- |
| Bitmap or raster work | De-interlaced PNG files |
| PNG graphics that don’t require full 24-bit color | An 8-bit color palette |
| Photos | JPEG files, optimized as necessary, or HEIC files |
| Stereo or spatial photos | Stereo HEIC |
| Flat icons, interface icons, and other flat artwork that requires high-resolution scaling | PDF or SVG files |

## Best practices

**Include a color profile with each image.** Color profiles help ensure that your app’s colors appear as intended on different displays. For guidance, see [Color management](color.md#color-management).

**Always test images on a range of actual devices.** An image that looks great at design time may appear pixelated, stretched, or compressed when viewed on various devices.

## Platform considerations

*No additional considerations for iOS, iPadOS, or macOS.*

## Change log

| Date | Changes |
| --- | --- |
| December 16, 2025 | Added guidance for spatial photos and spatial scenes in visionOS. |
| December 5, 2023 | Clarified guidance on choosing a resolution for a rasterized image in a visionOS app. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Added specifications for Apple Watch Ultra. |

---


<a id="inclusion"></a>
## inclusion

# Inclusion

> Source: <https://developer.apple.com/design/human-interface-guidelines/inclusion>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)

Inclusive apps and games put people first by prioritizing respectful communication and presenting content and functionality in ways that everyone can access and understand.

---

To help you design an inclusive app or game, consider the following goals as you review the words and images you use and the experiences you offer.

As with all design, designing an inclusive app is an iterative process that takes time to get right. Throughout the process, be prepared to examine your assumptions about how other people think and feel and be open to evolving knowledge and understanding.

## Inclusive by design

Simple, intuitive experiences are at the core of well-designed apps and games. To design an intuitive experience, you start by investigating people’s goals and perspectives so you can present content that resonates with them.

Empathy is an important tool in this investigation because it helps you understand how people with different perspectives might respond to the content and experiences you create. For example, you might discover that from some perspectives a word or image is incomprehensible or has a meaning you don’t intend.

Although each person’s perspective comprises a unique intersection of human qualities that’s both distinct and dynamic, all perspectives arise from human characteristics and experiences that everyone shares, including:

- Age
- Gender and gender identity
- Race and ethnicity
- Sexuality
- Physical attributes
- Cognitive attributes
- Permanent, temporary, and situational disabilities
- Language and culture
- Religion
- Education
- Political or philosophical opinions
- Social and economic context

As you examine your app or game through different perspectives, avoid framing the work as merely a search for content that might give offense. Although no design should contain offensive material or experiences, an inoffensive app or game isn’t necessarily an inclusive one. Focusing on inclusion can help you avoid potentially offensive content while also helping you create a welcoming experience that everyone can enjoy.

## Welcoming language

Using plain, inclusive language welcomes everyone and helps them understand your app or game. Carefully review the writing in your experience to make sure that your tone and words don’t exclude people. Here are a few tips for writing text — also known as *copy* — that’s direct, easy to understand, and inclusive.

**Consider the tone of your copy from different perspectives.** The style of your writing communicates almost as much as the words you use. Although different apps use different communication styles, make sure the tone you use doesn’t send messages you don’t intend. For example, an academic tone can make an app or game seem like it welcomes only high levels of education. As you seek the style that’s right for your experience, be clear, direct, and respectful.

**Pay attention to how you refer to people.** It typically works well to use *you* and *your* to address people directly. Referring to people indirectly as *the user* or *the player* can make your experience feel distant and unwelcoming. Also, consider reserving words like *we* and *our* to represent your software or company; otherwise, these terms can suggest a personal relationship with people that might be interpreted as insulting or condescending.

**Avoid using specialized or technical terms without defining them.** Using specialized or technical terms can make your writing more succinct, but doing so excludes people who don’t know what the terms mean. If you must use such terms, be sure to define them first and make the definitions easy for people to look up. Even when people know the definition of a specialized or technical term in a sentence, the sentence is easier to read — and translate — when it uses plain language instead.

**Replace colloquial expressions with plain language.** Colloquial expressions are often culture-specific and can be difficult to translate. Worse, some colloquial phrases have exclusionary meanings you might not know. For example, the phrases *peanut gallery* and *grandfathered in* both arose from oppressive contexts and continue to exclude people. Even when a colloquial phrase doesn’t have an exclusionary meaning, it can still exclude everyone who doesn’t understand it.

**Consider carefully before including humor.** Humor is highly subjective and — similar to colloquial expressions — difficult to translate from one culture to another. Including humor in your experience risks confusing people who donʼt understand it, irritating people who tire of repeatedly encountering it, and insulting people who interpret it differently. For additional writing guidance, see [Writing inclusively](https://help.apple.com/applestyleguide/#/apdcb2a65d68).

## Being approachable

An approachable app or game doesn’t require people to have particular skills or knowledge before they can use it, and it gives people a clear path toward deepening their understanding over time. Here are two ways to help make an experience approachable.

- Present a clear, straightforward interface. To help you design a simple interface that fits in with other experiences on each platform, see [Designing for iOS](designing-for-ios.md), [Designing for iPadOS](designing-for-ipados.md), [Designing for macOS](designing-for-macos.md),  Designing for tvOS, Designing for visionOS, Designing for watchOS, and [Designing for games](designing-for-games.md).
- Build in ways to learn how to use your app or game. Consider designing an onboarding flow that helps people who are new to your experience take a step-by-step approach while letting others skip straight to the content they want. For guidance, see [Onboarding](onboarding.md).

## Gender identity

Throughout history, cultures around the world have recognized a spectrum of self-identity and expression that expands beyond the binary variants of woman and man.

You can help everyone feel welcome in your app or game by avoiding unnecessary references to specific genders. For example, a recipe-sharing app that uses copy like “You can let a subscriber post his or her recipes to your shared folder” could avoid unnecessary gender references by using an alternative like “Subscribers can post recipes to your shared folder.” In addition to using the gender-neutral noun “subscribers,” the revised copy avoids the unnecessary singular pronouns “his” and “her,” helping the sentence remain inclusive when it’s localized for languages that use gendered pronouns.

In addition, you can often avoid referencing a specific gender in an avatar, emoji, glyph, or game character. To welcome everyone to your app or game, prefer giving people the tools they need to customize such items as they choose.

If you need to depict a generic person or people, use a nongendered human image to reinforce the message that *generic person* means *human*, not *man* or *woman*. SF Symbols provides many nongendered glyphs you can use, such as the figure and person symbols shown here:

Most apps and games don’t need to know a person’s gender, but if you require this information — such as for health or legal reasons — consider providing inclusive options, such as *nonbinary*, *self-identify*, and *decline to state*. In this situation, you could also let people specify the pronouns they use so you can address them properly when necessary.

## People and settings

Portraying human diversity is one of the most noticeable ways your app or game can welcome everyone. When people recognize others like themselves within an experience and its related materials, they’re less likely to feel excluded and can be more likely to think they’ll benefit from it.

As you create copy and images that represent people, portray a range of human characteristics and activities. For example, a fitness app could feature exercise moves demonstrated by people with different racial backgrounds, body types, ages, and physical capabilities. If you need to depict occupations or behaviors, avoid stereotypical representations, such as showing only male doctors, female nurses, or heroes and villains that may perpetuate real-world racial or gender stereotypes.

Also review the settings and objects you show. For example, showing high levels of affluence might make sense in some scenarios, but in other cases it can be unwelcoming and make an experience seem out of touch. When it makes sense in your app or game, prefer showing places, homes, activities, and items that are familiar and relatable to most people.

## Avoiding stereotypes

Everyone holds biases and stereotypes — often unconsciously — and it can be challenging to discover how they affect your thoughts. A goal of inclusive design is to become aware of your biases and generalizations so you can recognize where they might influence your design decisions.

For example, consider an app that helps people manage account access for various family members. If this app uses a stereotypical definition of *family* — such as a woman, a man, and their biological children — it’s likely to communicate this perspective in its copy and images. Because the app assumes that people’s families fit this narrow definition, it excludes everyone whose family is different.

Although the assumption made in the account-access app might seem like an obvious mistake, it’s important to realize that not all assumptions are so easy to spot. For example, consider an app or game that requires people to choose security questions they can answer for future identity confirmation, such as:

- What was your favorite subject in college?
- What was the make of your first car?
- How did you feel when you first saw a rainbow?

From some perspectives these questions refer to commonplace events, but all are based on experiences that not everyone has. Using a context-specific experience to communicate something is useless for everyone who doesn’t share that context and effectively excludes them. To create alternatives to the culture- and capability-specific questions above, you might reference more universal human experiences like:

- What’s your favorite activity?
- What was the name of your first friend?
- What quality describes you best?

Basing design decisions on stereotypes or assumptions inevitably leads to exclusion because generalizations can’t reflect the diversity of human perspectives. Avoiding assumptions and instead concentrating on inclusion can help you craft experiences that benefit everyone.

## Accessibility

An inclusive app or game is accessible to everyone. People rely on Apple’s accessibility features — such as VoiceOver, Display Accommodations, closed captioning, Switch Control, and Speak Screen — to customize their devices for their individual needs, so it’s essential to support these features.

It’s also essential to avoid assuming that any disability might prevent someone from wanting to enjoy the experience your software provides. Making an assumption like this can result in designs that limit the potential audience for your app or game. In contrast, when you make each experience accessible, you give everyone the opportunity to benefit from your app or game in ways that work for them.

To help you design an app or game that everyone can enjoy, remember that:

- Each disability is a spectrum. For example, visual disabilities range from low vision to complete blindness, and include things like color blindness, blurry vision, light sensitivity, and peripheral vision loss.
- Everyone can experience disabilities. In addition to disabilities that most people experience as they age, there are *temporary disabilities* — like short-term hearing loss due to an infection — and *situational disabilities* — like being unable to hear while on a noisy train — that can affect everyone at various times.

As you design content that welcomes people of all abilities, consider the following tips.

**Avoid images and language that exclude people with disabilities.** For example, include people with disabilities when you represent a variety of people, and avoid language that uses a disability to express a negative quality.

**Take a people-first approach when writing about people with disabilities.** For example, you could describe an individual’s accomplishments and goals before mentioning a disability they may have. If you’re writing about a specific person or community, find out how they self-identify; for more guidance, see [Writing about disability](https://help.apple.com/applestyleguide/#/apd49cbb2b06).

**Prioritize simplicity and perceivability.** Prefer familiar, consistent interactions that make tasks simple to perform, and ensure that everyone can perceive your content, whether they use sight, hearing, or touch.

To learn more about making your app or game accessible, see [Accessibility](accessibility.md).

## Languages

People expect to customize their device by choosing a language for text and a region for formatting values like date, time, and money. To welcome a global audience, first prepare your software to handle languages and regions other than your own — a process called *internationalization* — and provide translated text and resources for specific locales. For an overview of internationalization, see [Expanding your app to new markets](https://developer.apple.com/localization/); for developer guidance on localization, see [Localization](https://developer.apple.com/documentation/xcode/localization).

Creating an inclusive experience can also help you prepare for localization. For example, using plain language, avoiding unnecessary gender references, representing a variety of people, and avoiding stereotypes and culture-specific content, can put you in a good position to create versions of your software localized into more languages. Using [SF Symbols](sf-symbols.md) for the glyphs in your app or game can also help streamline localization. In addition to providing many language-specific glyphs, SF Symbols includes glyphs you can use in both left-to-right and right-to-left contexts; for guidance, see [Right to left](right-to-left.md).

As you localize your app or game and related content, also be aware of the ways you use color. Colors often have strong culture-specific meanings, so it’s essential to discover how people respond to specific colors in each locale you support. In some places, for example, white is associated with death or grief, whereas in other places, it’s associated with purity or peace. If you use color as a way to communicate, make sure your color choices communicate the same thing in each version of your software.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Related guidelines

- [Accessibility](accessibility.md)

---


<a id="layout"></a>
## layout

# Layout

> Source: <https://developer.apple.com/design/human-interface-guidelines/layout>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2026-09-09 (Updated guidance to reflect current best practices.)

A consistent layout that adapts across display sizes, orientations, and multitasking configurations helps people understand and enjoy your app or game on all their devices.

---

Your layout provides the structure for people to understand your content from the moment they open your app. Familiar relationships between controls and content let people use and discover features right away, and make your design feel at home on every platform.

Apple provides templates and layout guides that can help you integrate Apple technologies and design your apps and games to run on all Apple platforms. See [Apple Design Resources](https://developer.apple.com/design/resources/).

## Visual hierarchy

**Order content by relative importance.** People often start by viewing content in reading order — that is, from top to bottom and from the leading to trailing side — so place the most important items near the top and leading side of the window or display. To support right-to-left languages, prefer standard system components that can automatically adapt UI elements to better reflect each language’s natural reading order. For guidance, see [Right to left](right-to-left.md).

**Align elements to make them easier to scan, and use indentation to convey hierarchy.** Alignment makes an app look neat and organized, and can help people track content while scrolling or moving their eyes. People assume that aligned items are related to each other, and conversely, they perceive indented items as subordinate to the item they follow. Because of this, using alignment and indentation deliberately can help people understand your information hierarchy.

**Group related items to clearly express related information or functions.** For example, you might use negative space, container shapes, or separator lines to show which elements are related and which are unrelated.

**Use progressive disclosure to make layouts cleaner and easier to interact with.** An interface with too much content and too many choices makes it harder to find information quickly, and harder to understand the choices that are available. Use disclosure triangles, menus, or nested views to reduce how much content to initially display; or use scrollable sections to showcase additional content, which is particularly useful for media-focused apps like those for video, music, or books.

**Differentiate controls from content.** Take advantage of the Liquid Glass material on all platforms that support it to provide a distinct appearance for your controls. Instead of applying a solid or semi-opaque background color beneath controls, use a scroll edge effect to visually elevate controls above content. For guidance, see [Scroll views](scroll-views.md). For full-screen background content, be sure to extend it underneath sidebars, toolbars, and tab bars to fit the entire screen or window.

If scaling a background image to the full window edge results in components like sidebars or inspectors covering important parts of the image, you can use a background extension effect to flip and blur the image, mirroring it beneath adjacent components and providing the appearance that the background image extends beneath them. For developer guidance, see [backgroundExtensionEffect()](https://developer.apple.com/documentation/swiftui/view/backgroundextensioneffect()) and [UIBackgroundExtensionView](https://developer.apple.com/documentation/uikit/uibackgroundextensionview).

## Adaptability

Apps and games need to adapt to different display sizes, orientation changes, window sizes, and multitasking states. In iOS, iPadOS, tvOS, and visionOS, the system defines characteristics of the device environment that can affect the way your app or game looks. Use SwiftUI or Auto Layout to ensure that your interface adapts to them.

Here are some of the most common device and system characteristics that apps need to handle:

- Regular and compact horizontal and vertical [size classes](#size-classes)
- Different device screen sizes
- Different device orientations and aspect ratios
- System features like the Dynamic Island
- External display support, Display Zoom, and resizable windows on iPad and Mac
- Text-size changes
- Locale-based internationalization features like left-to-right/right-to-left layout direction, date/time/number formatting, font variation, and text length

**Design a layout that adapts gracefully and consistently.** People expect your experience to remain familiar when they rotate their device, resize a window, add another display, or switch to a different device. You can help ensure an adaptable interface by respecting system-defined safe areas, margins, and guides (where available) and specifying layout modifiers to fine-tune the placement of views in your interface.

Even if your app is locked to a certain orientation, such as a landscape-only game, it’s still important to ensure your interface resizes well to provide the best experience across devices and window sizes.

**Be prepared for text-size changes.** People use [Dynamic Type](typography.md#supporting-dynamic-type) to increase text size to be more readable, which occurs at the system level. Apps that don’t respond to this setting can be difficult or impossible to use for people who rely on this feature. Support Dynamic Type by adjusting your layout to accommodate text at larger sizes. For example, horizontally adjacent views may need to stack vertically to provide more space for text; table rows or other containers may need to grow in height so that text isn’t cropped or doesn’t overlap other content; and table rows with a single line of text by default might need to grow vertically to accommodate multiple lines of text.

To support Dynamic Type in your Unity-based game, use Apple’s accessibility plug-in (for developer guidance, see [Apple – Accessibility](https://github.com/apple/unityplugins/blob/main/plug-ins/Apple.Accessibility/Apple.Accessibility_Unity/Assets/Apple.Accessibility/Documentation~/Apple.Accessibility.md)). For guidance on displaying text in your app, see [Typography](typography.md).

**Preview your app on multiple devices, using different size classes, localizations, and text sizes.** You can streamline the testing process by first testing versions of your experience that use the largest and the smallest layouts. You can test on a simulated device in [Device Hub](https://developer.apple.com/documentation/xcode/device-hub) to check for clipping and other layout issues. For example, you can use Device Hub to make sure your layout looks great when your app is resized on iPad or in iPhone Mirroring on Mac.

**When necessary, scale background artwork in response to display changes.** Viewing your app or game in a different context — such as on a screen with a different aspect ratio — might make your artwork appear cropped, letterboxed, or pillarboxed. If this happens, don’t change the aspect ratio of the artwork; instead, scale it so that it fills the screen completely. Note that since windows can be very wide and short or tall and narrow, background artwork may often need to extend beyond what is typically visible in a more standard display aspect ratio.

### Size classes

In iOS and iPadOS, size classes are an indication of how much horizontal and vertical space is available to an app’s interface.

Each dimension — horizontal and vertical — is represented by one of two size classes: *compact* or *regular*. The horizontal size class determines whether an app is narrow (compact) or wide (regular), while the vertical size class determines whether it is short (compact) or tall (regular).

The system sets size classes based on the device type, [window](windows.md) configuration, and [multitasking](multitasking.md) state; for example, whether an app is full screen, in Slide Over, or mirrored from an iPhone to a Mac. Depending on their environment, iOS and iPadOS apps can exist in every combination of size classes.

For developer guidance, see [UITraitChangeObservable](https://developer.apple.com/documentation/uikit/uitraitchangeobservable-67e94) and [UserInterfaceSizeClass](https://developer.apple.com/documentation/swiftui/userinterfacesizeclass).

**Determine layout based on size classes, not device type or orientation.** Size classes describe the actual space available, regardless of whether an app is in portrait or landscape. Conversely, a device’s orientation and type (also called its *idiom*) aren’t useful for making layout decisions because they don’t provide your app with information about how much space is available.

Size classes also let your app’s interface adapt to a wide range of window sizes. For example, when a person runs your app in macOS with iPhone Mirroring, they can freely resize its width and height; or they can resize an iPad app when multitasking in iPadOS or when running it in macOS.

**Consider all possible combinations of size classes.** Your app can appear in a variety of size classes in both portrait and landscape aspect ratios, and it’s important to consider all of them to provide a good experience. A layout solely designed for landscape on iPhone with regular width and compact height might not take advantage of the vertical space available on iPad in landscape when someone resizes the window to regular height. Conversely, designing exclusively for compact portrait could leave extra space when someone resizes the app window to a regular width on iPad.

**Keep functionality the same as size classes change, and keep layout changes recognizable and familiar to the platform.** Don’t change your app’s functionality based on the space it occupies. However, you can change the amount of functionality that’s visible onscreen as the amount of space changes. Consider taking advantage of larger spaces to switch from a [tab bar](tab-bars.md) to a [sidebar](sidebars.md) or expose functionality that might otherwise be grouped into an overflow menu.

Similarly, while an app’s size classes might change when someone resizes it, its idiom — the device type it’s made for — remains the same: keep the layout recognizable and familiar to the platform even when resizing.

## Guides and safe areas

A *layout guide* defines a rectangular region that helps you position, align, and space your content on the screen. The system includes predefined layout guides that make it easy to apply standard margins around content and restrict the width of text for optimal readability. You can also define custom layout guides. For developer guidance, see [UILayoutGuide](https://developer.apple.com/documentation/uikit/uilayoutguide) and [NSLayoutGuide](https://developer.apple.com/documentation/appkit/nslayoutguide).

A *safe area* defines the area within a window that isn’t covered on the edge by a hardware feature or another view within the window, like a toolbar, tab bar, or status bar. Respecting the safe area is essential to make sure system UI and hardware features like the Dynamic Island don’t obstruct content and controls. For developer guidance, see [SafeAreaRegions](https://developer.apple.com/documentation/swiftui/safearearegions) and [Positioning content relative to the safe area](https://developer.apple.com/documentation/uikit/positioning-content-relative-to-the-safe-area).

## Platform considerations

*No additional considerations for iOS or iPadOS.*

### Desktop (macOS)

**Avoid placing controls or critical information at the bottom of a window.** People often move windows so that the bottom edge is below the bottom of the screen.

**Avoid displaying content behind the camera housing at the top edge of the window.** For developer guidance, see [NSPrefersDisplaySafeAreaCompatibilityMode](https://developer.apple.com/documentation/bundleresources/information-property-list/nsprefersdisplaysafeareacompatibilitymode).

## Change log

| Date | Changes |
| --- | --- |
| September 9, 2026 | Updated guidance to reflect current best practices. |
| September 9, 2025 | Added specifications for iPhone 17, iPhone Air, iPhone 17 Pro, iPhone 17 Pro Max, Apple Watch SE 3, Apple Watch Series 11, and Apple Watch Ultra 3. |
| June 9, 2025 | Added guidance for Liquid Glass. |
| March 7, 2025 | Added specifications for iPhone 16e, iPad 11-inch, iPad Air 11-inch, and iPad Air 13-inch. |
| September 9, 2024 | Added specifications for iPhone 16, iPhone 16 Plus, iPhone 16 Pro, iPhone 16 Pro Max, and Apple Watch Series 10. |
| June 10, 2024 | Made minor corrections and organizational updates. |
| February 2, 2024 | Enhanced guidance for avoiding system controls in iPadOS app layouts, and added specifications for 10.9-inch iPad Air and 8.3-inch iPad mini. |
| December 5, 2023 | Clarified guidance on centering content in a visionOS window. |
| September 15, 2023 | Added specifications for iPhone 15 Pro Max, iPhone 15 Pro, iPhone 15 Plus, iPhone 15, Apple Watch Ultra 2, and Apple Watch SE. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Added specifications for iPhone 14 Pro Max, iPhone 14 Pro, iPhone 14 Plus, iPhone 14, and Apple Watch Ultra. |

## Related guidelines

- [Right to left](right-to-left.md)

---


<a id="materials"></a>
## materials

# Materials

> Source: <https://developer.apple.com/design/human-interface-guidelines/materials>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-09-09 (Updated guidance for Liquid Glass.)

A material is a visual effect that creates a sense of depth, layering, and hierarchy between foreground and background elements.

---

Materials help visually separate foreground elements, such as text and controls, from background elements, such as content and solid colors. By allowing color to pass through from background to foreground, a material establishes visual hierarchy to help people more easily retain a sense of place.

Apple platforms feature two types of materials: Liquid Glass, and standard materials. [Liquid Glass](#liquid-glass) is a dynamic material that unifies the design language across Apple platforms, allowing you to present controls and navigation without obscuring underlying content. In contrast to Liquid Glass, the [standard materials](#standard-materials) help with visual differentiation within the content layer.

## Liquid Glass

Liquid Glass forms a distinct functional layer for controls and navigation elements — like tab bars and sidebars — that floats above the content layer, establishing a clear visual hierarchy between functional elements and content. Liquid Glass allows content to scroll and peek through from beneath these elements to give the interface a sense of dynamism and depth, all while maintaining legibility for controls and navigation.

**Don’t use Liquid Glass in the content layer.** Liquid Glass works best when it provides a clear distinction between interactive elements and content, and including it in the content layer can result in unnecessary complexity and a confusing visual hierarchy. Instead, use [standard materials](#standard-materials) for elements in the content layer, such as app backgrounds. An exception to this is for controls in the content layer with a transient interactive element like [sliders](sliders.md) and [toggles](toggles.md); in these cases, the element takes on a Liquid Glass appearance to emphasize its interactivity when a person activates it.

**Use Liquid Glass effects sparingly.** Standard components from system frameworks pick up the appearance and behavior of this material automatically. If you apply Liquid Glass effects to a custom control, do so sparingly. Liquid Glass seeks to bring attention to the underlying content, and overusing this material in multiple custom controls can provide a subpar user experience by distracting from that content. Limit these effects to the most important functional elements in your app. For developer guidance, see [Applying Liquid Glass to custom views](https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views).

**Only use clear Liquid Glass for components that appear over visually rich backgrounds.** Liquid Glass provides two variants — [regular](https://developer.apple.com/documentation/swiftui/glass/regular) and [clear](https://developer.apple.com/documentation/swiftui/glass/clear) — that you can choose when building custom components or styling some system components. The appearance of these variants can differ in response to certain system settings, like if people choose a preferred look for Liquid Glass in their device’s settings, or turn on accessibility settings that reduce transparency or increase contrast in the interface.

The *regular* variant blurs and adjusts the luminosity of background content to maintain legibility of text and other foreground elements. Scroll edge effects further enhance legibility by blurring and reducing the opacity of background content. Most system components use this variant. Use the regular variant when background content might create legibility issues, or when components have a significant amount of text, such as alerts, sidebars, or popovers.

The *clear* variant is highly translucent, which is ideal for prioritizing the visibility of the underlying content and ensuring visually rich background elements remain prominent. Use this variant for components that float above media backgrounds — such as photos and videos — to create a more immersive content experience.

For optimal contrast and legibility, determine whether to add a dimming layer behind components with clear Liquid Glass:

- If the underlying content is bright, consider adding a dark dimming layer of 35% opacity. For developer guidance, see [clear](https://developer.apple.com/documentation/swiftui/glass/clear).
- If the underlying content is sufficiently dark, or if you use standard media playback controls from AVKit that provide their own dimming layer, you don’t need to apply a dimming layer.

For guidance about the use of color, see [Liquid Glass color](color.md#liquid-glass-color).

## Standard materials

Use standard materials and effects — such as [blur](https://developer.apple.com/documentation/uikit/uiblureffect), [vibrancy](https://developer.apple.com/documentation/uikit/uivibrancyeffect), and [blending modes](https://developer.apple.com/documentation/appkit/nsvisualeffectview/blendingmode-swift.enum) — to convey a sense of structure in the content beneath Liquid Glass.

**Choose materials and effects based on semantic meaning and recommended usage.** Avoid selecting a material or effect based on the apparent color it imparts to your interface, because system settings can change its appearance and behavior. Instead, match the material or vibrancy style to your specific use case.

**Help ensure legibility by using vibrant colors on top of materials.** When you use system-defined vibrant colors, you don’t need to worry about colors seeming too dark, bright, saturated, or low contrast in different contexts. Regardless of the material you choose, use vibrant colors on top of it. For guidance, see [System colors](color.md#system-colors).

**Consider contrast and visual separation when choosing a material to combine with blur and vibrancy effects.** For example, consider that:

- Thicker materials, which are more opaque, can provide better contrast for text and other elements with fine features.
- Thinner materials, which are more translucent, can help people retain their context by providing a visible reminder of the content that’s in the background.

For developer guidance, see [Material](https://developer.apple.com/documentation/swiftui/material).

## Platform considerations

### Mobile (iOS, iPadOS)

In addition to Liquid Glass, iOS and iPadOS continue to provide four standard materials — ultra-thin, thin, regular (default), and thick — which you can use in the content layer to help create visual distinction.

iOS and iPadOS also define vibrant colors for labels, fills, and separators that are specifically designed to work with each material. Labels and fills both have several levels of vibrancy; separators have one level. The name of a level indicates the relative amount of contrast between an element and the background: The default level has the highest contrast, whereas quaternary (when it exists) has the lowest contrast.

Except for quaternary, you can use the following vibrancy values for labels on any material. In general, avoid using quaternary on top of the [thin](https://developer.apple.com/documentation/swiftui/material/thin) and [ultraThin](https://developer.apple.com/documentation/swiftui/material/ultrathin) materials, because the contrast is too low.

- [UIVibrancyEffectStyle.label](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/label) (default)
- [UIVibrancyEffectStyle.secondaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondarylabel)
- [UIVibrancyEffectStyle.tertiaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiarylabel)
- [UIVibrancyEffectStyle.quaternaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/quaternarylabel)

You can use the following vibrancy values for fills on all materials.

- [UIVibrancyEffectStyle.fill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/fill) (default)
- [UIVibrancyEffectStyle.secondaryFill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondaryfill)
- [UIVibrancyEffectStyle.tertiaryFill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiaryfill)

The system provides a single, default vibrancy value for a [separator](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/separator), which works well on all materials.

### Desktop (macOS)

macOS provides several standard materials with designated purposes, and vibrant versions of all [system colors](color.md#specifications). For developer guidance, see [NSVisualEffectView.Material](https://developer.apple.com/documentation/appkit/nsvisualeffectview/material-swift.enum).

**Choose when to allow vibrancy in custom views and controls.** Depending on configuration and system settings, system views and controls use vibrancy to make foreground content stand out against any background. Test your interface in a variety of contexts to discover when vibrancy enhances the appearance and improves communication.

**Choose a background blending mode that complements your interface design.** macOS defines two modes that blend background content: behind window and within window. For developer guidance, see [NSVisualEffectView.BlendingMode](https://developer.apple.com/documentation/appkit/nsvisualeffectview/blendingmode-swift.enum).

## Change log

| Date | Changes |
| --- | --- |
| September 9, 2025 | Updated guidance for Liquid Glass. |
| June 9, 2025 | Added guidance for Liquid Glass. |
| August 6, 2024 | Added platform-specific art. |
| December 5, 2023 | Updated descriptions of the various material types, and clarified terms related to vibrancy and material thickness. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Added guidance on using materials to provide context and orientation in watchOS apps. |

## Related guidelines

- [Color](color.md)
- [Accessibility](accessibility.md)
- [Dark Mode](dark-mode.md)

---


<a id="motion"></a>
## motion

# Motion

> Source: <https://developer.apple.com/design/human-interface-guidelines/motion>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-09-09 (Added guidance for Liquid Glass.)

Beautiful, fluid motions bring the interface to life, conveying status, providing feedback and instruction, and enriching the visual experience of your app or game.

---

Many system components automatically include motion, letting you offer familiar and consistent experiences throughout your app or game. System components might also adjust their motion in response to factors like accessibility settings or different input methods. For example, the movement of [Liquid Glass](materials.md#liquid-glass) responds to direct touch interaction with greater emphasis to reinforce the feeling of a tactile experience, but produces a more subdued effect when a person interacts using a trackpad.

If you design custom motion, follow the guidelines below.

## Best practices

**Add motion purposefully, supporting the experience without overshadowing it.** Don’t add motion for the sake of adding motion. Gratuitous or excessive animation can distract people and may make them feel disconnected or physically uncomfortable.

**Make motion optional.** Not everyone can or wants to experience the motion in your app or game, so it’s essential to avoid using it as the only way to communicate important information. To help everyone enjoy your app or game, supplement visual feedback by also using alternatives like [haptics](playing-haptics.md) and [audio](playing-audio.md) to communicate.

## Providing feedback

**Strive for realistic feedback motion that follows people’s gestures and expectations.** In nongame apps, accurate, realistic motion can help people understand how something works, but feedback motion that doesn’t make sense can make them feel disoriented. For example, if someone reveals a view by sliding it down from the top, they don’t expect to dismiss the view by sliding it to the side.

**Aim for brevity and precision in feedback animations.** When animated feedback is brief and precise, it tends to feel lightweight and unobtrusive, and it can often convey information more effectively than prominent animation. For example, when a game displays a succinct animation that’s precisely tied to a successful action, players can instantly get the message without being distracted from their gameplay. Another example is in visionOS: When people tap a panorama in Photos, it quickly and smoothly expands to fill the space in front of them, helping them track the transition without making them wait to enjoy the content.

**In apps, generally avoid adding motion to UI interactions that occur frequently.** The system already provides subtle animations for interactions with standard interface elements. For a custom element, you generally want to avoid making people spend extra time paying attention to unnecessary motion every time they interact with it.

**Let people cancel motion.** As much as possible, don’t make people wait for an animation to complete before they can do anything, especially if they have to experience the animation more than once.

**Consider using animated symbols where it makes sense.** When you use SF Symbols 5 or later, you can apply animations to SF Symbols or custom symbols. For guidance, see [Animations](sf-symbols.md#animations).

## Leveraging platform capabilities

**Make sure your game’s motion looks great by default on each platform you support.** In most games, maintaining a consistent frame rate of 30 to 60 fps typically results in a smooth, visually appealing experience. For each platform you support, use the device’s graphics capabilities to enable default settings that let people enjoy your game without first having to change those settings.

**Let people customize the visual experience of your game to optimize performance or battery life.** For example, consider letting people switch between power modes when the system detects the presence of an external power source.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, or tvOS.*

## Change log

| Date | Changes |
| --- | --- |
| September 9, 2025 | Added guidance for Liquid Glass. |
| June 10, 2024 | Added game-specific examples and enhanced guidance for using motion in games. |
| February 2, 2024 | Enhanced guidance for minimizing peripheral motion in visionOS apps. |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [Feedback](feedback.md)

---


<a id="privacy"></a>
## privacy

# Privacy

> Source: <https://developer.apple.com/design/human-interface-guidelines/privacy>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2023-06-21 (Consolidated guidance into new page and updated for visionOS.)

Privacy is paramount: it’s critical to be transparent about the privacy-related data and resources you require and essential to protect the data people allow you to access.

---

People use their devices in very personal ways and they expect apps to help them preserve their privacy.

When you submit a new or updated app, you must provide details about your privacy practices and the privacy-relevant data you collect so the App Store can display the information on your product page. (You can manage this information at any time in [App Store Connect](https://help.apple.com/app-store-connect/#/dev1b4647c5b).) People use the privacy details on your product page to make an informed decision before they download your app. To learn more, see [App privacy details on the App Store](https://developer.apple.com/app-store/app-privacy-details/).

## Best practices

**Request access only to data that you actually need.** Asking for more data than a feature needs — or asking for data before a person shows interest in the feature — can make it hard for people to trust your app. Give people precise control over their data by making your permission requests as specific as possible.

**Be transparent about how your app collects and uses people’s data.** People are less likely to be comfortable sharing data with your app if they don’t understand exactly how you plan to use it. Always respect people’s choices to use system features like Hide My Email and Mail Privacy Protection, and be sure you understand your obligations with regard to app tracking. To learn more about Apple privacy features, see [Privacy](https://www.apple.com/privacy/); for developer guidance, see [User privacy and data use](https://developer.apple.com/app-store/user-privacy-and-data-use/).

**Process data on the device where possible.** In iOS, for example, you can take advantage of the Apple Neural Engine and custom CreateML models to process the data right on the device, helping you avoid lengthy and potentially risky round trips to a remote server.

**Adopt system-defined privacy protections and follow security best practices.** For example, in iOS 15 and later, you can rely on CloudKit to provide encryption and key management for additional data types, like strings, numbers, and dates.

## Requesting permission

Here are several examples of the things you must request permission to access:

- Personal data, including location, health, financial, contact, and other personally identifying information
- User-generated content like emails, messages, calendar data, contacts, gameplay information, Apple Music activity, HomeKit data, and audio, video, and photo content
- Protected resources like Bluetooth peripherals, home automation features, Wi-Fi connections, and local networks
- Device capabilities like camera and microphone
- In a visionOS app running in a Full Space, ARKit data, such as hand tracking, plane estimation, image anchoring, and world tracking
- The device’s advertising identifier, which supports app tracking

The system provides a standard alert that lets people view each request you make. You supply copy that describes why your app needs access, and the system displays your description in the alert. People can also view the description — and update their choice — in Settings > Privacy.

**Request permission only when your app clearly needs access to the data or resource.** It’s natural for people to be suspicious of a request for personal information or access to a device capability, especially if there’s no obvious need for it. Ideally, wait to request permission until people actually use an app feature that requires access. For example, you can use the [location button](#location-button) to give people a way to share their location after they indicate interest in a feature that needs that information.

**Avoid requesting permission at launch unless the data or resource is required for your app to function.** People are less likely to be bothered by a launch-time request when it’s obvious why you’re making it. For example, people understand that a navigation app needs access to their location before they can benefit from it. Similarly, before people can play a visionOS game that lets them bounce virtual objects off walls in their surroundings, they need to permit the game to access information about their surroundings.

**Write copy that clearly describes how your app uses the ability, data, or resource you’re requesting.** The standard alert displays your copy (called a *purpose string* or *usage description string*) after your app name and before the buttons people use to grant or deny their permission. Aim for a brief, complete sentence that’s straightforward, specific, and easy to understand. Use sentence case, avoid passive voice, and include a period at the end. For developer guidance, see [Requesting access to protected resources](https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources) and [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency).

|  | Example purpose string | Notes |
| --- | --- | --- |
| ✓ | The app records during the night to detect snoring sounds. | An active sentence that clearly describes how and why the app collects the data. |
| ✗ | Microphone access is needed for a better experience. | A passive sentence that provides a vague, undefined justification. |
| ✗ | Turn on microphone access. | An imperative sentence that doesn’t provide any justification. |

Here are several examples of the standard system alert:

*Illustrated: Example 1, Example 2, Example 3.*

### Pre-alert screens, windows, or views

Ideally, the current context helps people understand why you’re requesting their permission. If it’s essential to provide additional details, you can display a custom screen or window before the system alert appears. The following guidelines apply to custom views that display before system alerts that request permission to access protected data and resources, including camera, microphone, location, contact, calendar, and tracking.

**Include only one button and make it clear that it opens the system alert.** People can feel manipulated when a custom screen or window also includes a button that doesn’t open the alert because the experience diverts them from making their choice. Another type of manipulation is using a term like “Allow” to title the custom screen’s button. If the custom button seems similar in meaning and visual weight to the allow button in the alert, people can be more likely to choose the alert’s allow button without meaning to. Use a term like “Continue” or “Next” to title the single button in your custom screen or window, clarifying that its action is to open the system alert.

**Don’t include additional actions in your custom screen or window, unless needed to obtain a legal consent.** For example, don’t provide a way for people to leave the screen or window without viewing the system alert — like offering an option to close or cancel.

### Tracking requests

App tracking is a sensitive issue. In some cases, it might make sense to display a custom screen or window that describes the benefits of tracking. If you want to perform app tracking as soon as people launch your app, you must display the system-provided alert before you collect any tracking data.

**Never precede the system-provided alert with a custom screen or window that could confuse or mislead people.** People sometimes tap quickly to dismiss alerts without reading them. A custom messaging screen, window, or view that takes advantage of such behaviors to influence choices will lead to rejection by App Store review.

There are several prohibited custom-screen designs that will cause rejection. Some examples are offering incentives, displaying a screen or window that looks like a request, displaying an image of the alert, and annotating the screen behind the alert (as shown below). For the avoidance of confusion, a consent screen or window shown before or after an [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency) system alert to comply with local privacy laws is allowed. To learn more, see [App Review Guidelines: 5.1.1 (iv)](https://developer.apple.com/app-store/review/guidelines/#data-collection-and-storage).

*Illustrated: Incentive, Imitation request, Alert image, Alert annotation.*

## Location button

In iOS, iPadOS, and watchOS, Core Location provides a button so people can grant your app temporary authorization to access their location at the moment a task needs it. A location button’s appearance can vary to match your app’s UI and it always communicates the action of location sharing in a way that’s instantly recognizable.

The first time people open your app and tap a location button, the system displays a standard alert. The alert helps people understand how using the button limits your app’s access to their location, and reminds them of the location indicator that appears when sharing starts.

After people confirm their understanding of the button’s action, simply tapping the location button gives your app one-time permission to access their location. Although each one-time authorization expires when people stop using your app, they don’t need to reconfirm their understanding of the button’s behavior.

> **Note:** If your app has no authorization status, tapping the location button has the same effect as when a person chooses *Allow Once* in the standard alert. If people previously chose *While Using the App*, tapping the location button doesn’t change your app’s status. For developer guidance, see [LocationButton](https://developer.apple.com/documentation/corelocationui/locationbutton) (SwiftUI) and [CLLocationButton](https://developer.apple.com/documentation/corelocationui/cllocationbutton) (Swift).

**Consider using the location button to give people a lightweight way to share their location for specific app features.** For example, your app might help people attach their location to a message or post, find a store, or identify a building, plant, or animal they’ve encountered in their location. If you know that people often grant your app *Allow Once* permission, consider using the location button to help them benefit from sharing their location without having to repeatedly interact with the alert.

**Consider customizing the location button to harmonize with your UI.** Specifically, you can:

- Choose the system-provided title that works best with your feature, such as “Current Location” or “Share My Current Location.”
- Choose the filled or outlined location glyph.
- Select a background color and a color for the title and glyph.
- Adjust the button’s corner radius.

To help people recognize and trust location buttons, you can’t customize the button’s other visual attributes. The system also ensures a location button remains legible by warning you about problems like low-contrast color combinations or too much translucency. In addition to fixing such problems, you’re responsible for making sure the text fits in the button — for example, button text needs to fit without truncation at all accessibility text sizes and when translated into other languages.

> **Important:** If the system identifies consistent problems with your customized location button, it won’t give your app access to the device location when people tap it. Although such a button can perform other app-specific actions, people may lose trust in your app if your location button doesn’t work as they expect.

## Protecting data

Protecting people’s information is paramount. Give people confidence in your app’s security and help preserve their privacy by taking advantage of system-provided security technologies when you need to store information locally, authorize people for specific operations, and transport information across a network.

Here are some high-level guidelines.

**Avoid relying solely on passwords for authentication.** Where possible, use [passkeys](https://developer.apple.com/documentation/authenticationservices/public-private_key_authentication/supporting_passkeys/) to replace passwords. If you need to continue using passwords for authentication, augment security by requiring two-factor authentication (for developer guidance, see [Securing Logins with iCloud Keychain Verification Codes](https://developer.apple.com/documentation/authenticationservices/securing-logins-with-icloud-keychain-verification-codes)). To further protect access to apps that people keep logged in on their device, use biometric identification like Face ID, Optic ID, or Touch ID. For developer guidance, see [Local Authentication](https://developer.apple.com/documentation/localauthentication).

**Store sensitive information in a keychain.** A keychain provides a secure, predictable user experience when handling someone’s private information. For developer guidance, see [Keychain services](https://developer.apple.com/documentation/security/keychain-services).

**Never store passwords or other secure content in plain-text files.** Even if you restrict access using file permissions, sensitive information is much safer in an encrypted keychain.

**Avoid inventing custom authentication schemes.** If your app requires authentication, prefer system-provided features like [passkeys](https://developer.apple.com/documentation/authenticationservices/public-private_key_authentication/supporting_passkeys/), [Sign in with Apple](sign-in-with-apple.md) or [Password AutoFill](https://developer.apple.com/documentation/security/password-autofill). For related guidance, see [Managing accounts](managing-accounts.md).

## Platform considerations

*No additional considerations for iOS, iPadOS, tvOS, or watchOS.*

### Desktop (macOS)

**Sign your app with a valid Developer ID.** If you choose to distribute your app outside the store, signing your app with Developer ID identifies you as an Apple developer and confirms that your app is safe to use. For developer guidance, see [Xcode Help](https://developer.apple.com/go/?id=ios-app-distribution-guide).

**Protect people’s data with app sandboxing.** Sandboxing provides your app with access to system resources and user data while protecting it from malware. All apps submitted to the Mac App Store require sandboxing. For developer guidance, see [Configuring the macOS App Sandbox](https://developer.apple.com/documentation/xcode/configuring-the-macos-app-sandbox).

**Avoid making assumptions about who is signed in.** Because of fast user switching, multiple people may be active on the same system.

## Change log

| Date | Changes |
| --- | --- |
| June 21, 2023 | Consolidated guidance into new page and updated for visionOS. |

## Related guidelines

- [Entering data](entering-data.md)
- [Onboarding](onboarding.md)

---


<a id="right-to-left"></a>
## right-to-left

# Right to left

> Source: <https://developer.apple.com/design/human-interface-guidelines/right-to-left>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)

Support right-to-left languages like Arabic and Hebrew by reversing your interface as needed to match the reading direction of the related scripts.

---

When people choose a language for their device — or just your app or game — they expect the interface to adapt in various ways (to learn more, see [Localization](https://developer.apple.com/localization/)).

System-provided UI frameworks support right-to-left (RTL) by default, allowing system-provided UI components to flip automatically in the RTL context. If you use system-provided elements and standard layouts, you might not need to make any changes to your app’s automatically reversed interface.

If you want to fine-tune your layout or enhance specific localizations to adapt to different currencies, numerals, or mathematical symbols that can occur in various locales in countries that use RTL languages, follow these guidelines.

## Text alignment

**Adjust text alignment to match the interface direction, if the system doesn’t do so automatically.** For example, if you left-align text with content in the left-to-right (LTR) context, right-align the text to match the content’s mirrored position in the RTL context.

**Align a paragraph based on its language, not on the current context.** When the alignment of a paragraph — defined as three or more lines of text — doesn’t match its language, it can be difficult to read. For example, right-aligning a paragraph that consists of LTR text can make the beginning of each line difficult to see. To improve readability, continue aligning one- and two-line text blocks to match the reading direction of the current context, but align a paragraph to match its language.

**Use a consistent alignment for all text items in a list.** To ensure a comfortable reading and scanning experience, reverse the alignment of all items in a list, including items that are displayed in a different script.

## Numbers and characters

Different RTL languages can use different number systems. For example, Hebrew text uses Western Arabic numerals, whereas Arabic text might use either Western or Eastern Arabic numerals. The use of Western and Eastern Arabic numerals varies among countries and regions and even among areas within the same country or region.

If your app covers mathematical concepts or other number-centric topics, it’s a good idea to identify the appropriate way to display such information in each locale you support. In contrast, apps that don’t address number-related topics can generally rely on system-provided number representations.

**Don’t reverse the order of numerals in a specific number.** Regardless of the current language or the surrounding content, the digits in a specific number — such as “541,” a phone number, or a credit card number — always appear in the same order.

**Reverse the order of numerals that show progress or a counting direction; never flip the numerals themselves.** Controls like progress bars, sliders, and rating controls often include numerals to clarify their meaning. If you use numerals in this way, be sure to reverse the order of the numerals to match the direction of the flipped control. Also reverse a sequence of numerals if you use the sequence to communicate a specific order.

## Controls

**Flip controls that show progress from one value to another.** Because people tend to view forward progress as moving in the same direction as the language they read, it makes sense to flip controls like sliders and progress indicators in the RTL context. When you do this, also be sure to reverse the positions of the accompanying glyphs or images that depict the beginning and ending values of the control.

**Flip controls that help people navigate or access items in a fixed order.** For example, in the RTL context, a back button must point to the right so the flow of screens matches the reading order of the RTL language. Similarly, next or previous buttons that let people access items in an ordered list need to flip in the RTL context to match the reading order.

**Preserve the direction of a control that refers to an actual direction or points to an onscreen area.** For example, if you provide a control that means “to the right,” it must always point right, regardless of the current context.

**Visually balance adjacent Latin and RTL scripts when necessary.** In buttons, labels, and titles, Arabic or Hebrew text can appear too small when next to uppercased Latin text, because Arabic and Hebrew don’t include uppercase letters. To visually balance Arabic or Hebrew text with Latin text that uses all capitals, it often works well to increase the RTL font size by about 2 points.

## Images

**Avoid flipping images like photographs, illustrations, and general artwork.** Flipping an image often changes the image’s meaning; flipping a copyrighted image could be a violation. If an image’s content is strongly connected to reading direction, consider creating a new version of the image instead of flipping the original.

**Reverse the positions of images when their order is meaningful.** For example, if you display multiple images in a specific order like chronological, alphabetical, or favorite, reverse their positions to preserve the order’s meaning in the RTL context.

## Interface icons

When you use [SF Symbols](sf-symbols.md) to supply interface icons for your app, you get variants for the RTL context and localized symbols for Arabic and Hebrew, among other languages. If you create custom symbols, you can specify their directionality. For developer guidance, see [Creating custom symbols](https://developer.apple.com/documentation/technologyoverviews/custom-sf-symbols).

**Flip interface icons that represent text or reading direction.** For example, if an interface icon uses left-aligned bars to represent text in the LTR context, right-align the bars in the RTL context.

**Consider creating a localized version of an interface icon that displays text.** Some interface icons include letters or words to help communicate a script-related concept, like font-size choice or a signature. If you have a custom interface icon that needs to display actual text, consider creating a localized version. For example, SF Symbols offers different versions of the signature, rich-text, and I-beam pointer symbols for use with Latin, Hebrew, and Arabic text, among others.

If you have a custom interface icon that uses letters or words to communicate a concept unrelated to reading or writing, consider designing an alternative image that doesn’t use text.

**Flip an interface icon that shows forward or backward motion.** When something moves in the same direction that people read, they typically interpret that direction as forward; when something moves in the opposite direction, people tend to interpret the direction as backward. An interface icon that depicts an object moving forward or backward needs to flip in the RTL context to preserve the meaning of the motion. For example, an icon that represents a speaker typically shows sound waves emanating forward from the speaker. In the LTR context, the sound waves come from the left, so in the RTL context, the icon needs to flip to show the waves coming from the right.

**Don’t flip logos or universal signs and marks.** Displaying a flipped logo confuses people and can have legal repercussions. Always display a logo in its original form, even if it includes text. People expect universal symbols and marks like the checkmark to have a consistent appearance, so avoid flipping them.

**In general, avoid flipping interface icons that depict real-world objects.** Unless you use the object to indicate directionality, it’s best to avoid flipping an icon that represents a familiar item. For example, clocks work the same everywhere, so a traditional clock interface icon needs to look the same regardless of language direction. Some interface icons might seem to reference language or reading direction because they represent items that are slanted for right-handed use. However, most people are right-handed, so flipping an icon that shows a right-handed tool isn’t necessary and might be confusing.

**Before merely flipping a complex custom interface icon, consider its individual components and the overall visual balance.** In some cases, a component — like a badge, slash, or magnifying glass — needs to adhere to a visual design language regardless of localization. For example, SF Symbols maintains visual consistency by using the same backslash to represent the prohibition or negation of a symbol’s meaning in both LTR and RTL versions.

In other cases, you might need to flip a component (or its position) to ensure the localized version of the icon still makes sense. For example, if a badge represents the actual UI that people see in your app, it needs to flip if your UI flips. Alternatively, if a badge modifies the meaning of an interface icon, consider whether flipping the badge preserves both the modified meaning and the overall visual balance of the icon. In the images shown below, the badge doesn’t depict an object in the UI, but keeping it in the top-right corner visually unbalances the cart.

If your custom interface icon includes a component that can imply handedness, like a tool, consider preserving the orientation of the tool while flipping the base image if necessary.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Related guidelines

- [Layout](layout.md)
- [Inclusion](inclusion.md)
- [SF Symbols](sf-symbols.md)

---


<a id="sf-symbols"></a>
## sf-symbols

# SF Symbols

> Source: <https://developer.apple.com/design/human-interface-guidelines/sf-symbols>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-07-28 (Updated with guidance for Draw animations and gradient rendering in SF Symbols 7.)

SF Symbols provides thousands of consistent, highly configurable symbols that integrate seamlessly with the San Francisco system font, automatically aligning with text in all weights and sizes.

---

You can use a symbol to convey an object or concept wherever interface icons can appear, such as in toolbars, tab bars, context menus, and within text.

Availability of individual symbols and features varies based on the version of the system you’re targeting. Symbols and symbol features introduced in a given year aren’t available in earlier operating systems.

Visit [SF Symbols](https://developer.apple.com/sf-symbols/) to download the app and browse the full set of symbols. Be sure to understand the terms and conditions for using SF Symbols, including the prohibition against using symbols — or images that are confusingly similar — in app icons, logos, or any other trademarked use. For developer guidance, see [Configuring and displaying symbol images in your UI](https://developer.apple.com/documentation/uikit/configuring-and-displaying-symbol-images-in-your-ui).

## Rendering modes

SF Symbols provides four rendering modes — monochrome, hierarchical, palette, and multicolor — that give you multiple options when applying color to symbols. For example, you might want to use multiple opacities of your app’s accent color to give symbols depth and emphasis, or specify a palette of contrasting colors to display symbols that coordinate with various color schemes.

To support the rendering modes, SF Symbols organizes a symbol’s paths into distinct layers. For example, the `cloud.sun.rain.fill` symbol consists of three layers: the primary layer contains the cloud paths, the secondary layer contains the paths that define the sun and its rays, and the tertiary layer contains the raindrop paths.

Depending on the rendering mode you choose, a symbol can produce various appearances. For example, Hierarchical rendering mode assigns a different opacity of a single color to each layer, creating a visual hierarchy that gives depth to the symbol.

To learn more about supporting rendering modes in custom symbols, see [Custom symbols](#custom-symbols).

SF Symbols supports the following rendering modes.

**Monochrome** — Applies one color to all layers in a symbol. Within a symbol, paths render in the color you specify or as a transparent shape within a color-filled path.

**Hierarchical** — Applies one color to all layers in a symbol, varying the color’s opacity according to each layer’s hierarchical level.

**Palette** — Applies two or more colors to a symbol, using one color per layer. Specifying only two colors for a symbol that defines three levels of hierarchy means the secondary and tertiary layers use the same color.

**Multicolor** — Applies intrinsic colors to some symbols to enhance meaning. For example, the `leaf` symbol uses green to reflect the appearance of leaves in the physical world, whereas the `trash.slash` symbol uses red to signal data loss. Some multicolor symbols include layers that can receive other colors.

Regardless of rendering mode, using system-provided colors ensures that symbols automatically adapt to accessibility accommodations and appearance modes like vibrancy and Dark Mode. For developer guidance, see [renderingMode(_:)](https://developer.apple.com/documentation/swiftui/image/renderingmode(_:)).

**Confirm that a symbol’s rendering mode works well in every context.** Depending on factors like the size of a symbol and its contrast with the current background color, different rendering modes can affect how well people can discern the symbol’s details. You can use the automatic setting to get a symbol’s preferred rendering mode, but it’s still a good idea to check the results for places where a different rendering mode might improve a symbol’s legibility.

## Gradients

In SF Symbols 7 and later, gradient rendering generates a smooth linear gradient from a single source color. You can use gradients across all rendering modes for both system and custom colors and for custom symbols. Gradients render for symbols of any size, but look best at larger sizes.

## Variable color

With variable color, you can represent a characteristic that can change over time — like capacity or strength — regardless of rendering mode. To visually communicate such a change, variable color applies color to different layers of a symbol as a value reaches different thresholds between zero and 100 percent.

For example, you could use variable color with the `speaker.wave.3` symbol to communicate three different ranges of sound — plus the state where there’s no sound — by mapping the layers that represent the curved wave paths to different ranges of decibel values. In the case of no sound, no wave layers get color. In all other cases, a wave layer receives color when the sound reaches a threshold the system defines based on the  number of nonzero states you want to represent.

Sometimes, it can make sense for some of a symbol’s layers to opt out of variable color. For example, in the `speaker.wave.3` symbol shown above, the layer that contains the speaker path doesn’t receive variable color because a speaker doesn’t change as the sound level changes. A symbol can support variable color in any number of layers.

**Use variable color to communicate change — don’t use it to communicate depth.** To convey depth and visual hierarchy, use Hierarchical rendering mode to elevate certain layers and distinguish foreground and background elements in a symbol.

## Weights and scales

SF Symbols provides symbols in a wide range of weights and scales to help you create adaptable designs.

Each of the nine symbol weights — from ultralight to black — corresponds to a weight of the San Francisco system font, helping you achieve precise weight matching between symbols and adjacent text, while supporting flexibility for different sizes and contexts.

Each symbol is also available in three scales: small, medium (the default), and large. The scales are defined relative to the cap height of the San Francisco system font.

Specifying a scale lets you adjust a symbol’s emphasis compared to adjacent text, without disrupting the weight matching with text that uses the same point size. For developer guidance, see [imageScale(_:)](https://developer.apple.com/documentation/swiftui/view/imagescale(_:)) (SwiftUI), [UIImage.SymbolScale](https://developer.apple.com/documentation/uikit/uiimage/symbolscale) (UIKit), and [NSImage.SymbolConfiguration](https://developer.apple.com/documentation/appkit/nsimage/symbolconfiguration-swift.class) (AppKit).

## Design variants

SF Symbols defines several design variants — such as fill, slash, and enclosed — that can help you communicate precise states and actions while maintaining visual consistency and simplicity in your UI. For example, you could use the slash variant of a symbol to show that an item or action is unavailable, or use the fill variant to indicate selection.

Outline is the most common variant in SF Symbols. An outlined symbol has no solid areas, resembling the appearance of text. Most symbols are also available in a fill variant, in which the areas within some shapes are solid.

In addition to outline and fill, SF Symbols also defines variants that include a slash or enclose a symbol within a shape like a circle, square, or rectangle. In many cases, enclosed and slash variants can combine with outline or fill variants.

SF Symbols provides many variants for specific languages and writing systems, including Latin, Arabic, Hebrew, Hindi, Thai, Chinese, Japanese, Korean, Cyrillic, Devanagari, and several Indic numeral systems. Language- and script-specific variants adapt automatically when the device language changes. For guidance, see [Images](right-to-left.md#images).

Symbol variants support a range of design goals. For example:

- The outline variant works well in toolbars, lists, and other places where you display a symbol alongside text.
- Symbols that use an enclosing shape — like a square or circle — can improve legibility at small sizes.
- The solid areas in a fill variant tend to give a symbol more visual emphasis, making it a good choice for iOS tab bars and swipe actions and places where you use an accent color to communicate selection.

In many cases, the view that displays a symbol determines whether to use outline or fill, so you don’t have to specify a variant. For example, an iOS tab bar prefers the fill variant, whereas a toolbar takes the outline variant.

## Animations

SF Symbols provides a collection of expressive, configurable animations that enhance your interface and add vitality to your app. Symbol animations help communicate ideas, provide feedback in response to people’s actions, and signal changes in status or ongoing activities.

Animations work on all SF Symbols in the library, in all rendering modes, weights, and scales, and on custom symbols. For considerations when animating custom symbols, see [Custom symbols](#custom-symbols). You can control the playback of an animation, whether you want the animation to run from start to finish, or run indefinitely, repeating its effect until a condition is met. You can customize behaviors, like changing the playback speed of an animation or determining whether to reverse an animation before repeating it. For developer guidance, see [Symbols](https://developer.apple.com/documentation/symbols) and [SymbolEffect](https://developer.apple.com/documentation/symbols/symboleffect).

**Appear** — Causes a symbol to gradually emerge into view.

**Disappear** — Causes a symbol to gradually recede out of view.

**Bounce** — Briefly scales a symbol with an elastic-like movement that goes either up or down and then returns to the symbol’s initial state. The bounce animation plays once by default and can help communicate that an action occurred or needs to take place.

**Scale** — Changes the size of a symbol, increasing or decreasing its scale. Unlike the bounce animation, which returns the symbol to its original state, the scale animation persists until you set a new scale or remove the effect. You might use the scale animation to draw people’s attention to a selected item or as feedback when people choose a symbol.

**Pulse** — Varies the opacity of a symbol over time. This animation automatically pulses only the layers within a symbol that are annotated to pulse, and optionally can pulse all layers within a symbol. You might use the pulse animation to communicate ongoing activity, playing it continuously until a condition is met.

**Variable color** — Incrementally varies the opacity of layers within a symbol. This animation can be cumulative or iterative. When cumulative, color changes persist for each layer until the animation cycle is complete. When iterative, color changes occur one layer at a time. You might use variable color to communicate progress or ongoing activity, such as playback, connecting, or broadcasting. You can customize the animation to autoreverse — meaning reverse the animation to the starting point and replay the sequence — as well as hide inactive layers rather than reduce their opacity.

The arrangement of layers within a symbol determines how variable color behaves during a repeating animation. Symbols with layers that are arranged linearly where the start and end points don’t meet are annotated as *open loop*. Symbols with layers that follow a complete shape where the start and end points do meet, like in a circular progress indicator, are annotated as *closed loop*. Variable color animations for symbols with closed loop designs feature seamless, continuous playback.

**Replace** — Replaces one symbol with another. The replace animation works between arbitrary symbols and across all weights and rendering modes. This animation features three configurations:

- Down-up, where the outgoing symbol scales down and the incoming symbol scales up, communicating a change in state.
- Up-up, where both the outgoing and incoming symbols scale up. This configuration communicates a change in state that includes a sense of forward progression.
- Off-up, where the outgoing symbol hides immediately and the incoming symbol scales up. This configuration communicates a state change that emphasizes the next available state or action.

**Magic Replace** — Performs a smart transition between two symbols with related shapes. For example, slashes can draw on and off, and badges can appear or disappear, or you can replace them independently of the base symbol. Magic Replace is the new default replace animation, but doesn’t occur between unrelated symbols; the default down-up animation occurs instead. You can choose a custom direction for the fallback animation in these situations if you prefer one other than the default.

**Wiggle** — Moves the symbol back and forth along a directional axis. You might use the wiggle animation to highlight a change or a call to action that a person might overlook. Wiggle can also add a dynamic emphasis to an interaction or reinforce what the symbol is representing, such as when an arrow points in a specific direction.

**Breathe** — Smoothly increases and decreases the presence of a symbol, giving it a living quality. You might use the breathe animation to convey status changes, or signal that an activity is taking place, like an ongoing recording session. Breathe is similar to pulse; however pulse animates by changing opacity alone, while breathe changes both opacity and size to convey ongoing activity.

**Rotate** — Rotates the symbol to act as a visual indicator or imitate an object’s behavior in the real world. For example, when a task is in progress, rotation confirms that it’s working as expected. The rotate animation causes some symbols to rotate entirely, while in others only certain parts of the symbol rotate. Symbols like the desk fan, for example, use the By Layer rotation option to spin only the fan blades.

**Draw On / Draw Off** — In SF Symbols 7 and later, draws the symbol along a path through a set of guide points, either from offscreen to onscreen (Draw On) or from onscreen to offscreen (Draw Off). You can draw all layers at once, stagger them, or draw each layer one at a time. You might use the draw animation to convey progress, as with a download, or to reinforce the meaning of a symbol, like a directional arrow.

**Apply symbol animations judiciously.** While there’s no limit to how many animations you can add to a view, too many animations can overwhelm an interface and distract people.

**Make sure that animations serve a clear purpose in communicating a symbol’s intent.** Each type of animation has a discrete movement that communicates a certain type of action or elicits a certain response. Consider how people might interpret an animated symbol and whether the animation, or combination of animations, might be confusing.

**Use symbol animations to communicate information more efficiently.** Animations provide visual feedback, reinforcing that something happened in your interface. You can use animations to present complex information in a simple way and without taking up a lot of visual space.

**Consider your app’s tone when adding animations.** When animating a symbol, think about what the animation can convey and how that might align with your brand identity and your app’s overall style and tone. For guidance, see [Branding](branding.md).

## Custom symbols

If you need a symbol that SF Symbols doesn’t provide, you can create your own. To create a custom symbol, first export the template for a symbol that’s similar to the design you want, then use a vector-editing tool to modify it. For developer guidance, see [Creating custom symbols](https://developer.apple.com/documentation/technologyoverviews/custom-sf-symbols).

> **Important:** SF Symbols includes copyrighted symbols that depict Apple products and features. You can display these symbols in your app, but you can’t customize them. To help you identify a noncustomizable symbol, the SF Symbols app badges it with an Info icon; to help you use the symbol correctly, the inspector pane describes its usage restrictions.

Using a process called *annotating*, you can assign a specific color — or a specific hierarchical level, such as primary, secondary, or tertiary — to each layer in a custom symbol. Depending on the rendering modes you support, you can use a different mode in each instance of the symbol in your app.

**Use the template as a guide.** Create a custom symbol that’s consistent with the ones the system provides in level of detail, optical weight, alignment, position, and perspective. Strive to design a symbol that is:

- Simple
- Recognizable
- Inclusive
- Directly related to the action or content it represents

For guidance, see [Icons](icons.md).

**Assign negative side margins to your custom symbol if necessary.** SF Symbols supports negative side margins to aid optical horizontal alignment when a symbol contains a badge or other elements that increase its width. For example, negative side margins can help you horizontally align a stack of folder symbols, some of which include a badge. The name of each margin includes the relevant configuration  — such as “left-margin-Regular-M” — so be sure to use this naming pattern if you add margins to your custom symbols.

**Optimize layers to use animations with custom symbols.** If you want to animate your symbol by layer, make sure to annotate the layers in the SF Symbols app. The Z-order determines the order that you want to apply colors to the layers of a variable color symbol, and you can choose whether to animate those changes from front-to-back, or back-to-front. You can also animate by layer groups to have related layers move together.

**Test animations for custom symbols.** It’s important to test your custom symbols with all of the animation presets because the shapes and paths might not appear how you expect when the layers are in motion. To get the most out of this feature, consider drawing your custom symbols with whole shapes. For example, a custom symbol similar to the `person.2.fill` symbol doesn’t need to create a cutout for the shape representing the person on the left. Instead, you can draw the full shape of the person, and in addition to that, draw an offset path of the person on the right to help represent the gap between them. You can later annotate this offset path as an erase layer to render the symbol as you want. This method of drawing helps preserve additional layer information that allows for animations to perform as you expect.

**Avoid making custom symbols that include common variants, such as enclosures or badges.** The SF Symbols app offers a component library for creating variants of your custom symbol. Using the component library allows you to create commonly used variants of your custom symbol while maintaining design consistency with the included SF Symbols.

**Provide alternative text labels for custom symbols.** Alternative text labels — or accessibility descriptions — let VoiceOver describe visible UI and content, making navigation easier for people with visual disabilities. For guidance, see [VoiceOver](voiceover.md).

**Don’t design replicas of Apple products.** Apple products are copyrighted and you can’t reproduce them in your custom symbols. Also, you can’t customize a symbol that SF Symbols identifies as representing an Apple feature or product.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| July 28, 2025 | Updated with guidance for Draw animations and gradient rendering in SF Symbols 7. |
| June 10, 2024 | Updated with guidance for new animations and features of SF Symbols 6. |
| June 5, 2023 | Added a new section on animations. Included animation guidance for custom symbols. |
| September 14, 2022 | Added a new section on variable color. Removed instructions on creating custom symbol paths, exporting templates, and layering paths, deferring to developer articles that cover these topics. |

## Related guidelines

- [Typography](typography.md)
- [Icons](icons.md)

---


<a id="typography"></a>
## typography

# Typography

> Source: <https://developer.apple.com/design/human-interface-guidelines/typography>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-12-16 (Added emphasized weights to the Dynamic Type style specifications for each platform.)

Your typographic choices can help you display legible text, convey an information hierarchy, communicate important content, and express your brand or style.

---

## Ensuring legibility

**Use font sizes that most people can read easily.** People need to be able to read your content at various viewing distances and under a variety of conditions. Follow the recommended default and minimum text sizes for each platform — for both custom and system fonts — to ensure your text is legible on all devices. Keep in mind that font weight can also impact how easy text is to read. If you use a custom font with a thin weight, aim for larger than the recommended sizes to increase legibility.

| Platform | Default size | Minimum size |
| --- | --- | --- |
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |

**Test legibility in different contexts.** For example, you need to test game text for legibility on each platform on which your game runs. If testing shows that some of your text is difficult to read, consider using a larger type size, increasing contrast by modifying the text or background colors, or using typefaces designed for optimized legibility, like the system fonts.

**In general, avoid light font weights.** For example, if you’re using system-provided fonts, prefer Regular, Medium, Semibold, or Bold font weights, and avoid Ultralight, Thin, and Light font weights, which can be difficult to see, especially when text is small.

## Conveying hierarchy

**Adjust font weight, size, and color as needed to emphasize important information and help people visualize hierarchy.** Be sure to maintain the relative hierarchy and visual distinction of text elements when people adjust text sizes.

**Minimize the number of typefaces you use, even in a highly customized interface.** Mixing too many different typefaces can obscure your information hierarchy and hinder readability, in addition to making an interface feel internally inconsistent or poorly designed.

**Prioritize important content when responding to text-size changes.** Not all content is equally important. When someone chooses a larger text size, they typically want to make the content they care about easier to read; they don’t always want to increase the size of every word on the screen. For example, when people increase text size to read the content in a tabbed window, they don’t expect the tab titles to increase in size. Similarly, in a game, people are often more interested in a character’s dialog than in transient hit-damage values.

## Using system fonts

Apple provides two typeface families that support an extensive range of weights, sizes, styles, and languages.

**San Francisco (SF)** is a sans serif typeface family that includes the SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian, SF Hebrew, and SF Mono variants.

The system also offers SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian, and SF Hebrew in rounded variants you can use to coordinate text with the appearance of soft or rounded UI elements, or to provide an alternative typographic voice.

**New York (NY)** is a serif typeface family designed to work well by itself and alongside the SF fonts.

You can download the San Francisco and New York fonts [here](https://developer.apple.com/fonts/).

The system provides the SF and NY fonts in the *variable* font format, which combines different font styles together in one file, and supports interpolation between styles to create intermediate ones.

> **Note:** Variable fonts support *optical sizing*, which refers to the adjustment of different typographic designs to fit different sizes. On all platforms, the system fonts support *dynamic optical sizes*, which merge discrete optical sizes (like Text and Display) and weights into a single, continuous design, letting the system interpolate each glyph or letterform to produce a structure that’s precisely adapted to the point size. With dynamic optical sizes, you don’t need to use discrete optical sizes unless you’re working with a design tool that doesn’t support all the features of the variable font format.

To help you define visual hierarchies and create clear and legible designs in many different sizes and contexts, the system fonts are available in a variety of weights, ranging from Ultralight to Black, and — in the case of SF — several widths, including Condensed and Expanded. Because SF Symbols use equivalent weights, you can achieve precise weight matching between symbols and adjacent text, regardless of the size or style you choose.

> **Note:** [SF Symbols](sf-symbols.md) provides a comprehensive library of symbols that integrate seamlessly with the San Francisco system font, automatically aligning with text in all weights and sizes. Consider using symbols when you need to convey a concept or depict an object, especially within text.

The system defines a set of typographic attributes — called text styles — that work with both typeface families. A *text style* specifies a combination of font weight, point size, and leading values for each text size. For example, the *body* text style uses values that support a comfortable reading experience over multiple lines of text, while the *headline* style assigns a font size and weight that help distinguish a heading from surrounding content. Taken together, the text styles form a typographic hierarchy you can use to express the different levels of importance in your content. Text styles also allow text to scale proportionately when people change the system’s text size or make accessibility adjustments, like turning on Larger Text in Accessibility settings.

**Consider using the built-in text styles.** The system-defined text styles give you a convenient and consistent way to convey your information hierarchy through font size and weight. Using text styles with the system fonts also ensures support for Dynamic Type and larger accessibility type sizes (where available), which let people choose the text size that works for them. For guidance, see [Supporting Dynamic Type](#supporting-dynamic-type).

**Modify the built-in text styles if necessary.** System APIs define font adjustments — called *symbolic traits* — that let you modify some aspects of a text style. For example, the bold trait adds weight to text, letting you create another level of hierarchy. You can also use symbolic traits to adjust leading if you need to improve readability or conserve space. For example, when you display text in wide columns or long passages, more space between lines (*loose leading*) can make it easier for people to keep their place while moving from one line to the next. Conversely, if you need to display multiple lines of text in an area where height is constrained — for example, in a list row — decreasing the space between lines (*tight leading*) can help the text fit well. If you need to display three or more lines of text, avoid tight leading even in areas where height is limited. For developer guidance, see [leading(_:)](https://developer.apple.com/documentation/swiftui/font/leading(_:)).

> **Developer note:** You can use the constants defined in [Font.Design](https://developer.apple.com/documentation/swiftui/font/design) to access all system fonts — don’t embed system fonts in your app or game. For example, use [Font.Design.default](https://developer.apple.com/documentation/swiftui/font/design/default) to get the system font on all platforms; use [Font.Design.serif](https://developer.apple.com/documentation/swiftui/font/design/serif) to get the New York font.

**If necessary, adjust tracking in interface mockups.** In a running app, the system font dynamically adjusts tracking at every point size. To produce an accurate interface mockup of an interface that uses the variable system fonts, you don’t have to choose a discrete optical size at certain point sizes, but you might need to adjust the tracking. For guidance, see [Tracking values](#tracking-values).

## Using custom fonts

**Make sure custom fonts are legible.** People need to be able to read your custom font easily at various viewing distances and under a variety of conditions. While using a custom font, be guided by the recommended minimum font sizes for various styles and weights in [Specifications](#specifications).

**Implement accessibility features for custom fonts.** System fonts automatically support Dynamic Type (where available) and respond when people turn on accessibility features, such as Bold Text. If you use a custom font, make sure it implements the same behaviors. For developer guidance, see [Applying custom fonts to text](https://developer.apple.com/documentation/swiftui/applying-custom-fonts-to-text). In a Unity-based game, you can use [Apple’s Unity plug-ins](https://github.com/apple/unityplugins) to support Dynamic Type. If the plug-in isn’t appropriate for your game, be sure to let players adjust text size in other ways.

## Supporting Dynamic Type

Dynamic Type is a system-level feature in iOS, iPadOS, tvOS, visionOS, and watchOS that lets people adjust the size of visible text on their device to ensure readability and comfort. For related guidance, see [Accessibility](accessibility.md).

For a list of available Dynamic Type sizes, see [Specifications](#specifications). You can also download Dynamic Type size tables in the [Apple Design Resources](https://developer.apple.com/design/resources/) for each platform.

For developer guidance, see [Text input and output](https://developer.apple.com/documentation/swiftui/text-input-and-output). To support Dynamic Type in Unity-based games, use [Apple’s Unity plug-ins](https://github.com/apple/unityplugins).

**Make sure your app’s layout adapts to all font sizes.** Verify that your design scales, and that text and glyphs are legible at all font sizes. On iPhone or iPad, turn on Larger Accessibility Text Sizes in Settings > Accessibility > Display & Text Size > Larger Text, and confirm that your app remains comfortably readable.

**Increase the size of meaningful interface icons as font size increases.** If you use interface icons to communicate important information, make sure they’re easy to view at larger font sizes too. When you use [SF Symbols](sf-symbols.md), you get icons that scale automatically with Dynamic Type size changes.

**Keep text truncation to a minimum as font size increases.** In general, aim to display as much useful text at the largest accessibility font size as you do at the largest standard font size. Avoid truncating text in scrollable regions unless people can open a separate view to read the rest of the content. You can prevent text truncation in a label by configuring it to use as many lines as needed to display a useful amount of text. For developer guidance, see [numberOfLines](https://developer.apple.com/documentation/uikit/uilabel/numberoflines).

**Consider adjusting your layout at large font sizes.** When font size increases in a horizontally constrained context, inline items (like glyphs and timestamps) and container boundaries can crowd text and cause truncation or overlapping. To improve readability, consider using a stacked layout where text appears above secondary items. Multicolumn text can also be less readable at large sizes due to horizontal space constraints. Reduce the number of columns when the font size increases to avoid truncation and enhance readability. For developer guidance, see [isAccessibilityCategory](https://developer.apple.com/documentation/uikit/uicontentsizecategory/isaccessibilitycategory).

**Maintain a consistent information hierarchy regardless of the current font size.** For example, keep primary elements toward the top of a view even when the font size is very large, so that people don’t lose track of these elements.

## Platform considerations

### Mobile (iOS, iPadOS)

SF Pro is the system font in iOS and iPadOS. iOS and iPadOS apps can also use NY.

### Desktop (macOS)

SF Pro is the system font in macOS. NY is available for Mac apps built with Mac Catalyst. macOS doesn’t support Dynamic Type.

**When necessary, use dynamic system font variants to match the text in standard controls.** Dynamic system font variants give your text the same look and feel of the text that appears in system-provided controls. Use the variants listed below to achieve a look that’s consistent with other apps on the platform.

| Dynamic font variant | API |
| --- | --- |
| Control content | [controlContentFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/controlcontentfont(ofsize:)) |
| Label | [labelFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/labelfont(ofsize:)) |
| Menu | [menuFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/menufont(ofsize:)) |
| Menu bar | [menuBarFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/menubarfont(ofsize:)) |
| Message | [messageFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/messagefont(ofsize:)) |
| Palette | [paletteFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/palettefont(ofsize:)) |
| Title | [titleBarFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/titlebarfont(ofsize:)) |
| Tool tips | [toolTipsFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/tooltipsfont(ofsize:)) |
| Document text (user) | [userFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/userfont(ofsize:)) |
| Monospaced document text (user fixed pitch) | [userFixedPitchFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/userfixedpitchfont(ofsize:)) |
| Bold system font | [boldSystemFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/boldsystemfont(ofsize:)) |
| System font | [systemFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/systemfont(ofsize:)) |

## Specifications

You can display emphasized variants of system text styles using symbolic traits. In SwiftUI, use the [bold()](https://developer.apple.com/documentation/swiftui/text/bold()) modifier; in UIKit, use [traitBold](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits-swift.struct/traitbold) in the [UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifontdescriptor) API. The emphasized weights can be medium, semibold, bold, or heavy. The following specifications include the emphasized weight for each text style.

### iOS, iPadOS Dynamic Type sizes

#### xSmall

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 31 | 38 | Bold |
| Title 1 | Regular | 25 | 31 | Bold |
| Title 2 | Regular | 19 | 24 | Bold |
| Title 3 | Regular | 17 | 22 | Semibold |
| Headline | Semibold | 14 | 19 | Semibold |
| Body | Regular | 14 | 19 | Semibold |
| Callout | Regular | 13 | 18 | Semibold |
| Subhead | Regular | 12 | 16 | Semibold |
| Footnote | Regular | 12 | 16 | Semibold |
| Caption 1 | Regular | 11 | 13 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |

*Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

#### Small

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 32 | 39 | Bold |
| Title 1 | Regular | 26 | 32 | Bold |
| Title 2 | Regular | 20 | 25 | Bold |
| Title 3 | Regular | 18 | 23 | Semibold |
| Headline | Semibold | 15 | 20 | Semibold |
| Body | Regular | 15 | 20 | Semibold |
| Callout | Regular | 14 | 19 | Semibold |
| Subhead | Regular | 13 | 18 | Semibold |
| Footnote | Regular | 12 | 16 | Semibold |
| Caption 1 | Regular | 11 | 13 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |

*Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

#### Medium

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 33 | 40 | Bold |
| Title 1 | Regular | 27 | 33 | Bold |
| Title 2 | Regular | 21 | 26 | Bold |
| Title 3 | Regular | 19 | 24 | Semibold |
| Headline | Semibold | 16 | 21 | Semibold |
| Body | Regular | 16 | 21 | Semibold |
| Callout | Regular | 15 | 20 | Semibold |
| Subhead | Regular | 14 | 19 | Semibold |
| Footnote | Regular | 12 | 16 | Semibold |
| Caption 1 | Regular | 11 | 13 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |

*Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

#### Large (default)

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 34 | 41 | Bold |
| Title 1 | Regular | 28 | 34 | Bold |
| Title 2 | Regular | 22 | 28 | Bold |
| Title 3 | Regular | 20 | 25 | Semibold |
| Headline | Semibold | 17 | 22 | Semibold |
| Body | Regular | 17 | 22 | Semibold |
| Callout | Regular | 16 | 21 | Semibold |
| Subhead | Regular | 15 | 20 | Semibold |
| Footnote | Regular | 13 | 18 | Semibold |
| Caption 1 | Regular | 12 | 16 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |

*Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

#### xLarge

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 36 | 43 | Bold |
| Title 1 | Regular | 30 | 37 | Bold |
| Title 2 | Regular | 24 | 30 | Bold |
| Title 3 | Regular | 22 | 28 | Semibold |
| Headline | Semibold | 19 | 24 | Semibold |
| Body | Regular | 19 | 24 | Semibold |
| Callout | Regular | 18 | 23 | Semibold |
| Subhead | Regular | 17 | 22 | Semibold |
| Footnote | Regular | 15 | 20 | Semibold |
| Caption 1 | Regular | 14 | 19 | Semibold |
| Caption 2 | Regular | 13 | 18 | Semibold |

*Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

#### xxLarge

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 38 | 46 | Bold |
| Title 1 | Regular | 32 | 39 | Bold |
| Title 2 | Regular | 26 | 32 | Bold |
| Title 3 | Regular | 24 | 30 | Semibold |
| Headline | Semibold | 21 | 26 | Semibold |
| Body | Regular | 21 | 26 | Semibold |
| Callout | Regular | 20 | 25 | Semibold |
| Subhead | Regular | 19 | 24 | Semibold |
| Footnote | Regular | 17 | 22 | Semibold |
| Caption 1 | Regular | 16 | 21 | Semibold |
| Caption 2 | Regular | 15 | 20 | Semibold |

*Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

#### xxxLarge

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 40 | 48 | Bold |
| Title 1 | Regular | 34 | 41 | Bold |
| Title 2 | Regular | 28 | 34 | Bold |
| Title 3 | Regular | 26 | 32 | Semibold |
| Headline | Semibold | 23 | 29 | Semibold |
| Body | Regular | 23 | 29 | Semibold |
| Callout | Regular | 22 | 28 | Semibold |
| Subhead | Regular | 21 | 28 | Semibold |
| Footnote | Regular | 19 | 24 | Semibold |
| Caption 1 | Regular | 18 | 23 | Semibold |
| Caption 2 | Regular | 17 | 22 | Semibold |

*Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

### iOS, iPadOS larger accessibility type sizes

#### AX1

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 44 | 52 | Bold |
| Title 1 | Regular | 38 | 46 | Bold |
| Title 2 | Regular | 34 | 41 | Bold |
| Title 3 | Regular | 31 | 38 | Semibold |
| Headline | Semibold | 28 | 34 | Semibold |
| Body | Regular | 28 | 34 | Semibold |
| Callout | Regular | 26 | 32 | Semibold |
| Subhead | Regular | 25 | 31 | Semibold |
| Footnote | Regular | 23 | 29 | Semibold |
| Caption 1 | Regular | 22 | 28 | Semibold |
| Caption 2 | Regular | 20 | 25 | Semibold |

*Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

#### AX2

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 48 | 57 | Bold |
| Title 1 | Regular | 43 | 51 | Bold |
| Title 2 | Regular | 39 | 47 | Bold |
| Title 3 | Regular | 37 | 44 | Semibold |
| Headline | Semibold | 33 | 40 | Semibold |
| Body | Regular | 33 | 40 | Semibold |
| Callout | Regular | 32 | 39 | Semibold |
| Subhead | Regular | 30 | 37 | Semibold |
| Footnote | Regular | 27 | 33 | Semibold |
| Caption 1 | Regular | 26 | 32 | Semibold |
| Caption 2 | Regular | 24 | 30 | Semibold |

*Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

#### AX3

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 52 | 61 | Bold |
| Title 1 | Regular | 48 | 57 | Bold |
| Title 2 | Regular | 44 | 52 | Bold |
| Title 3 | Regular | 43 | 51 | Semibold |
| Headline | Semibold | 40 | 48 | Semibold |
| Body | Regular | 40 | 48 | Semibold |
| Callout | Regular | 38 | 46 | Semibold |
| Subhead | Regular | 36 | 43 | Semibold |
| Footnote | Regular | 33 | 40 | Semibold |
| Caption 1 | Regular | 32 | 39 | Semibold |
| Caption 2 | Regular | 29 | 35 | Semibold |

*Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

#### AX4

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 56 | 66 | Bold |
| Title 1 | Regular | 53 | 62 | Bold |
| Title 2 | Regular | 50 | 59 | Bold |
| Title 3 | Regular | 49 | 58 | Semibold |
| Headline | Semibold | 47 | 56 | Semibold |
| Body | Regular | 47 | 56 | Semibold |
| Callout | Regular | 44 | 52 | Semibold |
| Subhead | Regular | 42 | 50 | Semibold |
| Footnote | Regular | 38 | 46 | Semibold |
| Caption 1 | Regular | 37 | 44 | Semibold |
| Caption 2 | Regular | 34 | 41 | Semibold |

*Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

#### AX5

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 60 | 70 | Bold |
| Title 1 | Regular | 58 | 68 | Bold |
| Title 2 | Regular | 56 | 66 | Bold |
| Title 3 | Regular | 55 | 65 | Semibold |
| Headline | Semibold | 53 | 62 | Semibold |
| Body | Regular | 53 | 62 | Semibold |
| Callout | Regular | 51 | 60 | Semibold |
| Subhead | Regular | 49 | 58 | Semibold |
| Footnote | Regular | 44 | 52 | Semibold |
| Caption 1 | Regular | 43 | 51 | Semibold |
| Caption 2 | Regular | 40 | 48 | Semibold |

*Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

### macOS built-in text styles

| Text style | Weight | Size (points) | Line height (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Subheadline | Regular | 11 | 14 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |

*Point size based on image resolution of 144 ppi for @2x designs.*

### Tracking values

#### iOS, iPadOS, visionOS tracking values

##### SF Pro

| Size (points) | Tracking (1/1000 em) | Tracking (points) |
| --- | --- | --- |
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | -6 | -0.08 |
| 14 | -11 | -0.15 |
| 15 | -16 | -0.23 |
| 16 | -20 | -0.31 |
| 17 | -26 | -0.43 |
| 18 | -25 | -0.44 |
| 19 | -24 | -0.45 |
| 20 | -23 | -0.45 |
| 21 | -18 | -0.36 |
| 22 | -12 | -0.26 |
| 23 | -4 | -0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28 | +14 | +0.38 |
| 29 | +14 | +0.40 |
| 30 | +14 | +0.40 |
| 31 | +13 | +0.39 |
| 32 | +13 | +0.41 |
| 33 | +12 | +0.40 |
| 34 | +12 | +0.40 |
| 35 | +11 | +0.38 |
| 36 | +10 | +0.37 |
| 37 | +10 | +0.36 |
| 38 | +10 | +0.37 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.37 |
| 41 | +9 | +0.36 |
| 42 | +9 | +0.37 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.35 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +7 | +0.33 |
| 50 | +7 | +0.34 |
| 51 | +7 | +0.35 |
| 52 | +6 | +0.33 |
| 53 | +6 | +0.31 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +5 | +0.28 |
| 60 | +4 | +0.26 |
| 62 | +4 | +0.24 |
| 64 | +4 | +0.22 |
| 66 | +3 | +0.19 |
| 68 | +2 | +0.17 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.14 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0 |
| 84 | 0 | 0 |
| 88 | 0 | 0 |
| 92 | 0 | 0 |
| 96 | 0 | 0 |

*Not all apps express tracking values as 1/1000 em. Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

##### SF Pro Rounded

| Size (points) | Tracking (1/1000 em) | Tracking (points) |
| --- | --- | --- |
| 6 | +87 | +0.51 |
| 7 | +80 | +0.54 |
| 8 | +72 | +0.57 |
| 9 | +65 | +0.57 |
| 10 | +58 | +0.57 |
| 11 | +52 | +0.56 |
| 12 | +46 | +0.54 |
| 13 | +40 | +0.51 |
| 14 | +35 | +0.48 |
| 15 | +30 | +0.44 |
| 16 | +26 | +0.41 |
| 17 | +22 | +0.37 |
| 18 | +21 | +0.37 |
| 19 | +20 | +0.37 |
| 20 | +18 | +0.36 |
| 21 | +17 | +0.35 |
| 22 | +16 | +0.34 |
| 23 | +16 | +0.35 |
| 24 | +15 | +0.35 |
| 25 | +14 | +0.35 |
| 26 | +14 | +0.36 |
| 27 | +14 | +0.36 |
| 28 | +13 | +0.36 |
| 29 | +13 | +0.37 |
| 30 | +12 | +0.37 |
| 31 | +12 | +0.36 |
| 32 | +12 | +0.38 |
| 33 | +12 | +0.39 |
| 34 | +12 | +0.38 |
| 35 | +11 | +0.38 |
| 36 | +11 | +0.39 |
| 37 | +10 | +0.38 |
| 38 | +10 | +0.39 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.39 |
| 41 | +10 | +0.38 |
| 42 | +10 | +0.39 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.37 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +8 | +0.36 |
| 50 | +7 | +0.34 |
| 51 | +6 | +0.32 |
| 52 | +6 | +0.33 |
| 53 | +6 | +0.31 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +4 | +0.25 |
| 60 | +4 | +0.23 |
| 62 | +4 | +0.21 |
| 64 | +3 | +0.19 |
| 66 | +2 | +0.16 |
| 68 | +2 | +0.13 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.11 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0.00 |
| 84 | 0 | 0.00 |
| 88 | 0 | 0.00 |
| 92 | 0 | 0.00 |
| 96 | 0 | 0.00 |

*Not all apps express tracking values as 1/1000 em. Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

##### New York

| Size (points) | Tracking (1/1000 em) | Tracking (points) |
| --- | --- | --- |
| 6 | +40 | +0.23 |
| 7 | +32 | +0.22 |
| 8 | +25 | +0.20 |
| 9 | +20 | +0.18 |
| 10 | +16 | +0.15 |
| 11 | +11 | +.12 |
| 12 | +6 | +0.07 |
| 13 | +4 | +0.05 |
| 14 | +2 | +0.03 |
| 15 | +0 | +0.00 |
| 16 | -2 | -0.03 |
| 17 | -4 | -0.07 |
| 18 | -6 | -0.11 |
| 19 | -8 | -0.15 |
| 20 | -10 | -0.20 |
| 21 | -10 | -0.21 |
| 22 | -10 | -0.23 |
| 23 | -11 | -0.25 |
| 24 | -11 | -0.26 |
| 25 | -11 | -0.27 |
| 26 | -12 | -0.29 |
| 27 | -12 | -0.32 |
| 28 | -12 | -0.33 |
| 29 | -12 | -0.34 |
| 30 | -12 | -0.37 |
| 31 | -13 | -0.39 |
| 32 | -13 | -0.41 |
| 33 | -13 | -0.42 |
| 34 | -14 | -0.45 |
| 35 | -14 | -0.48 |
| 36 | -14 | -0.49 |
| 38 | -14 | -0.52 |
| 40 | -14 | -0.55 |
| 42 | -14 | -0.57 |
| 44 | -14 | -0.62 |
| 46 | -14 | -0.65 |
| 48 | -14 | -0.68 |
| 50 | -14 | -0.71 |
| 52 | -14 | -0.74 |
| 54 | -15 | -0.79 |
| 58 | -15 | -0.85 |
| 62 | -15 | -0.91 |
| 66 | -15 | -0.97 |
| 70 | -16 | -1.06 |
| 72 | -16 | -1.09 |
| 80 | -16 | -1.21 |
| 88 | -16 | -1.33 |
| 96 | -16 | -1.50 |
| 100 | -16 | -1.56 |
| 120 | -16 | -1.88 |
| 140 | -16 | -2.26 |
| 160 | -16 | -2.58 |
| 180 | -17 | -2.99 |
| 200 | -17 | -3.32 |
| 220 | -18 | -3.76 |
| 240 | -18 | -4.22 |
| 260 | -18 | -4.57 |

*Not all apps express tracking values as 1/1000 em. Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

#### macOS tracking values

| Size (points) | Tracking (1/1000 em) | Tracking (points) |
| --- | --- | --- |
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | -6 | -0.08 |
| 14 | -11 | -0.15 |
| 15 | -16 | -0.23 |
| 16 | -20 | -0.31 |
| 17 | -26 | -0.43 |
| 18 | -25 | -0.44 |
| 19 | -24 | -0.45 |
| 20 | -23 | -0.45 |
| 21 | -18 | -0.36 |
| 22 | -12 | -0.26 |
| 23 | -4 | -0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28 | +14 | +0.38 |
| 29 | +14 | +0.40 |
| 30 | +14 | +0.40 |
| 31 | +13 | +0.39 |
| 32 | +13 | +0.41 |
| 33 | +12 | +0.40 |
| 34 | +12 | +0.40 |
| 35 | +11 | +0.38 |
| 36 | +10 | +0.37 |
| 37 | +10 | +0.36 |
| 38 | +10 | +0.37 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.37 |
| 41 | +9 | +0.36 |
| 42 | +9 | +0.37 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.35 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +7 | +0.33 |
| 50 | +7 | +0.34 |
| 51 | +7 | +0.35 |
| 52 | +6 | +0.31 |
| 53 | +6 | +0.33 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +5 | +0.28 |
| 60 | +4 | +0.26 |
| 62 | +4 | +0.24 |
| 64 | +4 | +0.22 |
| 66 | +3 | +0.19 |
| 68 | +2 | +0.17 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.14 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0 |
| 84 | 0 | 0 |
| 88 | 0 | 0 |
| 92 | 0 | 0 |
| 96 | 0 | 0 |

*Not all apps express tracking values as 1/1000 em. Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.*

## Change log

| Date | Changes |
| --- | --- |
| December 16, 2025 | Added emphasized weights to the Dynamic Type style specifications for each platform. |
| March 7, 2025 | Expanded guidance for Dynamic Type. |
| June 10, 2024 | Added guidance for using Apple’s Unity plug-ins to support Dynamic Type in a Unity-based game and enhanced guidance on billboarding in a visionOS app or game. |
| September 12, 2023 | Added artwork illustrating system font weights, and clarified tvOS specification table descriptions. |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [SF Symbols](sf-symbols.md)

---


<a id="writing"></a>
## writing

# Writing

> Source: <https://developer.apple.com/design/human-interface-guidelines/writing>
> Section: Foundations
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-12-16 (Clarified guidance on language patterns, and added guidance for possessive pronouns.)

The words you choose within your app are an essential part of its user experience.

---

Whether you’re building an onboarding experience, writing an alert, or describing an image for accessibility, designing through the lens of language will help people get the most from your app or game.

## Getting started

**Determine your app’s voice.** Think about who you’re talking to, so you can figure out the type of vocabulary you’ll use. What types of words are familiar to people using your app? How do you want people to feel? The words for a banking app might convey trust and stability, for example, while the words in a game might convey excitement and fun. Create a list of common terms, and reference that list to keep your language consistent. Consistent language, along with a voice that reflects your app’s values, helps everything feel more cohesive.

**Match your tone to the context.** Once you’ve established your app’s voice, vary your tone based on the situation. Consider what people are doing while they’re using your app — both in the physical world and within the app itself. Are they exercising and reached a goal? Or are they trying to make a payment and received an error? Situational factors affect both what you say and how you display the text on the screen.

Compare the tone of these two examples from Apple Watch. In the first, the tone is straightforward and direct, reflecting the seriousness of the situation. In the second, the tone is light and congratulatory.

**Be clear.** Choose words that are easily understood and convey the right thing. Check each word to be sure it needs to be there. If you can use fewer words, do so. When in doubt, read your writing out loud.

**Write for everyone.** For your app to be useful for as many people as possible, it needs to speak to as many people as possible. Choose simple, plain language and write with accessibility and localization in mind, avoiding jargon and gendered terminology. For guidance, see [Writing inclusively](https://help.apple.com/applestyleguide/#/apdcb2a65d68) and [VoiceOver](voiceover.md); for developer guidance, see [Localization](https://developer.apple.com/documentation/xcode/localization).

## Best practices

**Consider each screen’s purpose**. Pay attention to the order of elements on a screen, and put the most important information first. Format your text to make it easy to read. If you’re trying to convey more than one idea, consider breaking up the text onto multiple screens, and think about the flow of information across those screens.

**Be action oriented.** Active voice and clear labels help people navigate through your app from one step to the next, or from one screen to another. When labeling buttons and links, it’s almost always best to use a verb. Prioritize clarity and avoid the temptation to be too cute or clever with your labels. For example, just saying “Send” often works better than “Let’s do it!” For links, avoid using “Click here” in favor of more descriptive words or phrases, such as “Learn more about UX Writing.” This is especially important for people using screen readers to access your app.

**Build language patterns.** Consistency builds familiarity, helping your app feel cohesive, intuitive, and thoughtfully designed. It also makes writing for your app easier, as you can return to these patterns again and again.

**Adopt capitalization rules that align with your app’s style, then apply them consistently.** While certain components, like [button labels](buttons.md#content), have specific guidelines, how you format text reflects your app’s voice. Title case is generally considered formal, while sentence case is more casual. Choose a style for each UI element type and use it consistently throughout your app — for example, title case for all alerts or sentence case for all headlines.

**Give clear guidance and use consistent language throughout processes with multiple steps.** If your app has a flow that spans multiple screens, decide how you want to label the actions that take people from one step to the next. Begin with language like “Get Started” to indicate you’re starting a flow. You can use the button label to hint at the next step, or use terms like “Continue” or “Next,” but be consistent with what you choose. Make it clear when a flow is complete by using language like “Done.”

**Use possessive pronouns sparingly.** Possessive pronouns like *my* and *your* are often unnecessary to establish context. For example, “Favorites” conveys the same message as “Your Favorites,” and is more succinct. If you do use possessive pronouns, use them consistently throughout your app, and try not to switch perspectives. Avoid using *we* altogether because it may be unclear who the “we” in question refers to. This is particularly problematic in error messages like “We’re having trouble loading this content.” Something like “Unable to load content” is much clearer.

**Write for how people use each device.** People may use your app on several types of devices. While your language needs to be consistent across them, think about where it would be helpful to adjust your text to make it suitable for different devices. Make sure you describe gestures correctly on each device — for example, not saying “click” for a touch device like iPhone or iPad where you mean “tap.”

Where and how people use a device, its screen size, and its location all affect how you write for your app. iPhone and Apple Watch, for example, offer opportunities for personalization, but their small screens require brevity. TVs, on the other hand, are often in common living spaces, and several people are likely to see anything on the screen, so consider who you’re addressing. Bigger screens also require brevity, as the text must be large for people to see it from a distance.

**Provide clear next steps on any blank screens.** An empty state, like a completed to-do list or bookmarks folder with nothing in it, can provide a good opportunity to make people feel welcome and educate them about your app. Empty states can also showcase your app’s voice, but make sure that the content is useful and fits the context. An empty screen can be daunting if it isn’t obvious what to do next, so guide people on actions they can take, and give them a button or link to do so if possible. Remember that empty states are usually temporary, so don’t show crucial information that could then disappear.

**Write clear error messages.** It’s always best to help people avoid errors. When an error message is necessary, display it as close to the problem as possible, avoid blame, and be clear about what someone can do to fix it. For example, “That password is too short” isn’t as helpful as “Choose a password with at least 8 characters.” Remember that errors can be frustrating. Interjections like “oops!” or “uh-oh” are typically unnecessary and can sound insincere. If you find that language alone can’t address an error that’s likely to affect many people, use that as an opportunity to rethink the interaction.

**Choose the right delivery method.** There are many ways to get people’s attention, whether or not they are actively using your app. When there’s something you want to communicate, consider the urgency and importance of the message. Think about the context in which someone might see the message, whether it requires immediate action, and how much supporting information someone might need. Choose the correct delivery method, and use a tone appropriate for the situation. For guidance, see [Notifications](notifications.md), [Alerts](alerts.md), and [Action sheets](action-sheets.md).

**Keep settings labels clear and simple.** Help people easily find the settings they need by labeling them as practically as possible. If the setting label isn’t enough, add an explanation. Describe what it does when turned on, and people can infer the opposite. In the Handwashing Timer setting for Apple Watch, for example, the description explains that a timer can start when you’re washing your hands. It isn’t necessary to tell you that a timer won’t start when this setting is off.

If you need to direct someone to a setting, provide a direct link or button, rather than trying to describe its location. For guidance, see [Settings](settings.md).

**Show hints in text fields.** If your app allows people to enter their own text, like account or contact information, label all fields clearly, and use hint or placeholder text so people know how to format the information. You can give an example in hint text, like “name@example.com,” or describe the information, such as “Your name.” Show errors right next to the field, and instruct people how to enter the information correctly, rather than scolding them for not following the rules. “Use only letters for your name” is better than “Don’t use numbers or symbols.” Avoid robotic error messages with no helpful information, like “Invalid name.” For guidance, see [Text fields](text-fields.md).

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| December 16, 2025 | Clarified guidance on language patterns, and added guidance for possessive pronouns. |
| February 27, 2023 | New page. |

## Related guidelines

- [Inclusion](inclusion.md)
- [Accessibility](accessibility.md)
- [Color](color.md)

---
