# Apple HIG — Patterns
Bundled HIG pages for the “Patterns” group. Each page kept verbatim under an anchor heading `## <slug>`. Cite as **patterns.md › <slug> › heading**.


<a id="charting-data"></a>
## charting-data

# Charting data

> Source: <https://developer.apple.com/design/human-interface-guidelines/charting-data>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)

Presenting data in a chart can help you communicate information with clarity and appeal.

---

Charts provide efficient ways to communicate complex information without requiring people to read and interpret a lot of text. The graphical nature of charts also gives you additional opportunities to express the personality of your experience and add visual interest to your interface. To learn about the components you use to create a chart, see [Charts](charts.md).

A chart can range from a simple graphic that provides glanceable information to a rich, interactive experience that can form the centerpiece of your app and encourage people to explore the data from various perspectives. Whether simple or complex, you can use charts to help people perform data-driven tasks that are important to them, such as:

- Analyzing trends based on historical or predicted values
- Visualizing the current state of a process, system, or quantity that changes over time
- Evaluating different items — or the same item at different times — by comparing data across multiple categories

Not every collection of data needs to be displayed in a chart. If you simply need to provide data — and you don’t need to convey information about it or help people analyze it — consider offering the data in other ways, such as in a list or table that people can scroll, search, and sort.

## Best practices

**Use a chart when you want to highlight important information about a dataset.** Charts are visually prominent, so they tend to draw people’s attention. Take advantage of this prominence by clearly communicating what people can learn from the data they care about.

**Keep a chart simple, letting people choose when they want additional details.** Resist the temptation to pack as much data as possible into a chart. Too much data can make a chart visually overwhelming and difficult to use, obscuring the relationships and other information you want to convey. If you have a lot of data to present — or a lot of functionality to provide — consider giving people a way to reveal it gradually. For example, you might let people choose to view different levels of detail or subsets of data to match their interest. To help people learn how to use an interactive chart, you might offer several versions of the chart, each with more functionality than the last.

**Make every chart in your app accessible.** A chart communicates visually through graphical representations of data and visual descriptions. In addition to the visual descriptions you display, it’s crucial to provide both accessibility labels that describe chart values and components, and accessibility elements that help people interact with the chart. For guidance, see [Enhancing the accessibility of a chart](charts.md#enhancing-the-accessibility-of-a-chart).

## Designing effective charts

**In general, prefer using common chart types.** People tend to be familiar with common chart types — such as bar charts and line charts — so using one of these types in your app can make it more likely that people will already know how to read your chart. For guidance, see [Charts](charts.md).

**If you need to create a chart that presents data in a novel way, help people learn how to interpret the chart.** For example, when a Watch pairs with iPhone, Activity introduces the Activity rings by animating them individually, showing people how each ring maps to the move, exercise, and stand metrics.

**Examine the data from multiple levels or perspectives to find details you can display to enhance the chart.** For example, viewing the data from a macro level can help you determine high-level summaries that people might be interested in, like totals or averages. From a mid-level perspective, you might find ways to help people identify useful subsets of the data, whereas examining individual data points might help you find ways to draw people’s attention to specific values or items. Displaying information that helps people view the chart from various perspectives can encourage them to engage with it.

**Aid comprehension by adding descriptive text to the chart.** Descriptive text titles, subtitles, and annotations help emphasize the most important information in a chart and can highlight actionable takeaways. You can also display brief descriptive text that serves as a headline or summary for a chart, helping people grasp essential information at a glance. For example, Weather displays text that summarizes the information people need right now — such as “Chance of light rain in the next hour” — above the scrolling list of hourly forecasts for the next 24 hours. Although a descriptive headline or summary can make a chart more accessible, it doesn’t take the place of accessibility labels.

**Match the size of a chart to its functionality, topic, and level of detail.** In general, a chart needs to be large enough to comfortably display the details you need to include and expansive enough for the interactivity you want to support. For example, you always want to make it easy for people to read a chart’s details and descriptive text — like labels and annotations — but you might also want to give people enough room to change the scope of a chart or investigate the data from different perspectives. On the other hand, you might want to use a small chart to offer glanceable information about an individual item or to provide a snapshot or preview of a larger version of the chart that people can reveal in a different view.

**Prefer consistency across multiple charts, deviating only when you need to highlight differences.** If multiple charts in your app serve a similar purpose, you generally don’t want to imply that the charts are unrelated by using a different type or style for each one.  Also, using a consistent visual approach for the charts in your app lets people use what they learn about one chart to help them understand another. Consider using different chart types and styles when you need to highlight meaningful differences between charts.

**Maintain continuity among multiple charts that use the same data.** When you use multiple charts to help people explore one dataset from different perspectives, it’s important to use one chart type and consistent colors, annotations, layouts, and descriptive text to signal that the dataset remains the same. For example, the Health Trends screen shows small charts that each use a specific visual style to depict a recent trend in an area like steps or resting heart rate. When people choose a chart to reveal all their data in that area, the expanded version uses the same style, colors, marks, and annotations to strengthen the relationship between the versions.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| September 23, 2022 | New page. |

## Related guidelines

- [Charts](charts.md)

---


<a id="collaboration-and-sharing"></a>
## collaboration-and-sharing

# Collaboration and sharing

> Source: <https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to visionOS, watchOS omitted)
> Last change on Apple's site: 2023-12-05 (Added artwork illustrating button placement and various types of collaboration permissions.)

Great collaboration and sharing experiences are simple and responsive, letting people engage with the content while communicating effectively with others.

---

System interfaces and the Messages app can help you provide consistent and convenient ways for people to collaborate and share. For example, people can share content or begin a collaboration by dropping a document into a Messages conversation or selecting a destination in the familiar share sheet.

After a collaboration begins, people can use the Collaboration button in your app to communicate with others, perform custom actions, and manage details. In addition, people can receive Messages notifications when collaborators mention them, make changes, join, or leave.

You can take advantage of Messages integration and the system-provided sharing interfaces whether you implement collaboration and sharing through CloudKit, iCloud Drive, or a custom solution. To offer these features when you use a custom collaboration infrastructure, make sure your app also supports universal links (for developer guidance, see [Supporting universal links in your app](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app)).

With SharePlay, people can also take part in your app’s activities together in real time, from their own devices. For guidance, see SharePlay.

## Best practices

**Place the Share button in a convenient location, like a toolbar, to make it easy for people to start sharing or collaborating.** In iOS 16, the system-provided share sheet includes ways to choose a file-sharing method and set permissions for a new collaboration; iPadOS 16 and macOS 13 introduce similar appearance and functionality in the sharing popover. In your SwiftUI app, you can also enable sharing by presenting a share link that opens the system-provided share sheet when people choose it; for developer guidance, see [ShareLink](https://developer.apple.com/documentation/swiftui/sharelink).

**If necessary, customize the share sheet or sharing popover to offer the types of file sharing your app supports.** If you use CloudKit, you can add support for sending a copy of a file by passing both the file and your collaboration object to the share sheet. Because the share sheet has built-in support for multiple items, it automatically detects the file and makes the “send copy” functionality available. With iCloud Drive, your collaboration object supports “send copy” functionality by default. For custom collaboration, you can support “send copy” functionality in the share sheet by including a file — or a plain text representation of it — in your collaboration object.

**Write succinct phrases that summarize the sharing permissions you support.** For example, you might write phrases like “Only invited people can edit” or “Everyone can make changes.” The system uses your permission summary in a button that reveals a set of sharing options that people use to define the collaboration.

**Provide a set of simple sharing options that streamline collaboration setup.** You can customize the view that appears when people choose the permission summary button to provide choices that reflect your collaboration functionality. For example, you might offer options that let people specify who can access the content and whether they can edit it or just read it, and whether collaborators can add new participants. Keep the number of custom choices to a minimum and group them in ways that help people understand them at a glance.

**Prominently display the Collaboration button as soon as collaboration starts.** The system-provided Collaboration button reminds people that the content is shared and identifies who’s sharing it. Because the Collaboration button typically appears after people interact with the share sheet or sharing popover, it works well to place it next to the Share button.

**Provide custom actions in the collaboration popover only if needed.** Choosing the Collaboration button in your app reveals a popover that consists of three sections. The top section lists collaborators and provides communication buttons that can open Messages or FaceTime, the middle section contains your custom items, and the bottom section displays a button people use to manage the shared file. You don’t want to overwhelm people with too much information, so it’s crucial to offer only the most essential items that people need while they use your app to collaborate. For example, Notes summarizes the most recent updates and provides buttons that let people get more information about the updates or view more activities.

**If it makes sense in your app, customize the title of the modal view’s collaboration-management button.** People choose this button — titled “Manage Shared File” by default — to reveal the collaboration-management view where they can change settings and add or remove collaborators. If you use CloudKit sharing, the system provides a management view for you; otherwise, you create your own.

**Consider posting collaboration event notifications in Messages.** Choose the type of event that occurred — such as a change in the content or the collaboration membership, or the mention of a participant — and include a universal link people can use to open the relevant view in your app. For developer guidance, see [SWHighlightEvent](https://developer.apple.com/documentation/sharedwithyou/swhighlightevent).

## Platform considerations

*No additional considerations for iOS, iPadOS, or macOS. Not available in tvOS.*

## Change log

| Date | Changes |
| --- | --- |
| December 5, 2023 | Added artwork illustrating button placement and various types of collaboration permissions. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | New page. |

## Related guidelines

- [Activity views](activity-views.md)

---


<a id="drag-and-drop"></a>
## drag-and-drop

# Drag and drop

> Source: <https://developer.apple.com/design/human-interface-guidelines/drag-and-drop>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to visionOS omitted)
> Last change on Apple's site: 2023-10-24 (Added artwork.)

Using drag and drop, people can move or duplicate selected photos, text, and other content by dragging the selection from one location to another.

---

To perform drag and drop, people select content in one location, called the *source*, and drop it in another, called the *destination*. These locations can be in the same container — like a text view — or in different containers, like text views on opposite sides of a split view, or even in different apps.

Depending on various factors, the drag and drop action might *move* the selected content to the destination or *copy* it. After a successful drop, moved content exists only in the destination; copied content exists in both locations. As a general rule, dropping selected content within the same container moves it, whereas dropping content in a different container copies it. Dragging and dropping content between apps always results in a copy.

People use different interactions to perform drag and drop depending on platform. For example:

- In visionOS, people pinch and hold a virtual object while dragging it to a new location in any direction, including along the z-axis.
- iOS and iPadOS support drag and drop through gestures on the touchscreen, interactions with a pointing device, and through full keyboard-access mode.
- Universal Control lets people drag content between their Mac and iPad.
- On a Mac, people can interact with a pointing device, use full keyboard access mode, or use VoiceOver to perform drag and drop.

## Best practices

**As much as possible, support drag and drop throughout your app.** Most people are familiar with drag and drop and they often try it everywhere. When you use system-provided components — such as text fields and text views — you get built-in support for drag and drop.

**Offer alternative ways to accomplish drag-and-drop actions.** Sometimes, drag-and-drop operations are inconvenient or impossible for people to perform, so it’s important to provide other ways to do the same things. For example, you can include menu commands that people can use to copy an item and move it to another location. In iOS and iPadOS, you can use accessibility APIs to identify sources and destinations so that people can use assistive technologies to drag and drop in your app (for developer guidance, see [accessibilityDragSourceDescriptors](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitydragsourcedescriptors) and [accessibilityDropPointDescriptors](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitydroppointdescriptors)).

**Determine when dragging and dropping content within your app results in a move or a copy.** In general, a move makes sense when the source and destination containers are the same — such as dragging text from one location to another within a document — and a copy makes sense when they’re different, like dragging an image from one document to another. Before you change these defaults, consider the behavior that most people expect and prefer the one that is least likely to result in frustration or data loss.

**Support multi-item drag and drop when it makes sense.** People appreciate the convenience of dragging a group of items to a destination, instead of dragging each item separately. In iOS, iPadOS, macOS, and visionOS, people can select multiple items and drag them as a group; macOS also lets people select multiple items from several apps and drag them as a group. In iPadOS, people can select an item, start dragging it, and add other items to the group without stopping the drag operation.

**Prefer letting people undo a drag-and-drop operation.** Sometimes, people inadvertently drop content in the wrong destination, so they appreciate being able to undo the action and return to their previous state. You might also be able to help people avoid mistakes by asking for confirmation before completing a drag-and-drop operation that can’t be undone. In macOS, for example, the Finder asks for confirmation when people drag a file into a write-only folder because they won’t be able to open the folder and remove the dropped item. In some situations, it might make sense to provide a way to reverse the results of drag and drop when people can’t undo it. For example, Photos lets people cancel photo sharing after dropping a photo into a shared photo stream.

**Consider offering multiple versions of dragged content, ordered from highest to lowest fidelity.** By providing multiple alternatives, the destination can choose the highest quality version it can accept. For example, if people can drag a line drawing they created in your app, you could offer a PDF vector representation, a lossless PNG image with transparency, and a lossy JPEG image without transparency, in that order. Another example is an app that uses rich, complicated objects, like charts. This app might offer the native chart object followed by a simpler version — like an image of the chart — for destinations that don’t support chart objects.

**Consider supporting spring loading.** Spring loading lets people activate certain controls, like buttons and segmented controls, by dragging selected content over them. For example, Calendar lets people drag a selected event over the day, week, month, or year segments in the toolbar, giving them a convenient way to move the event to a different date. On a Mac equipped with a Magic Trackpad, a button or segmented control can activate when people force-click it while continuing to hold the content; on iPad, these components can activate when people hover over them while holding the content.

## Providing feedback

Drag and drop is a dynamic process that can result in multiple outcomes. To help people feel in control the process, it’s crucial to provide clear and continuous feedback throughout.

**Display a drag image as soon as people drag a selection about three points.** It works well to create a translucent representation of the content people are dragging. Translucency helps distinguish the representation from the original content and lets people see destinations as they pass over them. Display the drag image until people drop the content.

**If it adds clarity, modify the drag image to help people predict the result of a drag-and-drop operation.** For example, when dragging a photo into a document, the drag image could expand to show the default size of the photo in the document. You can also use drag *flocking* to visually group multiple drag items — letting people confirm that they haven’t missed an item they want to drag — and then ungroup the items when people drop them. Although changing the drag image can provide valuable feedback, avoid creating a distracting experience in which the drag image is constantly and radically changing.

**Show people whether a destination can accept dragged content.** For example, you might display an insertion point or highlight a containing view only when the destination can accept a dragged item, and show no visual feedback — or an explicit “not allowed” image, like the `circle.slash` from SF Symbols — when it can’t. Display highlighting or other visual cues only while the content is positioned above the destination, removing the visual feedback when people drag the content away. When there are multiple possible destinations, provide visual cues that help people identify one at a time.

**When people drop an item on an invalid destination, or when dropping fails, provide visual feedback.** For example, the item can move back from its current location to its source (if the source is still visible) or it can scale up and fade out to give the impression of the item evaporating instead of landing successfully.

## Accepting drops

**Scroll the contents of a destination when necessary.** When people drag an item within a scrolling container that has a lot of content, the content can automatically scroll as people move the item over it. This behavior makes it easy for people to find the right place to drop the item, but if they continue the drag operation outside of the container, automatic scrolling is no longer necessary. System-provided text views and text fields behave this way by default.

**When there’s a choice, pick the richest version of dropped content your app can accept.** For example, if people drag a chart object from another app, the drag operation might offer both the rich, native chart object and a simple image of it. If your app supports charts, extract and display the native chart object; it it doesn’t, use the image instead.

**Extract only the relevant portion of dropped content if necessary.** For example, when people drag a contact to a recipient field in an email, Mail displays only the name and email address, not the contact’s address information.

**When a physical keyboard is attached, check for the Option key at drop time.** When people hold the Option key while dragging, they can force a drag-and-drop operation within the same container to behave like a copy. If people stop holding Option before dropping content in the same container, the drag operation results in a move.

**Provide feedback when dropped content needs time to transfer.** For example, you might display a progress indicator to help people estimate how long the transfer will take. In collections, lists, and tables, you might also display a placeholder at the drop location so people know where to find the content after it finishes transferring. The system can display an alert when a time-consuming transfer occurs between apps.

**Provide feedback when dropped content initiates a task or action.** If people drop content onto a control that initiates a task — such as printing — show people that the task has begun and keep them informed of its progress.

**Apply appropriate styling to dropped text.** When the source and destination both support the same text styles, make sure dropped text maintains its original font, typeface, size, and other attributes. Otherwise, apply the destination’s style to dropped text.

**After a drop, maintain the content’s selection state in the destination, updating it in the source as needed.** People expect the content they drop to remain selected so they can immediately act on it. When the source and destination are the same container, the content disappears from its original location when the drag operation performs a move. When a drag operation within the same container performs a copy, remove the selection state from the content that remains in the original location. When people drag selected content to a different container, deselect the content in the source.

## Platform considerations

*Not supported in tvOS or watchOS.*

### Mobile (iOS, iPadOS)

**Let people perform multiple simultaneous drag activities.** In iPadOS, people can sequentially add items to an in-progress drag session, gathering as many items as their fingers can handle. For example, people can select an app icon on the Home Screen, start dragging it, and select additional app icons before dropping all of them in a different Home Screen or in a folder. To support this interaction, you need to let people add items during a drag — providing visual feedback through flocking — and accept multiple, simultaneous drops.

### Desktop (macOS)

**Consider letting people drag content from your app into the Finder.** When you support this, be sure to present the content in a format your app can open later. For example, Calendar lets people drag an event to the Finder as a `.ics` file. People can share this file with others or drag it back to Calendar to open it. When necessary, you can output dragged content in a *clipping*, which is a temporary container for storing dragged content. For example, most system apps let people drag text to the Finder, where it appears as a clipping. Later, people can drag the clipping into a text field or other location that accepts text. Note that a drag-and-drop clipping isn’t related to the Clipboard.

**Let people drag selected content from an inactive window without first making the window active.** Selected content in an inactive window is known as a *background selection* and has a different appearance from selected content in the active window. In general, people expect to drag a background selection to the active window without bringing the inactive window forward.

**When possible, let people drag individual items from an inactive window without affecting an existing background selection.** For example, people can drag an unselected file from an inactive Finder window without deselecting any of the window’s selected files.

**Consider displaying a badge during multi-item drag operations.** A badge is a small filled oval containing a number you can use to indicate the number of items people are dragging. If a destination can accept only a subset of dragged items, update the badge to show the new number.

**Consider changing the pointer appearance to indicate what will happen when people drop content.** In addition to using the *copy* pointer, you might want to use the *drag link*, *disappearing item*, and *operation not allowed* pointers, depending on the situation. For guidance, see [Pointers](pointing-devices.md#pointers).

**As much as possible, let people select and drag content with a single motion.** Unless people are selecting multiple items, they appreciate it when they don’t have to pause between making a selection and starting the drag operation.

## Change log

| Date | Changes |
| --- | --- |
| October 24, 2023 | Added artwork. |
| June 21, 2023 | Updated to include guidance for visionOS. |

---


<a id="entering-data"></a>
## entering-data

# Entering data

> Source: <https://developer.apple.com/design/human-interface-guidelines/entering-data>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2023-06-21 (Updated to include guidance for visionOS.)

When you need information from people, design ways that make it easy for them to provide it without making mistakes.

---

Entering information can be a tedious process regardless of the interaction methods people use. Improve the experience by:

- Pre-gathering as much information as possible to minimize the amount of data that people need to supply
- Supporting all available input methods so people can choose the method that works for them

## Best practices

**Get information from the system whenever possible.** Don’t ask people to enter information that you can gather automatically — such as from settings — or by getting their permission, such as their location or calendar information.

**Be clear about the data you need.** For example, you might display a prompt in a text field — like “username@company.com” — or provide an introductory label that describes the information, like “Email.” You can also prefill fields with reasonable default values, which can minimize decision making and speed data entry.

**Use a secure text-entry field when appropriate.** If your app or game needs sensitive data, use a field that obscures people’s input as they enter it, typically by displaying a small filled circle symbol for each character. For developer guidance, see [SecureField](https://developer.apple.com/documentation/swiftui/securefield). In tvOS, you can also configure a digit entry view to obscure the numerals people enter (for developer guidance, see [isSecureDigitEntry](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller/issecuredigitentry)). When you use the system-provided text field in visionOS, the system shows the entered data to the wearer, but not to anyone else; for example, a secure text field automatically blurs when people use AirPlay to stream their content.

**Never prepopulate a password field.** Always ask people to enter their password or use biometric or keychain authentication. For guidance, see [Managing accounts](managing-accounts.md).

**When possible, offer choices instead of requiring text entry.** It’s usually easier and more efficient to choose from lists of options than to type information, even when a keyboard is conveniently available. When it makes sense, consider using a picker, menu, or other selection component to give people an easy way to provide the information you need.

**As much as possible, let people provide data by dragging and dropping it or by pasting it.** Supporting these interactions can ease data entry and make your experience feel more integrated with the rest of the system.

**Dynamically validate field values.** People can get frustrated when they have to go back and correct mistakes after filling out a lengthy form. When you verify values as soon as people enter them — and provide feedback as soon as you detect a problem — you give them the opportunity to correct errors right away. For numeric data in particular, consider using a number formatter, which automatically configures a text field to accept only numeric values. You can also configure a formatter to display the value in a specific way, such as with a certain number of decimal places, as a percentage, or as currency.

**When data entry is necessary, make sure people understand that they must provide the required data before they can proceed.** For example, if you include a Next or Continue button after a set of text fields, make the button available only after people enter the data you require.

## Platform considerations

*No additional considerations for iOS, iPadOS, tvOS, visionOS, or watchOS.*

### Desktop (macOS)

**Consider using an expansion tooltip to show the full version of clipped or truncated text in a field.** An *expansion tooltip* behaves like a regular tooltip, appearing when the pointer rests on top of a field. Apps running in macOS — including iOS and iPadOS apps running on a Mac — can use an expansion tooltip to help people view the complete data they entered when a text field is too small to display it. For guidance, see [Offering help > macOS, visionOS](offering-help.md#desktop-macos-visionos).

## Change log

| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [Text fields](text-fields.md)
- [Virtual keyboards](virtual-keyboards.md)
- [Keyboards](keyboards.md)

---


<a id="feedback"></a>
## feedback

# Feedback

> Source: <https://developer.apple.com/design/human-interface-guidelines/feedback>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)

Feedback helps people know what’s happening, discover what they can do next, understand the results of actions, and avoid mistakes.

---

Providing clear, consistent feedback as people interact with your app or game can make it feel intuitive and encourage deeper exploration. Feedback can communicate several different things, such as:

- The current status of something
- The success or failure of an important task or action
- A warning about an action that can have negative consequences
- An opportunity to correct a mistake or problematic situation

The most effective feedback tends to match the significance of the information to the way it’s delivered. For example, it often works well to display status information in a passive way so that people can view it when they need it. In contrast, a warning about possible data loss needs to interrupt people so they have a chance to avoid the problem.

## Best practices

**Make sure all feedback is accessible.** When you use multiple ways to provide feedback, you reach more people and give them the opportunity to receive the feedback in ways that work for them. For example, when you provide feedback using color, text, sound, and haptics, people can receive it whether they silence their device, look away from the screen, or use VoiceOver. (For guidance on providing haptic feedback, see [Playing haptics](playing-haptics.md).)

**Consider integrating status feedback into your interface.** When status feedback is available near the items it describes, people get important information without having to take action or leave their current context. For example, Mail in iOS and iPadOS describes the most recent update and displays the number of unread messages in the toolbar of the mailbox screen, making the information unobtrusive but easy for people to check when they’re interested.

**Use alerts to deliver critical — and ideally actionable — information.** By design, alerts disrupt the current context, so you need to match the importance of the information to the level of interruption. Alerts can lose their impact if you use them too often or to deliver unimportant information. For guidance, see [Alerts](alerts.md).

**Warn people when they initiate a task that can cause data loss that’s unexpected and irreversible.** In contrast, don’t warn people when data loss is the expected result of their action. For example, the Finder doesn’t warn people every time they throw away a file because deleting the file is the expected result.

**When it makes sense, confirm that a significant action or task has completed.** For example, people appreciate getting feedback that confirms a successful Apple Pay transaction. It’s generally best to reserve this type of confirmation for activities that are sufficiently important — because people typically expect their action or task to succeed, they only need to know when it doesn’t.

**Show people when a command can’t be carried out and help them understand why.** For example, if people request directions without specifying a destination, Maps tells them that it can’t provide directions to and from the same location.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.*

## Related guidelines

- [Playing audio](playing-audio.md)
- [Playing haptics](playing-haptics.md)
- [Motion](motion.md)

---


<a id="file-management"></a>
## file-management

# File management

> Source: <https://developer.apple.com/design/human-interface-guidelines/file-management>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2024-06-10 (Added guidelines for using the document launcher in iOS and iPadOS.)

Some apps can support documents and files that people expect to manage throughout the system.

---

Document-based apps — such as Pages, Keynote, Photos, and Preview — help people create, edit, and save documents and files, often providing customized ways for people to browse for content they want to open in the app.

People also expect to browse documents without first opening a document-based app. On a Mac, for example, people use the Finder to access the macOS file system; on iPhone, iPad, and Apple Vision Pro, people use the Files app to manage the documents and files on their device. In watchOS and tvOS, people don’t typically create, edit, or manage documents, so these systems don’t provide a document-browsing interface.

## Creating and opening files

**Use app menus and keyboard shortcuts to give people convenient ways to create and open documents.** In iPadOS and macOS, people expect to create new documents or open existing ones using familiar menu commands. When you provide commands like New or Open, iPadOS presents them in the shortcuts interface that displays when people hold the Command key on a connected hardware keyboard, and macOS presents them in the menu bar File menu. Regardless of the availability of keyboard shortcuts, include an Add (+) button to help people create a new document. In a macOS app, you put the add action in the File menu (for guidance, see [File menu](the-menu-bar.md#file-menu)).

**If your app requires a custom file browser, support people’s understanding of the platform’s file system.** People who are familiar with the Finder and Files apps already understand the basic layout of their device’s file system. Although you might want to show the most relevant part of the file system when your custom file browser opens — for example, a Documents or iCloud folder or the most recently selected location — let people use your browser to view the rest of the file system if they want.

## Saving work

**Help people be confident that their work is always preserved unless they cancel or delete it.** In general, avoid making people take an explicit action to save their work. Instead, automatically perform periodic saves while they’re editing and when they close a file or switch to another app.

**Hide file extensions by default, but let people view them if they choose.** Be sure to reflect the current choice in all the save or open interfaces you display.

## Quick Look previews

Quick Look helps you create previews of the files your app handles so that people can view them within your app and in some cases interact with them. For example, you can use Quick Look to let people listen to a preview of an audio file, add markup to a photo’s preview, or rotate and scale a 3D file preview to examine it in different ways.

**Use a Quick Look viewer to let people preview a file even when your app can’t open it.** If your app lets people attach or otherwise interact with files that it doesn’t support, implementing a Quick Look viewer lets people preview those files without leaving your app.

**Consider implementing a Quick Look generator if your app produces custom file types.** A Quick Look generator lets other apps — including the Finder, Files, and Spotlight — display previews of your documents, making it easier for people to find them.

## Platform considerations

### Mobile (iOS, iPadOS)

#### Document launcher

Starting in iOS 18 and iPadOS 18, document-based apps can use the system’s document launcher to give people a consistent, highly graphical way to browse, open, and create files. The document launcher presents a full-screen experience that highlights key elements of your app’s theme, while making it easy for people to create new documents. For developer guidance, see [DocumentGroupLaunchScene](https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene).

The document launcher consists of three main parts:

- A *title card* that displays the app title and two app-specific buttons
- A background image that appears behind the title card and additional images — called *accessories* — that can appear around it
- A sheet that contains a file browser and optional app-specific controls

You can customize all three parts of the document launcher. Although the system automatically displays your app name in the title card, you specify the text and functions of the card’s primary and secondary buttons. You can also create a custom background image, one or more accessory images to surround the title card, and provide some custom controls that can appear in the file browser’s toolbar.

**Assign the title card’s buttons to your app’s most important functions.** The primary button typically creates a new document, and the secondary button can provide additional options. For example, the primary button in Numbers is Start Writing and the secondary button is Choose a Template.

**Provide a background that’s clearly distinct from the accessories and title card.** You can use a solid color, a gradient, or a pattern. Avoid including complex images or patterns that might distract from foreground elements.

**Be mindful of accessory placement.** For example, you can place accessories both in front of and behind the title card to create the appearance of depth, but you need to make sure that your app name and both buttons remain clearly visible. Avoid cluttering the title card with too many accessories, and be sure to test its overall appearance across the range of screen sizes and device orientations that you support.

**Use animation sparingly.** Too much motion on the display can confuse or disorient people. If you want to animate your accessories, consider creating gentle, repeating animations that subtly highlight and enhance your app’s content. For example, you might create an animation that makes an accessory appear to breathe or sway softly. For guidance, see [Motion](motion.md).

#### File provider app extension

If your app can share its files with other apps, you can create a file provider app extension that displays a custom interface for importing, exporting, opening, and moving your app’s documents. For developer guidance, see [File Provider](https://developer.apple.com/documentation/fileprovider). An *app extension* is code you provide that people can install and use to extend the functionality of a specific area of the system; to learn more, see [App extensions](https://developer.apple.com/app-extensions/).

**When someone uses your file provider extension to open or import documents, display only documents that are appropriate in the current context.** For example, if a PDF-editing app loads your extension, only list PDF files for opening or import. You might also want to display additional information, such as modification dates, sizes, and whether documents are local or remote.

**Let people select a destination when exporting and moving documents.** Unless your app stores documents in a single directory, let people navigate to a specific destination in your directory hierarchy. You could also provide a way to add new subdirectories.

**Avoid including a custom top toolbar.** Your extension loads within a modal view that already includes a toolbar. Providing a second toolbar is confusing and takes space away from your content.

Your app can also let people browse and open files from other apps. For developer guidance, see [Adding a document browser to your app](https://developer.apple.com/documentation/uikit/adding-a-document-browser-to-your-app).

### Desktop (macOS)

#### Custom file management

People have strong associations with the familiar file browsing experience of the Finder and most document-based apps. Use the default file browser unless you have an important reason to create a custom one.

**Make your custom file-opening interface convenient.** For example, people might appreciate an “open recent” action in addition to the simple “open” action. You might also want to let people choose criteria on which to filter the file-browsing experience, or select multiple documents to open at once. In a macOS open panel, you can customize the title of the Open button to reflect the task — for example, if your app lets people insert a file’s contents into the current document, you might change the title to Insert.

**Provide a save interface to let people change a file’s name, format, or location.** By default, a new document’s title is “Untitled” until people choose a custom name. As with a document-opening interface, a save view can also provide a browsing experience that defaults to a logical location to help people place the saved document where they want. If you support saving content in different formats, also give people a way to choose a specific file format.

**Consider extending the functionality of the Save dialog.** If it makes sense in your app, you can add a custom accessory view containing useful settings or options to the Save dialog. For example, the dialog for saving Mail messages as files contains an option to include attachments.

#### Finder Sync extensions

If your app syncs local and remote files, you can create a Finder Sync app extension to express file synchronization status and control within the Finder. For developer guidance, see [Finder Sync](https://developer.apple.com/documentation/findersync).

For example, you can use a Finder Sync extension to:

- Display badges in the Finder to indicate the sync status of items
- Provide custom contextual menu items that perform file and folder management tasks, like favoriting and adding password-protection
- Provide custom toolbar buttons that perform global actions, like initiating a sync operation

**Help people avoid losing work if they turn off autosaving.** People can turn off autosaving by selecting the “Ask to keep changes when closing documents” toggle in Desktop & Dock settings. In this scenario, show that a document has unsaved changes and present a save dialog when people choose to close the document, quit your app, log out, or restart.

**When autosaving is off, make sure people know when a document has unsaved changes.** To show that there are unsaved changes, display a dot on the document window’s close button and next to the document’s name in your app’s Window menu. When autosaving is on, showing a dot in these locations is confusing, because it implies that people need to take action to avoid losing their work. Regardless of autosave status, you can append “Edited” to the document’s title in the title bar, but be sure to remove this suffix as soon as autosave occurs or when people explicitly save their work.

## Change log

| Date | Changes |
| --- | --- |
| June 10, 2024 | Added guidelines for using the document launcher in iOS and iPadOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [Toolbars](toolbars.md)
- [Printing](printing.md)

---


<a id="going-full-screen"></a>
## going-full-screen

# Going full screen

> Source: <https://developer.apple.com/design/human-interface-guidelines/going-full-screen>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS
> Last change on Apple's site: 2025-06-09 (Updated guidance for hiding toolbars and navigation controls, and deferring Home Screen indicator gestures in full-screen iOS and iPadOS apps and games.)

iPhone, iPad, and Mac offer full-screen modes that let people expand a window to fill the screen, hiding system controls and providing a distraction-free environment.

---

Apple TV and Apple Watch don’t offer full-screen modes because apps and games already fill the screen by default. Apple Vision Pro doesn’t offer a full-screen mode because people can expand a window to fill more of their view or use the Digital Crown to hide passthrough and transition to a more immersive experience (for guidance, see Immersive experiences).

## Best practices

**Support full-screen mode when it makes sense for your experience.** People appreciate full-screen mode when they want to concentrate on a task or be immersed in content. Consider offering a full-screen mode if your experience lets people play a game; view media like videos or photo slideshows; or perform an in-depth task that benefits from a distraction-free environment.

**If necessary, adjust your layout in full-screen mode, but don’t programmatically resize your window.** When a window is larger in full-screen mode than in non-full-screen mode, you want to keep essential content prominent while making good use of the extra space. For example, it might make sense to adjust the proportions of your interface without changing which items appear. If you make such adjustments, be sure they’re subtle enough to maintain a consistent interface and avoid causing visually jarring transitions between modes.

**Continue to provide access to essential features and controls so people can complete their task without exiting full-screen mode.** For example, a full-screen media experience needs to make playback controls persistently available or easy to reveal when people need them.

**Except in games, let people reveal the Dock while your iPadOS or macOS app is in full-screen mode.** In iPadOS and macOS, it’s important to preserve access to the Dock so people can quickly open other apps and Dock items. To help prevent people from accidentally revealing the Dock while they’re playing your full-screen game, you can ask iPadOS to ignore an initial swipe up from the screen’s bottom edge or hide the Dock entirely in macOS. For developer guidance, see [preferredScreenEdgesDeferringSystemGestures](https://developer.apple.com/documentation/swiftui/uihostingcontroller/preferredscreenedgesdeferringsystemgestures) (SwiftUI), [preferredScreenEdgesDeferringSystemGestures](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredscreenedgesdeferringsystemgestures) (UIKit) and [hideDock](https://developer.apple.com/documentation/appkit/nsapplication/presentationoptions-swift.struct/hidedock) (AppKit).

**After people switch away from your full-screen experience, help them resume where they left off when they return.** For example, a game or a slideshow needs to pause automatically when people leave the experience so they don’t miss anything.

**Let people choose when to exit full-screen mode.** People generally don’t expect full-screen mode to end automatically when they switch to a different experience or finish an absorbing activity, like playing a game or viewing a movie.

**Prioritize content by temporarily hiding toolbars and navigation controls.** You can offer a distraction-free environment by hiding elements when content is the primary focus, such as when viewing full-screen photos or reading a document. If you implement such behavior, let people restore the hidden elements with a familiar gesture or action like tapping, swiping down, or moving the cursor to the top of the screen. Be sure to keep controls visible when they’re essential for navigation or performing tasks. Although a visionOS window can hide its toolbars or navigation controls, people generally expect different types of immersive experiences while wearing Apple Vision Pro; for guidance, see Immersive experiences.

## Platform considerations

*Not supported in tvOS, visionOS, or watchOS.*

### Mobile (iOS, iPadOS)

**Consider deferring system gestures to prevent accidental exits in a full-screen app or game.** By default, the Home Screen indicator automatically hides shortly after someone switches to your app or game. It reappears when someone interacts with the bottom portion of the screen, allowing them to swipe once to exit. Whenever possible, retain this behavior because it’s familiar and what people expect. If supporting this results in unexpected exits, you can enable two swipes rather than one to exit. For developer guidance, see [preferredScreenEdgesDeferringSystemGestures](https://developer.apple.com/documentation/swiftui/uihostingcontroller/preferredscreenedgesdeferringsystemgestures).

### Desktop (macOS)

**Use the system-provided full-screen experience.** Using the system’s full-screen support ensures that your full-screen window works well in all contexts. For example, some Mac models include a camera housing that occupies an area at the top-center of the screen. Using the system’s full-screen support automatically accommodates this area. For developer guidance, see [toggleFullScreen(_:)](https://developer.apple.com/documentation/appkit/nswindow/togglefullscreen(_:)).

**In a game, don’t change the display mode when players go full screen.** People expect to be in control of their display mode, and changing it automatically doesn’t improve performance.

For additional developer guidance, see [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/metal/managing-your-game-window-for-metal-in-macos).

**Always let people choose when to enter full-screen mode.** Prefer letting people use your window’s Enter Full Screen button, View menu item, or the Control-Command-F keyboard shortcut. Avoid offering a custom menu of window modes. In a game, you might also provide a custom [toggle](toggles.md) that turns full-screen mode on and off.

## Change log

| Date | Changes |
| --- | --- |
| June 9, 2025 | Updated guidance for hiding toolbars and navigation controls, and deferring Home Screen indicator gestures in full-screen iOS and iPadOS apps and games. |
| June 10, 2024 | Enhanced guidance for playing a game in full-screen mode. |

## Related guidelines

- [Layout](layout.md)
- [Multitasking](multitasking.md)
- [Windows](windows.md)
- [The menu bar](the-menu-bar.md)

---


<a id="launching"></a>
## launching

# Launching

> Source: <https://developer.apple.com/design/human-interface-guidelines/launching>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2024-06-10 (Added guidance on displaying a splash screen.)

A streamlined launch experience helps people start using your app or game immediately.

---

Launching begins when someone opens your app or game, includes an initial download, and ends when the first screen is ready. After launching completes, you might offer an [onboarding](onboarding.md) experience, which can give people a high-level view of your app or game.

## Best practices

**Launch instantly.** People want to start interacting with your app or game right away, and sometimes they don’t want to wait more than a couple of seconds.

**If the platform requires it, provide a launch screen.** In iOS, iPadOS, and tvOS, the system displays your launch screen the moment your app or game starts and quickly replaces it with your first screen, giving people the impression that your experience is fast and responsive. For guidance, see [Launch screens](#launch-screens). macOS, visionOS, and watchOS don’t require launch screens.

**If you need a splash screen, consider displaying it at the beginning of your onboarding flow.** A splash screen is a beautiful graphic that succinctly communicates branding and other information you need to provide. If you don’t provide an onboarding experience, you might display your splash screen as soon as launching completes.

**Restore the previous state when your app restarts so people can continue where they left off.** Avoid making people retrace steps to reach their previous location in your app or game. Restore granular details of the previous state as much as possible. For example, scroll the view to people’s most recent position, and display windows in the same state and location in which people left them.

## Launch screens

*Not applicable for macOS, visionOS, or watchOS.*

**Downplay the launch experience.** A launch screen isn’t part of an onboarding experience or a splash screen, and it isn’t an opportunity for artistic expression. A launch screen’s sole function is to enhance the perception of your experience as quick to launch and immediately ready to use.

**Design a launch screen that’s nearly identical to the first screen of your app or game.** If you include elements that look different when launching completes, people may experience an unpleasant flash between the launch screen and your first screen. If your app or game displays a solid color before transitioning to the first screen, create a launch screen that displays only that solid color. Also make sure that your launch screen matches the device’s current orientation and appearance mode.

**Avoid including text on your launch screen, even if your first screen displays text.** Because the content in a launch screen doesn’t change, any text you display won’t be localized.

**Don’t advertise.** The launch screen isn’t a branding opportunity. Avoid creating a screen that looks like a splash screen or an “About” window, and don’t include logos or other branding elements unless they’re a fixed part of your app’s first screen.

## Platform considerations

*No additional considerations for macOS or watchOS.*

### Mobile (iOS, iPadOS)

**Launch in the appropriate orientation.** If your app or game supports both portrait and landscape modes, launch using the device’s current orientation. If your interface only runs in one orientation, launch in that orientation and let people rotate the device if necessary. Ensure a landscape-only interface responds correctly, regardless of whether people enter landscape orientation by rotating the device left or right. For guidance, see [Layout](layout.md).

## Change log

| Date | Changes |
| --- | --- |
| June 10, 2024 | Added guidance on displaying a splash screen. |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [Onboarding](onboarding.md)
- [Loading](loading.md)

---


<a id="live-viewing-apps"></a>
## live-viewing-apps

# Live-viewing apps

> Source: <https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)

As you design a live-viewing app, prioritize the content and create fun, fluid interactions that encourage immersion in the live-viewing experience.

---

Live-viewing apps need to elevate and prioritize live content. In every screen, draw people’s attention to live content and make sure they can distinguish it from video-on-demand (VOD) content at a glance.

## Best practices

**Feature live content prominently and make it easy to access.** People come to your app to watch content, so you want to minimize the interval between starting your app and playing content. When live content is in the first tab, people don’t have to tap more than once to start viewing it.

**Let people tap once — or not at all — to start playback.** For example, you might display a Watch Now button on top of featured or recently viewed live content. When people tap this button, it immediately disappears and playback begins, replacing your app’s UI with a full-screen, immersive viewing experience.

**Make sure live content looks live.** People need to be able to distinguish live content from VOD content. Although simply playing live content is the best way to make it feel live, you can also help people recognize live content by marking it in some way. For example, you might display other channels in a collection row titled “Live” and give each item a visual indicator — such as a badge, symbol, or sash — that identifies it as live.

**Consider indicating the progress of currently playing live content.** People appreciate knowing where they’ll land when they jump into in-progress live content. You can use a progress bar or other indicator to show people how much content remains.

**Give people additional actions and viewing alternatives.** In addition to playback, which always needs to be the primary action, make it easy for people to record, restart, download, and perform other actions that you support. Display these actions in the same order throughout your app — for example, Watch, Start Over, Record, and Favorite. Also, if the currently playing content is playing again at other times, show this information so that people can schedule their viewing.

**Consider using a content footer for browsing channels during playback.** A content footer lets people browse without taking them out of the live playback experience. If you decide to use a content footer, be sure to:

- Give it a subtle treatment, such as a darkening, to keep text legible and help all items remain visually distinct from the content playing behind it.
- Make it easy for people to identify the thumbnail that represents the currently playing content by, for example, badging the thumbnail or tinting its progress bar.
- Match the categories in the content footer to those in your electronic program guide (for related guidance, see [EPG experience](#epg-experience)).
- Design a simple, predictable way for people to invoke and dismiss the content footer — for example, if swiping up invokes the footer, people would expect swiping down to dismiss it.

**Provide instant visual feedback when people change channels.** This is essential for two reasons: people need confirmation that they’ve arrived at the channel they want, and providing feedback can give the streaming content some time to load.

**Match audio to the current context.** When people start playing live content, they expect the audio to match even if they switch to browsing while the content plays in the background. However, when people navigate away from the live tab in your app, they leave the live-viewing context, so audio needs to stop.

## EPG experience

Live-viewing apps typically provide an electronic program guide (EPG) that contains information about scheduled programming. Follow these guidelines to give people a streamlined EPG experience that feels designed specifically for your live-viewing app.

**Prominently display current information and make it easy to return to playback.** When people first open the EPG, the current program, channel, and time needs to be easy to spot so they can instantly return to the current channel.

**Make browsing the EPG effortless.** A typical EPG contains a lot of information, so it’s important to help people page, scroll, or jump through it easily. Also consider providing a My Channels group or a Favorites group that gives people quick access to the content they view most often.

**Group content into familiar categories to help people find it more easily.** For example, you might use categories like Movies, TV Shows, Kids, Sports, and Popular. If your app includes a content footer, organize content thumbnails using the same categories as in the EPG.

**Let people browse the EPG without leaving their current content.** For example, you can continue playing content in a picture-in-picture (PiP) mode or in the background while people browse the EPG.

## Cloud DVR

If you support digital video recording (DVR) in the cloud, follow these guidelines to provide a great recording experience in your live-viewing app.

**Let people start and stop recording from the info panel.** While live-streaming, people want to reveal the info panel to start recording immediately.

**Let people record a future program in a view that provides details about the content.** Also, give people the option to record only that program or all future episodes.

**Help people adapt the recording experience to their needs.** Let people specify precisely what they want to record, such as only the current episode, only new episodes, or only games that involve specific teams.

**Allow playback and other content-specific actions within your cloud DVR area.** When people open a view that displays content details in your cloud DVR section, let them play or delete content and, if applicable, adjust recording settings.

**Consider offering a control that lets people manage cloud DVR settings.** For example, you might let people delete recordings they’ve already watched or content that’s older than a certain number of days. Ideally, help people avoid running out of space by letting them set up automatic storage management, which overwrites the oldest or already viewed content.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Related guidelines

- [Playing video](playing-video.md)

---


<a id="loading"></a>
## loading

# Loading

> Source: <https://developer.apple.com/design/human-interface-guidelines/loading>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-06-09 (Revised guidance for storing downloads to reflect downloading large assets in the background.)

The best content-loading experience finishes before people become aware of it.

---

If your app or game loads assets, levels, or other content, design the behavior so it doesn’t disrupt or negatively impact the user experience.

## Best practices

**Show something as soon as possible.** If you make people wait for loading to complete before displaying anything, they can interpret the lack of content as a problem with your app or game. Instead, consider showing placeholder text, graphics, or animations as content loads, replacing these elements as content becomes available.

**Let people do other things in your app or game while they wait for content to load.** Loading content in the background helps give people access to other actions. For example, a game could load content in the background while players learn about the next level or view an in-game menu. For developer guidance, see [Improving the player experience for games with large downloads](https://developer.apple.com/documentation/gamekit/improving-the-player-experience-for-games-with-large-downloads).

**If loading takes an unavoidably long time, give people something interesting to view while they wait.** For example, you might provide gameplay hints, display tips, or introduce people to new features. Gauge the remaining loading time as accurately as possible to help you avoid giving people too little time to enjoy your placeholder content or having so much time that you need to repeat it.

**Improve installation and launch time by downloading large assets in the background.** Consider using the [Background Assets](https://developer.apple.com/documentation/backgroundassets) framework to schedule asset downloads — like game level packs, 3D character models, and textures — to occur immediately after installation, during updates, or at other nondisruptive times.

## Showing progress

**Clearly communicate that content is loading and how long it might take to complete.** Ideally, content displays instantly, but for situations where loading takes more than a moment or two, you can use system-provided components — called *progress indicators* — to show that loading is ongoing. In general, you use a *determinate* progress indicator when you know how long loading will take, and you use an *indeterminate* progress indicator when you don’t. For guidance, see [Progress indicators](progress-indicators.md).

**For games, consider creating a custom loading view.** Standard progress indicators work well in most apps, but can sometimes feel out of place in a game. Consider designing a more engaging experience by using custom animations and elements that match the style of your game.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.*

## Change log

| Date | Changes |
| --- | --- |
| June 9, 2025 | Revised guidance for storing downloads to reflect downloading large assets in the background. |
| June 10, 2024 | Added guidelines for showing progress and storing downloads, and enhanced guidance for games. |

## Related guidelines

- [Launching](launching.md)
- [Progress indicators](progress-indicators.md)

---


<a id="managing-accounts"></a>
## managing-accounts

# Managing accounts

> Source: <https://developer.apple.com/design/human-interface-guidelines/managing-accounts>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)

When it doesn’t create an unnecessary barrier to your experience, an account can be a convenient way for people to access their content and track personal details.

---

Ask people to create an account only if your core functionality requires it; otherwise, let people enjoy your app or game without one. If you require an account, consider using [Sign in with Apple](sign-in-with-apple.md) to give people a consistent sign-in experience they can trust and the convenience of not having to remember multiple accounts and authentication methods.

## Best practices

**Explain the benefits of creating an account and how to sign up.** If your app or game requires an account, write a brief, friendly description of the reasons for the requirement and its benefits. Display this message in your sign-in view.

**Delay sign-in for as long as possible.** People often abandon apps when they’re forced to sign in before they can do anything useful. To help avoid this situation, give people a chance to get a sense of what your app or game does before asking them to make a commitment to it. For example, a shopping app might let people browse as much as they want, requiring sign-in only when they’re ready to make a purchase.

**If you don’t use Sign in with Apple in your iOS, iPadOS, macOS, or visionOS app, prefer using a passkey.** Passkeys simplify account creation and authentication, eliminating the need for people to create or enter passwords. When an app supports passkeys, people simply provide their user name when creating a new account or signing in to an existing one. For developer guidance, see [Supporting passkeys](https://developer.apple.com/documentation/authenticationservices/supporting-passkeys). If you need to continue using passwords for authentication, augment security by requiring two-factor authentication (for developer guidance, see [Securing Logins with iCloud Keychain Verification Codes](https://developer.apple.com/documentation/authenticationservices/securing-logins-with-icloud-keychain-verification-codes)).

**Always identify the authentication method you offer.** For example, if you display a button for signing in to your app with Face ID, title it using a phrase like “Sign In with Face ID” instead of a generic phrase like “Sign In.”

**Refer only to authentication methods that are available in the current context.** For example, don’t reference Face ID on a device that doesn’t offer it. Check the device’s capabilities and use the appropriate terminology. For developer guidance, see [LABiometryType](https://developer.apple.com/documentation/localauthentication/labiometrytype).

**In general, avoid offering an app-specific setting for opting in to biometric authentication.** People turn on biometric authentication at the system level, so presenting an in-app setting is redundant and could be confusing.

**Avoid using the term *passcode* to refer to account authentication.** People create a passcode to unlock their device or authenticate for Apple services. If you use the term in your interface, people might think you’re asking them to reuse their passcode in your app or game.

## Deleting accounts

If you help people create an account within your app or game, you must also help them delete it, not just deactivate it. In addition to following the guidelines below, be sure to understand and comply with your region’s legal requirements related to account deletion and the right to be forgotten.

> **Important:** If legal requirements compel your app to maintain accounts or information — such as digital health records — or to follow a specific account-deletion process, clearly describe the situation so people can understand the information or accounts you must maintain and the process you must follow.

**Provide a clear way to initiate account deletion within your app or game.** If people can’t perform account deletion within your app, you must provide a direct link to the webpage on which people can do so. Make the link easy to discover — for example, don’t bury it in your Privacy Policy or Terms of Service pages.

> **Developer note:** If people used [Sign in with Apple](sign-in-with-apple.md) to create an account within your app, you revoke the associated tokens when they delete their account. See [Token revocation](https://developer.apple.com/documentation/signinwithapplerestapi/revoke-tokens).

**Provide a consistent account-deletion experience whether people perform it within your app or game or on the website.** For example, avoid making one version of the deletion flow longer or more complicated than the other.

**Consider letting people schedule account deletion to occur in the future.** People can appreciate the opportunity to use their remaining services or wait until their subscription auto-renews before deleting their account. If you offer a way to schedule account deletion, offer an option for immediate deletion as well.

**Tell people when account deletion will complete, and notify them when it’s finished.** Because it can sometimes take a while to fully delete an account, it’s essential to keep people informed about the status of the deletion process so they know what to expect.

**If you support in-app purchases, help people understand how billing and cancellation work when they delete their account.** For example, you might need to help people understand the following scenarios:

- Billing for an auto-renewable subscription continues through Apple until people cancel the subscription, regardless of whether they delete their account.
- After they delete their account, people need to cancel their subscription or request a refund.

In addition to helping people understand these scenarios, provide information that describes how to cancel subscriptions and manage purchases. For guidance, see [Helping people manage their subscriptions](apple-in-app-purchase.md#helping-people-manage-their-subscriptions) and [Providing help](apple-in-app-purchase.md#providing-help).

> **Note:** Even if people didn’t use your app to purchase the subscription, you still need to support account deletion.

## TV provider accounts

Many popular TV providers let people sign in to their accounts at the system level, eliminating the need to authenticate on an app-by-app basis. If your TV provider app requires people to sign in, use TV Provider Authentication to provide the most efficient onboarding experience.

**Avoid displaying a sign-out option when people are signed in at the system level.** If your app must include a sign-out option, invoking it needs to prompt people to navigate to Settings > TV Provider to sign out of their account.

**Never instruct people to sign out by adjusting privacy controls.** The TV provider controls in Settings > Privacy aren’t a sign-out mechanism. These settings help people manage the apps that can access their TV provider account.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, or visionOS.*

## Related guidelines

- [Onboarding](onboarding.md)
- [Sign in with Apple](sign-in-with-apple.md)

---


<a id="managing-notifications"></a>
## managing-notifications

# Managing notifications

> Source: <https://developer.apple.com/design/human-interface-guidelines/managing-notifications>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)

Notifications can give people timely and important information, whether the device is locked or in use.

---

You need to get permission before sending any notification. The system lets people change this decision in settings, where they can also silence all notifications (except for government alerts in some locales).

## Integrating with Focus

People appreciate receiving a notification for something they care about, but they don’t always appreciate being interrupted. To help people manage the experience, the system lets them specify delivery times and set up a Focus.

- A Focus helps people filter notifications during a time period they reserve for an activity like sleeping, working, reading, or driving.
- Delivery scheduling lets people choose whether to receive notification alerts immediately or in a summary that’s delivered at times they choose.

People identify the contacts and apps that can break through a Focus to deliver notification alerts. In a Work Focus, for example, people might want to receive alerts from work colleagues, family members, and work-related apps as soon as notifications arrive. People might also want to receive all Time Sensitive notification alerts during a Focus. A *Time Sensitive* notification contains essential information people appreciate getting right away.

> **Important:** Even though a Focus might delay the delivery of a notification alert, the notification itself is available as soon as it arrives.

To support these behavior customizations, you first identify the types of notifications your app or game can send. If you support direct communications — like phone calls and messages — you use *communication* notifications; for all other types of tasks, you use *noncommunication* notifications. To support communication notifications, you adopt SiriKit intents, which means people can use Siri to customize notification behaviors; for developer guidance, see [INSendMessageIntent](https://developer.apple.com/documentation/intents/insendmessageintent) and [UNNotificationContentProviding](https://developer.apple.com/documentation/usernotifications/unnotificationcontentproviding).

You need to specify a system-defined interruption level for each noncommunication notification you send. The system uses the interruption level to help determine when to deliver the alert; when a communication notification arrives, the system uses the sender to determine when to deliver the alert.

The system defines four interruption levels for noncommunication notifications:

- *Passive*. Information people can view at their leisure, like a restaurant recommendation.
- *Active* (the default). Information people might appreciate knowing about when it arrives, like a score update on their favorite sports team.
- *Time Sensitive*. Information that directly impacts the person and requires their immediate attention, like an account security issue or a package delivery.
- *Critical*. Urgent information about health and safety that directly impacts the person and demands their immediate attention. Critical notifications are extremely rare and typically come from governmental and public agencies or apps that help people manage their health or home.

Notification alerts in each system-defined interruption level can behave in the following ways:

| Interruption level | Overrides scheduled delivery | Breaks through Focus | Overrides Ring/Silent switch on iPhone and iPad |
| --- | --- | --- | --- |
| Passive | No | No | No |
| Active | No | No | No |
| Time Sensitive | Yes | Yes | No |
| Critical | Yes | Yes | Yes |

> **Note:** Because a Critical notification can override the Ring/Silent switch and break through scheduled delivery and Focus, you must get an entitlement to send one.

## Best practices

**Build trust by accurately representing the urgency of each notification.** People have several ways to adjust how they receive your notifications — including turning off all notifications — so it’s essential to be as realistic as possible when assigning an interruption level. You don’t want people to feel that a notification uses a high level of urgency to interrupt them with low-priority information.

**Use the Time Sensitive interruption level only for notifications that are relevant in the moment.** To help people understand the benefits of letting Time Sensitive notifications break through a Focus or scheduled delivery, make sure the notification is about an event that’s happening now or will happen within an hour. The first time a Time Sensitive notification arrives from your app, the system describes how such a notification works and gives people a way to turn it off if they don’t agree that the information requires their immediate attention. Going forward, the system periodically gives people additional opportunities to evaluate how your Time Sensitive notification is working for them. For developer guidance, see [UNNotificationInterruptionLevel](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel).

## Sending marketing notifications

Don’t use notifications to send marketing or promotional content unless people explicitly agree to receive such information. When people want to learn about new features, content, or events related to your app or game, they can grant their permission to receive marketing notifications. For example, people who use a subscription app might appreciate getting an offer to become a subscriber, and game players might want to receive a special offer related to a live game event.

**Never use the Time Sensitive interruption level to send a marketing notification.** People may have agreed to receive marketing notifications from your app, but such a notification must never break through a Focus or scheduled delivery setting.

**Get people’s permission if you want to send them promotional or marketing notifications.** Before you send these notifications to people, you must receive their explicit permission to do so. Create an alert, modal view, or other interface that describes the types of information you want to send and gives people a clear way to opt in or out.

**Make sure people can manage their notification settings within your app.** In addition to requesting permission to send informational or marketing notifications, you must also provide an in-app settings screen that lets people change their choice. For guidance, see [Settings](settings.md).

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.*

## Related guidelines

- [Privacy](privacy.md)

---


<a id="modality"></a>
## modality

# Modality

> Source: <https://developer.apple.com/design/human-interface-guidelines/modality>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2023-12-05 (Enhanced guidance for in-depth modal experiences and clarified guidance on multiple modal views.)

Modality is a design technique that presents content in a separate, dedicated mode that prevents interaction with the parent view and requires an explicit action to dismiss.

---

Presenting content modally can:

- Ensure that people receive critical information and, if necessary, act on it
- Provide options that let people confirm or modify their most recent action
- Help people perform a distinct, narrowly scoped task without losing track of their previous context
- Give people an immersive experience or help them concentrate on a complex task

Depending on the platform, you might use different components to present these types of modal experiences. For example, all platforms can present an *alert*, which is a modal view that delivers important information related to your app or game. In addition, each platform may define various types of modal views for presenting context-specific options, such as *activity views,* *sheets*, and *confirmation dialogs* or *action sheets*. To help people perform a distinct task, iOS, iPadOS, and macOS apps tend to use sheets or popovers, but iPadOS, macOS, and visionOS apps might also just use a separate window.

To provide a temporary experience, like viewing media, or to help people perform a distinct, multistep task, like editing content, apps can offer a full-screen modal experience. In contrast, apps may also offer nonmodal types of full-screen experiences; for guidance, see [Going full screen](going-full-screen.md). visionOS apps can offer a range of immersive experiences; for guidance, see Immersive experiences.

## Best practices

**Present content modally only when there’s a clear benefit.** A modal experience takes people out of their current context and requires an action to dismiss, so it’s important to use modality only when it helps people focus or make choices that affect their content or device.

**Aim to keep modal tasks simple, short, and streamlined.** If a modal task is too complicated, people can lose track of the task they suspended when they entered the modal view, especially if the modal view obscures their previous context.

**Take care to avoid creating a modal experience that feels like an app within your app.** In particular, presenting a hierarchy of views within a modal task can make people forget how to retrace their steps. If a modal task must contain subviews, provide a single path through the hierarchy and avoid including buttons that people might mistake for the button that dismisses the modal view.

**Consider using a full-screen modal style for in-depth content or a complex task.** A modal experience that fills a window or the device display minimizes distractions, so it can work well for presenting videos, photos, or camera views, or to support a multistep task like marking up a document or editing a photo. When a visionOS app runs alongside other apps in the Shared Space, a full-screen modal presentation fills a window; if people transition the app to a Full Space, the full-screen modal presentation can become a more immersive experience.

**Always give people an obvious way to dismiss a modal view.** In general, it works well to follow the platform conventions people already know. For example, in iOS, iPadOS, and watchOS apps, people typically expect to find a button in the top toolbar or swipe down; in macOS and tvOS apps, people expect to find a button in the main content view.

**When necessary, help people avoid data loss by getting confirmation before closing a modal view.** Regardless of whether people use a dismiss gesture or a button, if closing the view could result in the loss of user-generated content, be sure to explain the situation and give people ways to resolve it. For example, in iOS, you might present an action sheet that includes a save option.

**Make it easy to identify a modal view’s task.** When people enter a modal view, they switch away from their previous context and might not return to it right away. When you provide a title that names the modal view’s task — or additional text that describes the task or provides guidance — you can help people keep their place in your app.

**Let people dismiss a modal view before presenting another one.** Allowing multiple modal views to be visible at the same time tends to create visual clutter and can make your app seem scattered and disorganized. People need to remember the context they were in before a modal view appears, so presenting multiple views adds to people’s cognitive load, especially when a modal view hides another one by appearing on top of it. Although an alert can appear on top of all other content — including other modal views — you never want to display more than one alert at the same time.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| December 5, 2023 | Enhanced guidance for in-depth modal experiences and clarified guidance on multiple modal views. |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [Sheets](sheets.md)
- [Alerts](alerts.md)
- [Popovers](popovers.md)
- [Action sheets](action-sheets.md)
- [Activity views](activity-views.md)

---


<a id="multitasking"></a>
## multitasking

# Multitasking

> Source: <https://developer.apple.com/design/human-interface-guidelines/multitasking>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS omitted)
> Last change on Apple's site: 2025-06-09 (Reorganized guidance in platform considerations, and added guidance for multitasking with multiple windows in iPadOS.)

Multitasking lets people switch quickly from one app to another, performing tasks in each.

---

People expect to use multitasking on their devices, and they may think something is wrong if your app doesn’t allow it. With rare exceptions — such as some games, and Apple Vision Pro apps running in a Full Space — every app needs to work well with multitasking.

In addition to app switching, multitasking can present different experiences on different devices; see [Platform considerations](#platform-considerations).

## Best practices

A great multitasking experience helps people accomplish tasks in multiple apps by managing content in a variety of simultaneous contexts. Because you don’t know when people will initiate multitasking, your app or game always needs to be prepared to save and restore their context.

**Pause activities that require people’s attention or active participation when they switch away.** If your app is a game or a media-viewing app, for example, make sure people don’t miss anything when they switch to another app. When they switch back, let them continue as if they never left.

**Respond smoothly to audio interruptions.** Occasionally, audio from another app or the system itself may interrupt your app’s audio. For example, an incoming phone call or a music playlist initiated by Siri might interrupt your app’s audio. When situations like these occur, people expect your app to respond in the following ways:

- Pause audio indefinitely for primary audio interruptions, such as playing music, podcasts, or audiobooks.
- Temporarily lower the volume or pause the audio for shorter interruptions, such as GPS directional notifications, and resume the original volume or playback when the interruption ends.

For guidance, see [Playing audio](playing-audio.md).

**Finish user-initiated tasks in the background.** When someone starts a task like downloading assets or processing a video file, they expect it to finish even if they switch away from your app. If your app is in the middle of performing a task that doesn’t need additional input, complete it in the background before suspending.

**Use notifications sparingly.** Your app can send notifications when it’s suspended or running in the background. If people start an important or time-sensitive task in your app, and then switch away from it, they might appreciate receiving a notification when the task completes so they can switch back to your app and take the next step. In contrast, people don’t generally need to know the moment a routine or secondary task completes. In this scenario, avoid sending an unnecessary notification; instead, let people check on the task when they return to your app. For guidance, see [Managing notifications](managing-notifications.md).

## Platform considerations

*Not supported in watchOS.*

### Phone (iOS)

On iPhone, multitasking lets people use FaceTime or watch a video in Picture in Picture while they also use a different app.

### Tablet (iPadOS)

On iPad, people can view and interact with the [windows](windows.md) of several different apps at the same time. An individual app can also support multiple open windows, which lets people view and interact with more than one window in the same app at one time.

People can use iPad with either full-screen or windowed apps. When full screen, apps occupy the full screen, and people can switch between individual app windows using the app switcher.

When using windowed apps, app windows are resizable, and people can arrange them to suit their needs with behavior similar to macOS. The system provides window controls for common tiling configurations, entering full screen, minimizing, and closing windows. The system identifies the frontmost window by coloring its window controls and casting a drop shadow on windows behind it. For guidance, see [Windows > iPadOS](windows.md#tablet-ipados).

Additionally, videos and FaceTime calls can also play in a Picture in Picture overlay above other content regardless of whether apps are full screen or windowed.

> **Note:** Apps don’t control multitasking configurations or receive any indication of the ones that people choose.

To help your app respond correctly when people open it while windowed, make sure it adapts gracefully to different screen sizes. For guidance, see [Layout](layout.md) and [Windows](windows.md); for developer guidance, see [Multitasking on iPad, Mac, and Apple Vision Pro](https://developer.apple.com/documentation/uikit/multitasking-on-ipad-mac-and-apple-vision-pro). To learn more about how people use iPad multitasking features, see [Use multitasking on your iPad](https://support.apple.com/en-us/HT207582).

### Desktop (macOS)

On Mac, multitasking is the default experience because people typically run more than one app at a time, switching between windows and tasks as they work. When multiple app windows are open, macOS applies drop shadows that make the windows appear layered on the desktop, and applies other visual effects to help people distinguish different window states; for guidance, see [macOS window states](windows.md#macos-window-states).

## Change log

| Date | Changes |
| --- | --- |
| June 9, 2025 | Reorganized guidance in platform considerations, and added guidance for multitasking with multiple windows in iPadOS. |
| December 5, 2023 | Added artwork for primary and auxiliary windows in iPadOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [Layout](layout.md)
- [Windows](windows.md)
- [Playing video](playing-video.md)

---


<a id="offering-help"></a>
## offering-help

# Offering help

> Source: <https://developer.apple.com/design/human-interface-guidelines/offering-help>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2023-12-05 (Included visionOS in guidance for creating tooltips.)

Although the most effective experiences are approachable and intuitive, you can provide contextual help when necessary.

---

## Best practices

**Let your app’s tasks inform the types of help people might need.** For example, you might help people perform simple, one- or two-step tasks by displaying an inline view that succinctly describes the task. In contrast, if your app or game supports complex or multistep tasks you might want to provide a tutorial that teaches people how to accomplish larger goals. In general, directly relate the help you provide to the precise action or task people are doing right now and make it easy for people to dismiss or avoid the help if they don’t need it.

**Use relevant and consistent language and images in your help content.** Always make sure guidance is appropriate for the current context. For example, if someone’s using the Siri Remote with your tvOS experience, don’t show tips or images that feature a game controller. Also be sure the terms and descriptions you use are consistent with the platform. For example, don’t write copy that tells people to click a button on an iPhone or tap a menu item on a Mac.

**Make sure all help content is inclusive.** For guidance, see [Inclusion](inclusion.md).

**Avoid bloating your help content by explaining how standard components or patterns work.** Instead, describe the specific action or task that a standard element performs in your app or game. If your experience introduces a unique control or expects people to use an input device in a nonstandard way — such as holding the Siri Remote rotated 90 degrees — orient people quickly, preferring animation or graphics to educate instead of a lengthy description.

## Creating tips

A tip is a small, transient view that briefly describes how to use a feature in your app. Tips are a great way to teach people about new or less obvious features in your app, or help them discover faster ways to accomplish a task. For developer guidance, see [TipKit](https://developer.apple.com/documentation/TipKit).

**Use the most appropriate tip type for your app’s user interface.** Display a popover tip when you want to preserve the content flow, or an inline tip when you want to ensure that surrounding information is visible. You can use an annotation-style inline tip when pointing to a specific UI element, or a hint-style tip when it’s not related to a specific piece of UI.

**Use tips for simple features.** Tips work best on features that are easy to describe and that people can complete with a few simple steps. If a feature requires more than three actions, it’s probably too complicated for a tip.

**Make tips short, actionable, and engaging.** A tip’s goal is to encourage people to try new features. Use direct, action-oriented language to describe what the feature does and explain how to use it. Keep your tips to one or two sentences and avoid including content that’s promotional or related to a different feature or user flow. Promotional content is anything that advertises, sells, or isn’t aligned with the current context of what the person is doing.

**Define rules to help ensure your tips reach the intended audience.** Not everyone benefits from every tip. For example, people who’ve already used a feature won’t appreciate viewing a tip that describes it. Use parameter-based or event-based eligibility rules to control when a tip appears, and only display a tip if someone might benefit from its use. When your app has more than one tip, set the display frequency so tips display at a reasonable cadence — for example, once every 24 hours.

**If there’s an image or symbol that people associate with the feature, consider including it in the tip, and prefer the filled variant.** For example, a tip with a star can help people understand that the tip is related to favorites.

If the feature is represented by an image that the tip connects to directly, avoid repeating the same image in both the tip and the UI.

**Use buttons to direct people to information or options.** If your feature has settings people can customize, or you want to redirect people to an area where they can learn more about a feature, consider adding a button. Buttons can take people directly to the settings where they make adjustments. Or if there’s more information people might find useful, add a button to take them to additional resources, such as a setup flow.

## Platform considerations

*No additional considerations for iOS, iPadOS, tvOS, or watchOS.*

### Desktop (macOS, visionOS)

A *tooltip* (called a *help tag* in user documentation) displays a small, transient view that briefly describes how to use a component in the interface. In apps that run on a Mac — including iPhone and iPad apps — tooltips can appear when a person holds the pointer over an element; in visionOS apps, a tooltip can appear when a person looks at an element or holds the pointer over it. For developer guidance, see [help(_:)](https://developer.apple.com/documentation/swiftui/view/help(_:)-6oiyb).

**Describe only the control that people indicate interest in.** When people want to know how to use a specific control, they don’t want to learn how to use nearby controls or how to perform a larger task.

**Explain the action or task the control initiates.** It often works well to begin the description with a verb — for example, “Restore default settings” or “Add or remove a language from the list.”

**In general, avoid repeating a control’s name in its tooltip.** Repeating the name takes up space in the tooltip and rarely adds value to the description.

**Be brief.** As much as possible, limit tooltip content to a maximum of 60 to 75 characters (note that localization often changes the length of text). To make a description brief and direct, consider using a sentence fragment and omitting articles. If you need a lot of text to describe a control, consider simplifying your interface design.

**Use sentence case.** Sentence case tends to appear more casual and approachable. If you write complete sentences, omit ending punctuation unless it’s required to be consistent with your app’s style.

**Consider offering context-sensitive tooltips.** For example, you could provide different text for a control’s different states.

## Change log

| Date | Changes |
| --- | --- |
| December 5, 2023 | Included visionOS in guidance for creating tooltips. |
| September 12, 2023 | Added guidance for creating tips. |

## Related guidelines

- [Onboarding](onboarding.md)
- [Feedback](feedback.md)
- [Writing](writing.md)

---


<a id="onboarding"></a>
## onboarding

# Onboarding

> Source: <https://developer.apple.com/design/human-interface-guidelines/onboarding>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2024-06-10 (Clarified different approaches to onboarding and added a guideline on displaying a splash screen.)

Onboarding can help people get a quick start using your app or game.

---

Ideally, people can understand your app or game simply by experiencing it, but if onboarding is necessary, design a flow that’s fast, fun, and optional. When available, onboarding occurs after [launching](launching.md) is complete — it isn’t part of the launch experience.

## Best practices

**Teach through interactivity.** People tend to grasp and retain information better when they can actually perform the task they’re learning about instead of just viewing instructional material. As much as possible, provide an interactive onboarding experience where people can safely test an action, discover a feature, or try out a game mechanic.

**Consider providing a collection of context-specific tips instead of a single onboarding flow.** Integrating contextually relevant tips into your experience can help people learn about their current task while they make progress in your app or game. A context-specific tip can also help people learn better because it lets them concentrate on a single action or task before encountering new information. When you have instructional content that refers to a specific area of the interface, display these instructions near that area. For developer guidance, see [TipKit](https://developer.apple.com/documentation/tipkit).

**If you need to present a prerequisite onboarding flow, design a brief, enjoyable experience that doesn’t require people to memorize a lot of information.** When onboarding is quick and entertaining, people are more likely to complete it. In contrast, if you try to teach too much, people can feel overwhelmed and may be less likely to remember what they learned.

**If it makes sense to offer a separate tutorial, consider making it optional.** If you let people skip the tutorial when they first launch your app or game, don’t present it again on subsequent launches, but make sure it’s easy for people to find if they want to view it later. For example, you could make the tutorial available in a help, account, or settings area within your app or game.

**Keep onboarding content focused on the experience you provide.** People enter your onboarding flow to learn about your app or game; they don’t need to learn how to use the system or the device.

## Additional content

**Briefly display a splash screen if necessary.** If you need to include a splash screen, design a beautiful graphic that communicates succinctly. Aim to display your splash screen just long enough for people to absorb the information at a glance without feeling that it’s delaying their experience.

**Don’t let large downloads hinder onboarding.** People want to start using your app or game immediately after first launching it, whether they participate in an onboarding flow or skip it. Consider including enough media and other content in your software package to prevent people from having to wait for downloads to complete before they can start interacting with your app or game. For guidance, see [Launching](launching.md).

**Avoid displaying licensing details within your onboarding flow.** Let the App Store display agreements and disclaimers so people can read them before downloading your app or game. If you must include these items within the onboarding flow, integrate them in a balanced way that doesn’t disrupt the experience.

## Additional requests

**Postpone nonessential setup flows or customization steps.** Provide reasonable default settings so most people can immediately start interacting with your app or game without performing additional configuration.

**If your app or game needs access to private data or resources before it can function, consider integrating the permission request into your onboarding flow.** In this scenario, making the request during your onboarding flow gives you the opportunity to show people why your app or game needs their permission and the benefits of granting it. Otherwise, present a permission request when people first access the specific function that relies on private data or resources. For guidance, see [Requesting permission](privacy.md#requesting-permission).

**Prefer letting people experience your app or game before prompting them for ratings or purchases.** People can be more likely to respond positively to such requests when they’ve had a chance to become engaged with your app or game.

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| June 10, 2024 | Clarified different approaches to onboarding and added a guideline on displaying a splash screen. |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [Launching](launching.md)
- [Feedback](feedback.md)
- [Offering help](offering-help.md)

---


<a id="playing-audio"></a>
## playing-audio

# Playing audio

> Source: <https://developer.apple.com/design/human-interface-guidelines/playing-audio>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2023-06-21 (Updated to include guidance for visionOS.)

People expect rich audio experiences that automatically adjust when the context changes on the device.

---

Devices can play audio in a variety of ways, such as through internal or external speakers, headphones, and wirelessly through devices that use Bluetooth or AirPlay. To manipulate sound on their devices people use several types of controls, including volume buttons, the Ring/Silent switch on iPhone, headphone controls, the Control Center volume slider, and sound controls in third-party accessories. Whether sound is a primary part of your experience or an embellishment, you need to make sure it behaves as people expect as they make changes to volume and output.

**Silence.** People switch a device to silent when they want to avoid being interrupted by unexpected sounds like ringtones and incoming message tones. In this scenario, they also want to silence nonessential sounds, such as keyboard clicks, sound effects, game soundtracks, and other audible feedback. When a device is in silent mode, it plays only the audio that people explicitly initiate, like media playback, alarms, and audio/video messaging.

**Volume.** People expect their volume settings to affect all sound in the system — including music and in-app sound effects — regardless of the method they use to adjust the volume. An exception is the ringer volume on iPhone, which people can adjust separately in Settings.

**Headphones.** People use headphones to keep their listening private and in some cases to free their hands. When connecting headphones, people expect sound to reroute automatically without interruption; when disconnecting headphones, they expect playback to pause immediately.

## Best practices

**Adjust levels automatically when necessary — don’t adjust the overall volume.** Your app can adjust relative, independent volume levels to achieve a great mix of audio, but the system volume always governs the final output.

**Permit rerouting of audio when possible.** People often want to select a different audio output device. For example, they may want to listen to music through their living room stereo, car radio, or Apple TV. Support this capability unless there’s a compelling reason not to.

**Use the system-provided volume view to let people make audio adjustments.** The volume view includes a volume-level slider and a control for rerouting audio output. You can customize the appearance of the slider. For developer guidance, see [MPVolumeView](https://developer.apple.com/documentation/mediaplayer/mpvolumeview).

**Choose an audio category that fits the way your app or game uses sound.** Depending on the audio category you choose, your app’s sounds can mix with other audio, play while your app is in the background, or stop when people set the Ring/Silent switch to silent. As much as possible, pick a category that helps your app meet people’s expectations. For example, don’t make people stop listening to music from another app if you don’t need to. For developer guidance, see [AVAudioSession.Category](https://developer.apple.com/documentation/avfaudio/avaudiosession/category-swift.struct).

| Category | Meaning | Behavior |
| --- | --- | --- |
| Solo ambient | Sound isn’t essential, but it silences other audio. For example, a game with a soundtrack. | Responds to the silence switch. Doesn’t mix with other sounds. Doesn’t play in the background. |
| Ambient | Sound isn’t essential, and it doesn’t silence other audio. For example, a game that lets people play music from another app during gameplay in place of the game’s soundtrack. | Responds to the silence switch. Mixes with other sounds. Doesn’t play in the background. |
| Playback | Sound is essential and might mix with other audio. For example, an audiobook or educational app that teaches a foreign language, which people might want to listen to after leaving the app. | Doesn’t respond to the silence switch. May or may not mix with other sounds. Can play in the background. |
| Record | Sound is recorded. For example, a note-taking app that offers an audio recording mode. An app of this nature might switch its category to playback if it lets people play the recorded notes. | Doesn’t respond to the silence switch. Doesn’t mix with other sounds. Can record in the background. |
| Play and record | Sound is recorded and played, potentially simultaneously. For example, an audio messaging or video calling app. | Doesn’t respond to the silence switch. May or may not mix with other sounds. Can record and play in the background. |

**Respond to audio controls only when it makes sense.** People can control audio playback from outside your app’s interface — such as in Control Center or with controls on their headphones — regardless of whether your app is in the foreground or background. If your app is actively playing audio, in a clear audio-related context, or connected to a device that uses Bluetooth or AirPlay, it’s fine to respond to audio controls. Otherwise, when people activate a control, avoid halting audio currently playing from another app.

**Avoid repurposing audio controls.** People expect audio controls to behave consistently in all apps, so it’s essential to avoid redefining the meaning of an audio control in your app. If your app doesn’t support certain controls, don’t respond to them.

**Consider creating custom audio player controls only if you need to offer commands that the system doesn’t support.** For example, you might want to define custom increments for skipping forward or backward, or present content that’s related to the playing audio, such as a sports score.

**Let other apps know when your app finishes playing temporary audio.** If your app can temporarily interrupt the audio of other apps, be sure to flag your audio session in a way that lets other apps know when they can resume. For developer guidance, see [notifyOthersOnDeactivation](https://developer.apple.com/documentation/avfaudio/avaudiosession/setactiveoptions/notifyothersondeactivation).

## Handling interruptions

Although most apps and games rely on the system’s default interruption behavior, you can customize this behavior to better accommodate your needs.

**Determine how to respond to audio-session interruptions.** For example, if your app supports recording or other audio-related tasks that people don’t want interrupted, you can tell the system to avoid interrupting the currently playing audio for an incoming call unless people choose to accept it. Another example is a VoIP app, which must end a call when people close the Smart Folio of their iPad while they’re using the built-in microphone. Closing the Smart Folio automatically mutes the iPad microphone and by default interrupts the audio session associated with it. If a VoIP app restarts the audio session when people reopen their Smart Folio, it risks invading people’s privacy by unmuting the microphone without their knowledge. You can inspect an audio-session interruption to help determine the right way to respond; for developer guidance, see [Handling audio interruptions](https://developer.apple.com/documentation/avfaudio/handling-audio-interruptions).

**When an interruption ends, determine whether to resume audio playback automatically.** Sometimes, audio from a different app can interrupt the audio your app is playing. An interruption can be *resumable*, like an incoming phone call, or *nonresumable*, like when people start a new music playlist. Use the interruption type and your app’s type to decide whether to resume playback automatically. For example, a media playback app that’s actively playing audio when an interruption occurs can check to be sure the type is resumable before continuing playback when the interruption ends. On the other hand, a game doesn’t need to check the interruption type before automatically resuming playback, because a game plays audio without an explicit user choice. For developer guidance, see [shouldResume](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionoptions/shouldresume).

## Platform considerations

### Mobile (iOS, iPadOS)

**Use the system’s sound services to play short sounds and vibrations.** For developer guidance, see [Audio Services](https://developer.apple.com/documentation/audiotoolbox/audio-services).

### Desktop (macOS)

In macOS, notification sounds mix with other audio by default.

## Change log

| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [Playing video](playing-video.md)
- [Feedback](feedback.md)

---


<a id="playing-haptics"></a>
## playing-haptics

# Playing haptics

> Source: <https://developer.apple.com/design/human-interface-guidelines/playing-haptics>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2024-05-07 (Added guidance for playing haptics on Apple Pencil Pro.)

Playing haptics can engage people’s sense of touch and bring their familiarity with the physical world into your app or game.

---

Depending on the platform and the device people are using, the system can play haptics in addition to visual and auditory feedback. For example, components like switches, sliders, and pickers automatically play haptic feedback on supported iPhone models; on Apple Watch, the Taptic Engine generates haptics for a number of built-in feedback patterns, which watchOS combines with an audible tone. On a Mac that’s equipped with a Force Touch trackpad, an app can play haptics while people drag content or when they force click to change the speed of media controls.

In addition to built-in haptic capabilities, some external input devices can also play haptics. For example:

- In an iPadOS, macOS, tvOS, or visionOS app or game, [game controllers](game-controls.md) can provide haptic feedback (for developer guidance, see [Playing Haptics on Game Controllers](https://developer.apple.com/documentation/corehaptics/playing-haptics-on-game-controllers)).
- [Apple Pencil Pro](apple-pencil-and-scribble.md) and some trackpads can provide haptic feedback when connected to certain iPad models. (For details on Apple Pencil features and compatibility, see [Apple Pencil](https://www.apple.com/apple-pencil/).)

## Best practices

**Use system-provided haptic patterns according to their documented meanings.** People recognize standard haptics because the system plays them consistently on interactions with standard controls. If the documented use case for a pattern doesn’t make sense in your app or game, avoid using the pattern to mean something else. Instead, use a generic pattern or create your own, where supported. For guidance, see [Custom haptics](#custom-haptics).

**Use haptics consistently throughout your app or game.** It’s important to build a clear, causal relationship between each haptic and the action that causes it so people learn to associate certain haptic patterns with certain experiences. If a haptic doesn’t reinforce a cause-and-effect relationship, it can be confusing and seem gratuitous. For example, if your game plays a specific haptic pattern when a character fails to finish a mission, people associate that pattern with a negative outcome. If you use the same haptic pattern for a positive outcome like a level completion, people will be confused.

**Prefer using haptics to complement other feedback in your app or game.** When visual, auditory, and tactile feedback are in harmony — as they generally are in the physical world — the user experience is more coherent and can seem more natural. For example, you generally want to match the intensity and sharpness of a haptic with the intensity and sharpness of the animation it accompanies. You can also synchronize sound with haptics; for developer guidance, see [Delivering Rich App Experiences with Haptics](https://developer.apple.com/documentation/corehaptics/delivering-rich-app-experiences-with-haptics).

**Avoid overusing haptics.** Sometimes a haptic can feel just right when it happens occasionally, but become tiresome when it plays frequently. Doing user testing can help you discover a balance that most people appreciate. Often, the best haptic experience is one that people may not be conscious of, but miss when it’s turned off.

**In most apps, prefer playing short haptics that complement discrete events.** Although long-running haptics that accompany a gameplay flow can enhance the experience, long-running haptics in an app can dilute the meaning of the feedback and distract people from their task. On Apple Pencil Pro, for example, continuous or long-lasting haptics don’t tend to clarify the writing or drawing experience and can even make holding the pencil less pleasant.

**Make haptics optional.** Let people turn off or mute haptics, and make sure people can still enjoy your app or game without them.

**Be aware that playing haptics might impact other user experiences.** By design, haptics produce enough physical force for people to feel the vibration. Ensure that haptic vibrations don’t disrupt experiences involving device features like the camera, gyroscope, or microphone.

## Custom haptics

Games often use custom haptics to enhance gameplay. Although it’s less common, nongame apps might also use custom haptics to provide a richer, more delightful experience.

You can design custom haptic patterns that vary dynamically, based on user input or context. For example, the impact players feel when a game character jumps from a tree can be stronger than when the character jumps in place, and substantial experiences — like a collision or a hit — can feel very different from subtle experiences like the approach of footsteps or a looming danger.

There are two basic building blocks you can use to generate custom haptic patterns.

- *Transient* events are brief and compact, often feeling like taps or impulses. The experience of tapping the Flashlight button on the Home Screen is an example of a transient event.
- *Continuous* events feel like sustained vibrations, such as the experience of the lasers effect in a message.

Regardless of the type of haptic event you use to generate a custom haptic, you can also control its *sharpness* and *intensity*. You can think of sharpness as a way to abstract a haptic experience into the waveform that produces the corresponding physical sensations. Specifying sharpness lets you relay to the system your intent for the experience. For example, you might use sharpness values to convey an experience that’s soft, rounded, or organic, or one that’s crisp, precise, or mechanical. As the term implies, intensity means the strength of the haptic.

By combining transient and continuous events, varying sharpness and intensity, and including optional audio content, you can create a wide range of different haptic experiences. For developer guidance, see [Core Haptics](https://developer.apple.com/documentation/corehaptics).

## Platform considerations

### Phone (iOS)

On supported iPhone models, you can add haptics to your experience in the following ways:

- Use standard UI components — like [toggles](toggles.md), [sliders](sliders.md), and [pickers](pickers.md) — that play Apple-designed system haptics by default.
- When it makes sense, use a feedback generator to play one of several predefined haptic patterns in the categories of [notification](#notification), [impact](#impact), and [selection](#selection) (for developer guidance, see [UIFeedbackGenerator](https://developer.apple.com/documentation/uikit/uifeedbackgenerator)).

#### Notification

Notification haptics provide feedback about the outcome of a task or action, such as depositing a check or unlocking a vehicle.

#### Impact

Impact haptics provide a physical metaphor you can use to complement a visual experience. For example, people might feel a tap when a view snaps into place or a thud when two heavy objects collide.

#### Selection

Selection haptics provide feedback while the values of a UI element are changing.

### Desktop (macOS)

When a Magic Trackpad is available, your app can provide one of the three following haptic patterns in response to a drag operation or force click.

| Haptic feedback pattern | Description |
| --- | --- |
| Alignment | Indicates the alignment of a dragged item. For example, this pattern could be used in a drawing app when the people drag a shape into alignment with another shape. Other scenarios where this type of feedback could be used might include scaling an object to fit within specific dimensions, positioning an object at a preferred location, or reaching the beginning/end or minimum/maximum of something like a scrubber in a video app. |
| Level change | Indicates movement between discrete levels of pressure. For example, as people press a fast-forward button on a video player, playback could increase or decrease and haptic feedback could be provided as different levels of pressure are reached. |
| Generic | Intended for providing general feedback when the other patterns don’t apply. |

For developer guidance, see [NSHapticFeedbackPerformer](https://developer.apple.com/documentation/appkit/nshapticfeedbackperformer).

## Change log

| Date | Changes |
| --- | --- |
| May 7, 2024 | Added guidance for playing haptics on Apple Pencil Pro. |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [Feedback](feedback.md)
- [Gestures](gestures.md)

---


<a id="playing-video"></a>
## playing-video

# Playing video

> Source: <https://developer.apple.com/design/human-interface-guidelines/playing-video>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2023-09-12 (Corrected the recommended width for a thumbnail in visionOS.)

People expect to enjoy rich video experiences on their devices, regardless of the app or game they’re using.

---

The system provides video players designed for you to use to embed playback experiences within your app or game in iOS, iPadOS, macOS, tvOS, and visionOS. You can also offer your content through the TV app in these platforms, which gives people a convenient and consistent viewing experience.

The system-provided video players support different aspect-ratio playback modes and in most platforms, Picture in Picture (PiP) viewing mode. Although people can switch modes during playback, by default, the system selects one of the following playback modes based on a video’s aspect ratio:

- In full-screen — or *aspect-fill* — mode, the video scales to fill the display, and some edge cropping may occur. This mode is the default for wide video (2:1 through 2.40:1). For developer guidance, see [resizeAspectFill](https://developer.apple.com/documentation/avfoundation/avlayervideogravity/resizeaspectfill).
- In fit-to-screen — or *aspect* — mode, the entire video is visible onscreen, and letterboxing or pillarboxing occurs as needed. This mode is the default for standard video (4:3, 16:9, and anything up to 2:1) and ultrawide video (anything above 2.40:1). For developer guidance, see [resizeAspect](https://developer.apple.com/documentation/avfoundation/avlayervideogravity/resizeaspect).

In visionOS and tvOS, the built-in video player also provides *transport controls,* which let people perform playback tasks, like turning on subtitles or changing the audio language, and actions, like adding a show to a library or favoriting a clip. Below the transport controls, the video player displays *content tabs*, like Info, Episodes, or Chapters, that can provide supporting information and help streamline navigation. In visionOS, the transport controls appear as an ornament.

## Best practices

**Use the system video player to give people a familiar and convenient experience.** The built-in video player provides an exceptional video playback experience that offers consistent interactions and behaviors that let people concentrate on enjoying immersive content. If your app truly requires a custom video player, reference the behavior and interface of the system video player to help you provide an experience that people can instantly understand. A custom experience that diverges slightly from the system-provided experience can cause frustration because people don’t know which of their habitual interactions they can continue to use.

**Always display video content at its original aspect ratio.** When video content uses embedded letterbox or pillarbox padding to conform to a specific aspect ratio, the system may be unable to correctly scale the video based on the current playback mode. Padding embedded within the video frame can cause videos to appear smaller in both full-screen and fit-to-screen modes. It also prevents videos from displaying correctly in edge-to-edge, non-full-screen contexts, like Picture in Picture mode on iPad.

Here are some examples that show how padding can affect video display on iPhone Xs.

*Illustrated: Result of padding a 4:3 video, Result of padding a 21:9 video.*

**Provide additional information when it adds value.** In iOS, iPadOS, tvOS, and visionOS, you can customize a video’s additional information by providing an image, title, description, and other useful information. In general, restrict this content so that it doesn’t obscure media playback. For developer guidance, see [externalMetadata](https://developer.apple.com/documentation/avfoundation/avplayeritem/externalmetadata).

**Support the interactions people expect, regardless of the input device they’re using to control playback.** For example, people expect to press Space on a connected keyboard to play or pause media playback on Apple Vision Pro, Mac, iPhone, iPad, and Apple TV. Similarly, people expect to move through their media on Apple TV by making familiar, intuitive gestures with the Siri Remote. For guidance, see Keyboards and Remotes.

**If people need to access playback options or content-specific information in your tvOS app, consider adding a transport control or a custom content tab.** People typically open a transport control or content tab while they’re watching a video, so it’s essential to provide only the most useful actions and information. Help people return quickly to the viewing experience by making sure your actions don’t take more than a step or two and your content is succinct. Use a transport control to support a playback-related action like favoriting a video; use custom content tabs to display supplementary information or recommendations.

**Avoid allowing audio from different sources to mix as viewers switch between modes.** Mixed audio is an unpleasant and frustrating user experience. In general, audio mixes when at least one of the audio sources fails to handle secondary audio correctly. Here is a typical scenario: While watching a full-screen video, the viewer moves it into the PiP window, where the system automatically mutes the video. In the full-screen window, the viewer starts a game that plays background music, then switches to the PiP window and unmutes the video. If the game doesn’t handle secondary audio appropriately, its audio mixes with the audio from the unmuted video. For developer guidance, see [silenceSecondaryAudioHintNotification](https://developer.apple.com/documentation/avfaudio/avaudiosession/silencesecondaryaudiohintnotification).

## Integrating with the TV app

The TV app provides global access to favorite, recently played, and recommended video content from across the system. When people initiate content playback within your app, the TV app automatically opens your app and transitions to it. Follow these guidelines to help the TV app experience feel like an integrated part of your app.

**Ensure a smooth transition to your app.** The TV app fades to black when transitioning to your app and doesn’t show your app’s launch screen. Maintain visual continuity with this transition by immediately presenting your own black screen before starting to play or resume content.

**Show the expected content immediately.** People expect the content they choose to begin playing as soon as the transition to your app completes, especially when resuming playback. Jump right from your app’s black screen into content, and avoid displaying splash screens, detail screens, intro animations, or any other barriers that make it take longer to reach content. In rare situations where you must display an interstitial element before the selected media plays, people can choose Select to step through the element, or choose Play if they want to skip the interstitial content and start playback.

**Avoid asking people if they want to resume playback.** If playback can be resumed, do so automatically without prompting for confirmation.

**Play or pause playback when people press Space on a connected Bluetooth keyboard.** Pressing Space to control media playback is an interaction people expect, regardless of the keyboard they’re using.

**Make sure content plays for the correct viewer.** If your app supports multiple user profiles, the TV app can specify a profile when issuing a playback request. Make your app automatically switch to this profile before starting playback. If a playback request doesn’t specify a profile, ask the viewer to choose one before playback begins so this information is available in the future.

**Use the previous end time when resuming playback of a long video clip.** Resuming playback at the previous stopping point lets people quickly continue where they left off.

### Loading content

**Avoid displaying loading screens when possible.** A loading screen is unnecessary if your content loads quickly, but if loading takes more than two seconds, consider showing a black loading screen with a centered activity spinner and no surrounding content.

**Start playback immediately.** If you must display a loading screen, display it only until enough content loads for playback to begin. Continue loading remaining content in the background.

**Minimize loading screen content.** If you include branding or images on your loading screen, do so minimally while maintaining the black background that helps provide a seamless transition to playback.

### Exiting playback

After exiting playback, people remain in your app rather than returning to the TV app, so it’s a good idea to help them avoid becoming disoriented.

**Show a contextually relevant screen.** When exiting playback, display a detail view for the content the viewer was just watching and include an option to resume playback. If a detail view isn’t available, show either a menu that lists this content or your app’s main menu.

**Be prepared for an immediate exit.** Prepare an exit view as soon as possible after receiving a playback notification so you’re ready to display the view if people exit immediately after playback begins.

## Platform considerations

*No additional considerations for iOS, iPadOS, or macOS.*

## Change log

| Date | Changes |
| --- | --- |
| September 12, 2023 | Corrected the recommended width for a thumbnail in visionOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |

## Related guidelines

- [Playing audio](playing-audio.md)
- [Feedback](feedback.md)

---


<a id="printing"></a>
## printing

# Printing

> Source: <https://developer.apple.com/design/human-interface-guidelines/printing>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to visionOS omitted)

An iOS, iPadOS, macOS, or visionOS app can integrate system-provided print functionality when it makes sense, presenting custom printer- and document-specific options if necessary.

---

## Best practices

**Make printing discoverable.** Help people find your print action by placing it in standard system locations. For example, include a Print item in your macOS app’s File menu; in your iOS or iPadOS app, add a toolbar button that opens an [action sheet](action-sheets.md). If your macOS app has a toolbar, you might want to put a Print button there, too, but consider making it an optional button that people can add when they customize the toolbar.

**Present a printing option only when it’s possible.** If there’s nothing onscreen to print, or no printers are available, dim the Print item in a macOS app’s File menu and remove the Print action from the Action sheet in an iOS or iPadOS app. If you implement a custom print button, dim or hide it when printing isn’t possible.

**Present relevant printing options.** If it makes sense to offer options like selecting a page range, requesting multiple copies, or printing on both sides — and the printer supports the options — use the system-provided view to present them.

## Platform considerations

*No additional considerations for iOS, iPadOS, or visionOS. Not supported in tvOS or watchOS.*

### Desktop (macOS)

**If your macOS app offers app-specific print options that the system doesn’t offer, consider creating a custom category for the print panel.** By default, the print panel offers several categories of settings, such as Layout, Paper Handling, and Media & Quality. Give your custom category a unique name, such as your app name, and include options that help people have a great print experience in your app. For example, Keynote offers presentation-specific options, like the ability to print presenter notes, slide backgrounds, and skipped slides.

**If your app supports document-specific page settings, consider presenting a page setup dialog.** A *page setup dialog* includes rarely changed settings for page size, orientation, and scaling that apply to printing a particular document. If this makes sense in your app, avoid implementing features the system already provides. For example, you don’t need to include options like changing the page orientation or printing in reverse order because the system implements these options.

**Make sure interdependencies between options are clear.** For example, if double-sided printing is available, an option to print on transparencies becomes unavailable.

**Separate advanced features from frequently used features.** Consider using a disclosure control to hide advanced options until they’re needed. Label advanced options as *Advanced Options*.

**Consider letting people preview the effect of a setting.** For example, you could update a thumbnail image to show the effect of changing a tone control.

**Consider storing modified settings with the document.** At minimum, it makes sense to store print settings until the document is closed in case people want to print it again.

## Related guidelines

- [File management](file-management.md)

---


<a id="ratings-and-reviews"></a>
## ratings-and-reviews

# Ratings and reviews

> Source: <https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2023-09-12 (Added artwork.)

People often view the ratings and reviews for an app or game before they download it.

---

Delivering a great overall experience is the best way to encourage positive ratings and reviews, but it’s also crucial to choose the right time to ask people for feedback. Although every app is different, some possible ways to do this involve looking at how many times or how frequently people launch your app, the number of features someone explores, or the number of tasks they complete.

People can always rate your app within the App Store.

## Best practices

**Ask for a rating only after people have demonstrated engagement with your app or game.** For example, you might prompt people when they complete a game level or a significant task. Avoid asking for a rating on first launch or during onboarding, because people haven’t had enough time to gain a clear understanding of your app’s value or form an opinion. People may even be more likely to leave negative feedback if they feel an app is asking for a rating before they get a chance to use it.

**Avoid interrupting people while they’re performing a task or playing a game.** Asking for feedback can disrupt the user experience and feel like a burden. Look for natural breaks or stopping points in your app or game where a rating request is less likely to be bothersome.

**Avoid pestering people.** Repeated rating requests can be irritating, and may even negatively influence people’s opinion of your app. Consider allowing at least a week or two between requests, prompting again after people demonstrate additional engagement with your experience.

**Prefer the system-provided prompt.** iOS, iPadOS, and macOS offer a consistent, nonintrusive way for apps and games to request ratings and reviews. When you identify places in your experience where it makes sense to ask for feedback, the system checks for previous feedback and — if there isn’t any — displays an in-app prompt that asks for a rating and an optional written review. People can supply feedback or dismiss the prompt with a single tap or click; they can also opt out of receiving these prompts for all apps they have installed. The system automatically limits the display of the prompt to three occurrences per app within a 365-day period. For developer guidance, see [RequestReviewAction](https://developer.apple.com/documentation/storekit/requestreviewaction).

**Weigh the benefits of resetting your summary rating against the potential disadvantage of showing fewer ratings.** When you release a new version of your app or game, you can reset the summary of individual ratings you received since the last reset. Although resetting means that the ratings reflect the current version, it also tends to result in having fewer ratings overall, which can discourage some people from downloading your app. For developer guidance, see [Reset app summary rating](https://help.apple.com/app-store-connect/#/devfb7e87af8).

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| September 12, 2023 | Added artwork. |

---


<a id="searching"></a>
## searching

# Searching

> Source: <https://developer.apple.com/design/human-interface-guidelines/searching>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2026-06-08 (Updated terminology and refined best practices.)

People use various search techniques to find content on their device, within an app, and within a document or file.

---

To search for content within an app, people generally expect to use a [search field](search-fields.md). When it makes sense, you can personalize the search experience by using what you know about how people interact with your app. For example, you might display recent searches, search suggestions, completions, or corrections based on terms people searched earlier in your app.

In some cases, people appreciate the ability to scope a search or filter the results. For example, people might want to search for items by specifying attributes like creation date, file size, or file type. For guidance, see [Scope bars and tokens](search-fields.md#scope-bars-and-tokens). You can also help people find content within an open document or file by implementing ways to find content in a window or page in your iOS, iPadOS, or macOS app.

In iOS, iPadOS, and macOS, Spotlight helps people find content across all apps in the system and on the web. When you index and provide information about your app’s content, people can use Spotlight to find content your app contains without opening it first. For guidance, see [Systemwide search](#systemwide-search).

## Best practices

**If search is important, give it a primary position in your app or view.** For example, in the Notes app, a search field is in the bottom [toolbar](toolbars.md) alongside other important actions. In apps that use [tab bars](tab-bars.md), like Photos and Apple TV, search is a dedicated tab.

**Aim to make your app’s content searchable through a single location.** People appreciate having one clearly identified location they can use to find anything they’re looking for in your app. For apps with clearly distinct sections, it may still be useful to offer a local search. For example, search acts as a filter on the current view when searching your songs and albums in the iOS Music app.

**Clearly display the current scope of a search.** Use a descriptive placeholder text, a [scope bar](search-fields.md#scope-bars-and-tokens), or a title to help reinforce what someone is currently searching. For example, in the Mail app there is always a clear reference to the mailbox someone is searching.

**Provide suggestions to make searching easier.** When you display a personʼs recent searches before they start typing or offer predictive search suggestions while they’re typing, you can help people search faster and type less. For developer guidance, see [searchSuggestions(_:)](https://developer.apple.com/documentation/swiftui/view/searchsuggestions(_:)).

**Take privacy into consideration before displaying search history.** People might not appreciate having their search history appear where others might see it. If you do show search history, provide a way for people to clear it if they want.

## Systemwide search

**Make your app’s content searchable in Spotlight.** You can share content with Spotlight by making it indexable and specifying descriptive attributes known as *metadata*. Spotlight extracts, stores, and organizes this information to allow for fast, comprehensive searches.

**Define metadata for custom file types you handle.** Supply a Spotlight File Importer plug-in that describes the types of metadata your file format contains. For developer guidance, see [CSImportExtension](https://developer.apple.com/documentation/corespotlight/csimportextension).

**Use Spotlight to offer advanced file-search capabilities within the context of your app.** For example, you might include a button that instantly initiates a Spotlight search based on the current selection. You might then display a custom view that presents the search results or a filtered subset of them.

**Prefer using the system-provided open and save views.** The system-provided open and save views generally include a built-in search field that people can use to search and filter the entire system. For related guidance, see [File management](file-management.md).

**Implement a Quick Look generator if your app produces custom file types.** A Quick Look generator helps Spotlight and other apps show previews of your documents. For developer guidance, see [Quick Look](https://developer.apple.com/documentation/quicklook).

## Platform considerations

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| June 8, 2026 | Updated terminology and refined best practices. |
| June 9, 2025 | Updated best practices with general guidance from Search fields, and reorganized guidance for systemwide search. |

## Related guidelines

- [Search fields](search-fields.md)

---


<a id="settings"></a>
## settings

# Settings

> Source: <https://developer.apple.com/design/human-interface-guidelines/settings>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2024-06-10 (Reorganized some guidance into new topics and added game-specific examples.)

People expect apps and games to just work, but they also appreciate having ways to customize the experience to fit their needs.

---

On all Apple platforms, the system-provided Settings app lets people adjust things like the overall appearance of the system, network connections, account details, accessibility requirements, and language and region settings. On some platforms, the system-provided Settings app can also include settings for specific apps and games, often letting people adjust whether the app or game can access location information, use device features like microphone or camera, and integrate with system features like notifications, Siri, or Search.

When necessary, you can provide a custom settings area within your app or game to offer general settings that affect your overall experience, like interface style or game-saving behavior. If you need to offer settings that affect only a specific task, you can provide these options within the task itself, so people don’t have to leave the experience to customize it.

## Best practices

**Aim to provide default settings that give the best experience to the largest number of people.** For example, you can automatically maximize performance for the device your game is running on instead of asking players to make this choice after your game launches (for developer guidance, see [Improving your game’s graphics performance and settings](https://developer.apple.com/documentation/metal/improving-your-games-graphics-performance-and-settings)). When you choose appropriate default settings, people may not have to make any adjustments before they can start enjoying your app or game.

**Minimize the number of settings you offer.** Although people appreciate having control over an app or game, too many settings can make the experience feel less approachable, while also making it hard to find a particular setting.

**Make settings available in ways people expect.** For example, when a physical keyboard is connected, people often use the standard Command-Comma (,) keyboard shortcut to open an app’s settings, whereas in a game, players often use the Esc (Escape) key.

**Avoid using settings to ask for setup information you can get in other ways.** For example, a game can automatically detect a connected controller or accessory instead of asking the player to identify it; an app can detect whether people are currently using Dark Mode.

**Respect people’s systemwide settings and avoid including redundant versions of them in your custom settings area.** People expect to use the system-provided Settings app to manage global options like accessibility accommodations, scrolling behavior, and authentication methods, and they expect all apps and games to adhere to their choices. Including custom versions of global options in your settings area is likely to confuse people because it implies that systemwide settings may not apply to your app or game and that changing your custom version of a global setting may affect other apps and games, too.

## General settings

**Put general, infrequently changed settings in your custom settings area.** People must suspend what they’re doing to open an app’s or game’s settings area, so you want to include options that people don’t need to change all the time. For example, an app might list options for adjusting window configuration; a game might let players specify game-saving behavior or keyboard mappings; both apps and games might offer options related to people’s accounts.

## Task-specific options

**When possible, prefer letting people modify task-specific options without going to your settings area.** For example, if people can adjust things like showing or hiding parts of the current view, reordering a collection of items, or filtering a list, make these options available in the screens they affect, where they’re discoverable and convenient. Putting this type of option in a separate settings area disconnects it from its context, requiring people to suspend their task to make adjustments, and often hiding the results until people resume the task.

> **Note:** In games, players tend to adjust their approach to a specific task as part of the gameplay, not as a settings option to change.

## System settings

**Add only the most rarely changed options to the system-provided Settings app.** If it makes sense to add your app’s or game’s settings to the system-provided Settings app, consider providing a button that opens it directly from your interface.

## Platform considerations

*No additional considerations for iOS, iPadOS, tvOS, or visionOS.*

### Desktop (macOS)

When people choose the Settings item in your app’s or game’s App menu, your custom settings window opens. Typically, a custom settings window contains a toolbar that includes buttons for switching between views — called *panes* — that each contain a group of related settings.

**Include a settings item in the [App menu](the-menu-bar.md#app-menu).** Avoid adding settings buttons to a window’s toolbar, because doing so decreases the space available for essential commands that people use frequently. If you provide document-level options, add this item to your app’s [File menu](the-menu-bar.md#file-menu).

**Dim a settings window’s minimize and maximize buttons.** It’s quick to open a custom settings window using the standard Command–Comma (,) keyboard command, so there’s no need to keep the window in the Dock, and because a settings window accommodates the size of the current pane, people don’t need to expand the window to see more.

**In your settings window, use a noncustomizable toolbar that remains visible and always indicates the active toolbar button.** A settings window’s toolbar identifies the areas people can customize and helps people navigate among those areas. People rely on a stable settings interface to help them find what they need.

**Update the window’s title to reflect the currently visible pane.** If your settings window doesn’t have multiple panes, use the title *App Name* Settings.

**Restore the most recently viewed pane.** People often adjust related settings more than once, so it can be convenient when a settings window opens to the last pane people used.

## Change log

| Date | Changes |
| --- | --- |
| June 10, 2024 | Reorganized some guidance into new topics and added game-specific examples. |

## Related guidelines

- [Onboarding](onboarding.md)

---


<a id="undo-and-redo"></a>
## undo-and-redo

# Undo and redo

> Source: <https://developer.apple.com/design/human-interface-guidelines/undo-and-redo>
> Section: Patterns
> Platforms covered: iOS, iPadOS, macOS (guidance specific to visionOS omitted)

Undo and redo gives people easy ways to reverse many types of actions, which can also help people explore and experiment safely as they learn a new interface or task.

---

People expect undo and redo to let them reverse their recent actions, so they’re likely to try undoing — often multiple times — until something changes. In a situation like this, people might not remember which of their previous actions an undo is targeting, which can lead to unintended changes and frustration. To help people remain in control, it’s essential to help people predict the outcome of undoing and redoing and to highlight the results.

## Best practices

**Help people predict the results of undo and redo as much as possible.** On iPhone, for example, you can describe the result in the alert that displays when people shake the device, giving them the option of performing the undo or canceling it. If you provide undo and redo menu items, you can modify the menu item labels to identify the result. For example, a document-based app might use menu item labels like Undo Typing or Redo Bold.

**Show the results of an undo or redo.** Sometimes, the most recent action that people want to undo affects content or an area that’s no longer visible. In cases like this, it’s crucial to highlight the result of each undo and redo to keep people from thinking that the action had no effect, which can lead them to perform it repeatedly. For example, if people undo after deleting a paragraph in a document area that’s no longer onscreen, you might scroll the document to show the restored paragraph.

**Let people undo multiple times.** Avoid placing unnecessary limits on the number of times people can undo or redo. People generally expect to undo every action they’ve performed since taking a logical step like opening a document or saving their work.

**Consider giving people the option to revert multiple changes at once.** In some scenarios, people might appreciate the ability to undo a batch of discrete but related actions — like incremental adjustments to a single property or attribute — so they don’t have to undo each individual adjustment. In other cases, it can make sense to give people a convenient way to undo all the changes they made since opening a document or saving their work.

**Provide undo and redo buttons only when necessary.** People generally expect to initiate undo and redo in system-supported ways, such as choosing the items in a macOS app’s Edit menu, using keyboard shortcuts on a Mac or iPad, or shaking their iPhone. If it’s important to provide dedicated undo and redo buttons in your app, use the standard system-provided symbols and put the buttons in a toolbar.

## Platform considerations

### Mobile (iOS, iPadOS)

**Avoid redefining standard gestures for undo and redo.** For example, people can use a three-finger swipe to initiate an undo or redo, or shake their iPhone. As with all standard gestures, redefining them in your interface runs the risk of confusing people and making your experience unpredictable.

**Briefly and precisely describe the operation to be undone or redone.** The undo and redo alert title automatically includes a prefix of “Undo ” or “Redo ” (including the trailing space). You need to provide an additional word or two that describes what’s being undone or redone, to appear after this prefix. For example, you might create alert titles such as “Undo Name” or “Redo Address Change.”

### Desktop (macOS)

**Place undo and redo commands in the Edit menu and support the standard keyboard shortcuts.** Mac users expect to find undo and redo at the top of the Edit menu; they also expect to use Command–Z and Shift–Command–Z to perform undo and redo, respectively.

## Related guidelines

- [Feedback](feedback.md)
- [Pointing devices](pointing-devices.md)

---
