# Apple HIG — Components › Menus and actions
Bundled HIG pages for the “Components › Menus and actions” group. Each page kept verbatim under an anchor heading `## <slug>`. Cite as **components-menus-and-actions.md › <slug> › heading**.


<a id="activity-views"></a>
## activity-views

# Activity views

> Source: <https://developer.apple.com/design/human-interface-guidelines/activity-views>
> Section: Components › Menus and actions
> Platforms covered: iOS, iPadOS (guidance specific to visionOS omitted)

An activity view — often called a *share sheet* — presents a range of tasks that people can perform in the current context.

---

Activity views present sharing activities like messaging and actions like Copy and Print, in addition to quick access to frequently used apps. People typically reveal a share sheet by choosing an Action button while viewing a page or document, or after they’ve selected an item. An activity view can appear as a sheet or a popover, depending on the device and orientation.

You can provide app-specific activities that can appear in a share sheet when people open it within your app or game. For example, Photos provides app-specific actions like Copy Photo, Add to Album, and Adjust Location. By default, the system lists app-specific actions before actions — such as Add to Files or AirPlay — that are available in multiple apps or throughout the system. People can edit the list of actions to ensure that it displays the ones they use most and to add new ones.

You can also create app extensions to provide custom share and action activities that people can use in other apps. (An *app extension* is code you provide that people can install and use outside of your app.) For example, you might create a custom share activity that people can install to help them share a webpage with a specific social media service. Even though macOS doesn’t provide an activity view, you can create share and action app extensions that people can use on a Mac. For guidance, see [Share and action extensions](#share-and-action-extensions).

## Best practices

**Avoid creating duplicate versions of common actions that are already available in the activity view.** For example, providing a duplicate Print action is unnecessary and confusing because people wouldn’t know how to distinguish your action from the system-provided one. If you need to provide app-specific functionality that’s similar to an existing action, give it a custom title. For example, if you let people use custom formatting to print a bank transaction, use a title that helps people understand what your print activity does, like “Print Transaction.”

**Consider using a symbol to represent your custom activity.** [SF Symbols](sf-symbols.md) provides a comprehensive set of configurable symbols you can use to communicate items and concepts in an activity view. If you need to create a custom interface icon, center it in an area measuring about 70x70 pixels. For guidance, see [Icons](icons.md).

**Write a succinct, descriptive title for each custom action you provide.** If a title is too long, the system wraps it and may truncate it. Prefer a single verb or a brief verb phrase that clearly communicates what the action does. Avoid including your company or product name in an action title. In contrast, the share sheet displays the title of a share activity — typically a company name — below the icon that represents it.

**Make sure activities are appropriate for the current context.** Although you can’t reorder system-provided tasks in an activity view, you can exclude tasks that aren’t applicable to your app. For example, if it doesn’t make sense to print from within your app, you can exclude the Print activity. You can also identify which custom tasks to show at any given time.

**Use the Share button to display an activity view.** People are accustomed to accessing system-provided activities when they choose the Share button. Avoid confusing people by providing an alternative way to do the same thing.

## Share and action extensions

Share extensions give people a convenient way to share information from the current context with apps, social media accounts, and other services. Action extensions let people initiate content-specific tasks — like adding a bookmark, copying a link, editing an inline image, or displaying selected text in another language — without leaving the current context.

The system presents share and action extensions differently depending on the platform:

- In iOS and iPadOS, share and action extensions are displayed in the share sheet that appears when people choose an Action button.
- In macOS, people access share extensions by clicking a Share button in the toolbar or choosing Share in a context menu. People can access an action extension by holding the pointer over certain types of embedded content — like an image they add to a Mail compose window — clicking a toolbar button, or choosing a quick action in a Finder window.

**If necessary, create a custom interface that feels familiar to people.** For a share extension, prefer the system-provided composition view because it provides a consistent sharing experience that people already know. For an action extension, include your app name. If you need to present an interface, include elements of your app’s interface to help people understand that your extension and your app are related.

**Streamline and limit interaction.** People appreciate extensions that let them perform a task in just a few steps. For example, a share extension might immediately post an image to a social media account with a single tap or click.

**Avoid placing a modal view above your extension.** By default, the system displays an extension within a modal view. While it might be necessary to display an alert above an extension, avoid displaying additional modal views.

**If necessary, provide an image that communicates the purpose of your extension.** A share extension automatically uses your app icon, helping give people confidence that your app provided the extension. For an action extension, prefer using a [symbol](sf-symbols.md) or creating an interface [icon](icons.md) that clearly identifies the task.

**Use your main app to denote the progress of a lengthy operation.** An activity view dismisses immediately after people complete the task in your share or action extension. If a task is time-consuming, continue it in the background, and give people a way to check the status in your main app. Although you can use a notification to tell people about a problem, don’t notify them simply because the task completes.

## Platform considerations

*No additional considerations for iOS, iPadOS, or visionOS. Not supported in macOS, tvOS, or watchOS.*

## Related guidelines

- [Sheets](sheets.md)
- [Popovers](popovers.md)

---


<a id="buttons"></a>
## buttons

# Buttons

> Source: <https://developer.apple.com/design/human-interface-guidelines/buttons>
> Section: Components › Menus and actions
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-12-16 (Updated guidance for Liquid Glass.)

A button initiates an instantaneous action.

---

Versatile and highly customizable, buttons give people simple, familiar ways to do tasks in your app. In general, a button combines three attributes to clearly communicate its function:

- **Style.** A visual style based on size, color, and shape.
- **Content.** A symbol (or icon), text label, or both that a button displays to convey its purpose.
- **Role.** A system-defined role that identifies a button’s semantic meaning and can affect its appearance.

There are also many button-like components that have distinct appearances and behaviors for specific use cases, like [toggles](toggles.md), [pop-up buttons](pop-up-buttons.md), and [segmented controls](segmented-controls.md).

## Best practices

When buttons are instantly recognizable and easy to understand, an app tends to feel intuitive and well designed.

**Make buttons easy for people to use.** It’s essential to include enough space around a button so that people can visually distinguish it from surrounding components and content. Giving a button enough space is also critical for helping people select or activate it, regardless of the method of input they use. As a general rule, a button needs a hit region of at least 44x44 pt — in visionOS, 60x60 pt — to ensure that people can select it easily, whether they use a fingertip, a pointer, their eyes, or a remote.

**Always include a press state for a custom button.** Without a press state, a button can feel unresponsive, making people wonder if it’s accepting their input.

## Style

System buttons offer a range of styles that support customization while providing built-in interaction states, accessibility support, and appearance adaptation. Different platforms define different styles that help you communicate hierarchies of actions in your app.

**In general, use a button that has a prominent visual style for the most likely action in a view.** To draw people’s attention to a specific button, use a prominent button style so the system can apply an accent color to the button’s background. Buttons that use color tend to be the most visually distinctive, helping people quickly identify the actions they’re most likely to use. Keep the number of prominent buttons to one or two per view. Presenting too many prominent buttons increases cognitive load, requiring people to spend more time considering options before making a choice.

**Use style — not size — to visually distinguish the preferred choice among multiple options.** When you use buttons of the same size to offer two or more options, you signal that the options form a coherent set of choices. By contrast, placing two buttons of different sizes near each other can make the interface look confusing and inconsistent. If you want to highlight the preferred or most likely option in a set, use a more prominent button style for that option and a less prominent style for the remaining ones.

**Avoid applying a similar color to button labels and content layer backgrounds.** If your app already has bright, colorful content in the content layer, prefer using the default monochromatic appearance of button labels. For more guidance, see [Liquid Glass color](color.md#liquid-glass-color).

## Content

**Ensure that each button clearly communicates its purpose.** Depending on the platform, a button can contain a symbol (or icon), a text label, or both to help people understand what it does.

> **Note:** In macOS and visionOS, the system displays a tooltip after people hover over a button for a moment. A tooltip displays a brief phrase that explains what a button does; for guidance, see [Offering help](offering-help.md).

**Try to associate familiar actions with familiar icons.** For example, people can predict that a button containing the `square.and.arrow.up` symbol will help them perform share-related activities. If it makes sense to use an icon in your button, consider using an existing or customized [symbol](sf-symbols.md). For a list of symbols that represent common actions, see [Standard icons](icons.md#standard-icons).

**Consider using text when a short label communicates more clearly than an icon.** To use text, write a few words that succinctly describe what the button does. Using [title-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64), consider starting the label with a verb to help convey the button’s action — for example, a button that lets people add items to their shopping cart might use the label “Add to Cart.”

## Role

A system button can have one of the following roles:

- **Normal.** No specific meaning.
- **Primary.** The button is the default button — the button people are most likely to choose.
- **Cancel.** The button cancels the current action.
- **Destructive.** The button performs an action that can result in data destruction.

A button’s role can have additional effects on its appearance. For example, a primary button uses an app’s accent color, whereas a destructive button uses the system red color.

**Assign the primary role to the button people are most likely to choose.** When a primary button responds to the Return key, it makes it easy for people to quickly confirm their choice. In addition, when the button is in a temporary view — like a [sheet](sheets.md), an editable view, or an [alert](alerts.md) — assigning it the primary role means that the view can automatically close when people press Return.

**Don’t assign the primary role to a button that performs a destructive action, even if that action is the most likely choice.** Because of its visual prominence, people sometimes choose a primary button without reading it first. Help people avoid losing content by assigning the primary role to nondestructive buttons.

## Platform considerations

### Mobile (iOS, iPadOS)

**Configure a button to display an activity indicator when you need to provide feedback about an action that doesn’t instantly complete.** Displaying an activity indicator within a button can save space in your user interface while clearly communicating the reason for the delay. To help clarify what’s happening, you can also configure the button to display a different label alongside the activity indicator. For example, the label “Checkout” could change to “Checking out…” while the activity indicator is visible. When a delay occurs after people click or tap your configured button, the system displays the activity indicator next to the original or alternative label, hiding the button image, if there is one.

### Desktop (macOS)

Several specific button types are unique to macOS.

#### Push buttons

The standard button type in macOS is known as a *push button*. You can configure a push button to display text, a symbol, an icon, or an image, or a combination of text and image content. Push buttons can act as the default button in a view and you can tint them.

**Use a flexible-height push button only when you need to display tall or variable height content.** Flexible-height buttons support the same configurations as regular push buttons — and they use the same corner radius and content padding — so they look consistent with other buttons in your interface. If you need to present a button that contains two lines of text or a tall icon, use a flexible-height button; otherwise, use a standard push button. For developer guidance, see [NSButton.BezelStyle.flexiblePush](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/flexiblepush).

**Append a trailing ellipsis to the title when a push button opens another window, view, or app.** Throughout the system, an ellipsis in a control title signals that people can provide additional input. For example, the Edit buttons in the AutoFill pane of Safari Settings include ellipses because they open other views that let people modify autofill values.

**Consider supporting spring loading.** On systems with a Magic Trackpad, *spring loading* lets people activate a button by dragging selected items over it and force clicking — that is, pressing harder — without dropping the selected items. After force clicking, people can continue dragging the items, possibly to perform additional actions.

#### Square buttons

A *square button* (also known as a *gradient button*) initiates an action related to a view, like adding or removing rows in a table.

Square buttons contain symbols or icons — not text — and you can configure them to behave like push buttons, toggles, or pop-up buttons. The buttons appear in close proximity to their associated view — usually within or beneath it — so people know which view the buttons affect.

**Use square buttons in a view, not in the window frame.** Square buttons aren’t intended for use in toolbars or status bars. If you need a button in a [toolbar](toolbars.md), use a toolbar item.

**Prefer using a symbol in a square button.** [SF Symbols](sf-symbols.md) provides a wide range of symbols that automatically receive appropriate coloring in their default state and in response to user interaction.

**Avoid using labels to introduce square buttons.** Because square buttons are closely connected with a specific view, their purpose is generally clear without the need for descriptive text.

For developer guidance, see [NSButton.BezelStyle.smallSquare](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/smallsquare).

#### Help buttons

A *help button* appears within a view and opens app-specific help documentation.

Help buttons are circular, consistently sized buttons that contain a question mark. For guidance on creating help documentation, see [Offering help](offering-help.md).

**Use the system-provided help button to display your help documentation.** People are familiar with the appearance of the standard help button and know that choosing it opens help content.

**When possible, open the help topic that’s related to the current context.** For example, the help button in the Rules pane of Mail settings opens the Mail User Guide to a help topic that explains how to change these settings. If no specific help topic applies directly to the current context, open the top level of your app’s help documentation when people choose a help button.

**Include no more than one help button per window.** Multiple help buttons in the same context make it hard for people to predict the result of clicking one.

**Position help buttons where people expect to find them.** Use the following locations for guidance.

| View style | Help button location |
| --- | --- |
| Dialog with dismissal buttons (like OK and Cancel) | Lower corner, opposite to the dismissal buttons and vertically aligned with them |
| Dialog without dismissal buttons | Lower-left or lower-right corner |
| Settings window or pane | Lower-left or lower-right corner |

**Use a help button within a view, not in the window frame.** For example, avoid placing a help button in a toolbar or status bar.

**Avoid displaying text that introduces a help button.** People know what a help button does, so they don’t need additional descriptive text.

#### Image buttons

An *image button* appears in a view and displays an image, symbol, or icon. You can configure an image button to behave like a push button, toggle, or pop-up button.

**Use an image button in a view, not in the window frame.** For example, avoid placing an image button in a toolbar or status bar. If you need to use an image as a button in a toolbar, use a toolbar item. See [Toolbars](toolbars.md).

**Include about 10 pixels of padding between the edges of the image and the button edges.** An image button’s edges define its clickable area even when they aren’t visible. Including padding ensures that a click registers correctly even if it’s not precisely within the image. In general, avoid including a system-provided border in an image button; for developer guidance, see [isBordered](https://developer.apple.com/documentation/appkit/nsbutton/isbordered).

**If you need to include a label, position it below the image button.** For related guidance, see [Labels](labels.md).

## Change log

| Date | Changes |
| --- | --- |
| December 16, 2025 | Updated guidance for Liquid Glass. |
| June 9, 2025 | Updated guidance for button styles and content. |
| February 2, 2024 | Noted that visionOS buttons don’t support custom hover effects. |
| December 5, 2023 | Clarified some terminology and guidance for buttons in visionOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance for using buttons in watchOS. |

## Related guidelines

- [Pop-up buttons](pop-up-buttons.md)
- [Pull-down buttons](pull-down-buttons.md)
- [Toggles](toggles.md)
- [Segmented controls](segmented-controls.md)

---


<a id="context-menus"></a>
## context-menus

# Context menus

> Source: <https://developer.apple.com/design/human-interface-guidelines/context-menus>
> Section: Components › Menus and actions
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS omitted)
> Last change on Apple's site: 2023-12-05 (Added guidance on hiding unavailable menu items.)

A context menu provides access to functionality that’s directly related to an item, without cluttering the interface.

---

Although a context menu provides convenient access to frequently used items, it’s hidden by default, so people might not know it’s there. To reveal a context menu, people generally choose a view or select some content and then perform an action, using the input modes their current configuration supports. For example:

- The system-defined touch or pinch and hold gesture in visionOS, iOS, and iPadOS
- Pressing the Control key while clicking a pointing device in macOS and iPadOS
- Using a secondary click on a Magic Trackpad in macOS or iPadOS

## Best practices

**Prioritize relevancy when choosing items to include in a context menu.** A context menu isn’t for providing advanced or rarely used items; instead, it helps people quickly access the commands they’re most likely to need in their current context. For example, the context menu for a Mail message in the Inbox includes commands for replying and moving the message, but not commands for editing message content, managing mailboxes, or filtering messages.

**Aim for a small number of menu items.** A context menu that’s too long can be difficult to scan and scroll.

**Support context menus consistently throughout your app.** If you provide context menus for items in some places but not in others, people won’t know where they can use the feature and may think there’s a problem.

**Always make context menu items available in the main interface, too.** For example, in Mail in iOS and iPadOS, the context menu items that are available for a message in the Inbox are also available in the toolbar of the message view. In macOS, an app’s menu bar menus list all the app’s commands, including those in various context menus.

**If you need to use submenus to manage a menu’s complexity, keep them to one level.** A submenu is a menu item that reveals a secondary menu of logically related commands. Although submenus can shorten a context menu and clarify its commands, more than one level of submenu complicates the experience and can be difficult for people to navigate. If you need to include a submenu, give it an intuitive title that helps people predict its contents without opening it. For guidance, see [Submenus](menus.md#submenus).

**Hide unavailable menu items, don’t dim them.** Unlike a regular menu, which helps people discover actions they can perform even when the action isn’t available, a context menu displays only the actions that are relevant to the currently selected view or content. In macOS, the exceptions are the Cut, Copy, and Paste menu items, which may appear unavailable if they don’t apply to the current context.

**Aim to place the most frequently used menu items where people are likely to encounter them first.** When a context menu opens, people often read it starting from the part that’s closest to where their finger or pointer revealed it. Depending on the location of the selected content, a context menu might open above or below it, so you might also need to reverse the order of items to match the position of the menu.

**Show keyboard shortcuts in your app’s main menus, not in context menus.** Context menus already provide a shortcut to task-specific commands, so it’s redundant to display keyboard shortcuts too.

**Follow best practices for using separators.** As with other types of menus, you can use separators to group items in a context menu and help people scan the menu more quickly. In general, you don’t want more than about three groups in a context menu. For guidance, see [Menus](menus.md).

**In iOS, iPadOS, and visionOS, warn people about context menu items that can destroy data.** If you need to include potentially destructive items in your context menu — such as Delete or Remove — list them at the end of the menu and identify them as destructive (for developer guidance, see [destructive](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/destructive)). The system can display a destructive menu item using a red text color.

## Content

A context menu seldom displays a title. In contrast, each item in a context menu needs to display a short label that clearly describes what it does. For guidance, see [Menus > Labels](menus.md#labels).

**Include a title in a context menu only if doing so clarifies the menu’s effect.** For example, when people select multiple Mail messages and tap the Mark toolbar button in iOS and iPadOS, the resulting context menu displays a title that states the number of selected messages, reminding people that the command they choose affects all the messages they selected.

**Represent menu item actions with familiar icons.** Icons help people recognize common actions throughout your app. Use the same icons as the system to represent actions such as Copy, Share, and Delete, wherever they appear. For a list of icons that represent common actions, see [Standard icons](icons.md#standard-icons). For additional guidance, see [Menus](menus.md).

## Platform considerations

### Mobile (iOS, iPadOS)

**Provide either a context menu or an edit menu for an item, but not both.** If you provide both features for the same item, it can be confusing to people — and difficult for the system to detect their intent. See [Edit menus](edit-menus.md).

**In iPadOS, consider using a context menu to let people create a new object in your app.** iPadOS lets you reveal a context menu when people perform a long press on the touchscreen or use a secondary click with an attached trackpad or keyboard. For example, Files lets people create a new folder by revealing a context menu in an area between existing files and folders.

In iOS and iPadOS, a context menu can display a preview of the current content near the list of commands. People can choose a command in the menu or — in some cases — they can tap the preview to open it or drag it to another area.

**Prefer a graphical preview that clarifies the target of a context menu’s commands.** For example, when people reveal a context menu on a list item in Notes or Mail, the preview shows a condensed version of the actual content to help people confirm that they’re working with the item they intend.

**Ensure that your preview looks good as it animates.** As people reveal a context menu on an onscreen object, the system animates the preview image as it emerges from the content, dimming the screen behind the preview and the menu. It’s important to adjust the preview’s clipping path to match the shape of the preview image so that its contours, such as the rounded corners, don’t appear to change during animation. For developer guidance, see [UIContextMenuInteractionDelegate](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate).

### Desktop (macOS)

On a Mac, a context menu is sometimes called a *contextual* menu.

## Change log

| Date | Changes |
| --- | --- |
| December 5, 2023 | Added guidance on hiding unavailable menu items. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Refined guidance on including a submenu and added a guideline on using a context menu to support object creation in an iPadOS app. |

## Related guidelines

- [Menus](menus.md)
- [Edit menus](edit-menus.md)
- [Pop-up buttons](pop-up-buttons.md)
- [Pull-down buttons](pull-down-buttons.md)

---


<a id="dock-menus"></a>
## dock-menus

# Dock menus

> Source: <https://developer.apple.com/design/human-interface-guidelines/dock-menus>
> Section: Components › Menus and actions
> Platforms covered: macOS

On a Mac, people can secondary click an app’s or game’s icon in the Dock to reveal a Dock menu, which presents both system-provided and custom items.

---

The system-provided Dock menu items can vary depending on whether the app is open. For example, the Dock menu for Safari includes menu items for actions like viewing a current window or creating a new window.

> **Note:** Although iOS and iPadOS don’t support a Dock menu, people can reveal a similar menu of system-provided and custom items — called Home Screen quick actions — when they long press an app icon on the Home Screen or in the Dock. For guidance, see [Home Screen quick actions](home-screen-quick-actions.md).

## Best practices

As with all menus, you need to label Dock menu items succinctly and organize them logically. For guidance, see [Menus](menus.md).

**Make custom Dock menu items available in other places, too.** Not everyone uses a Dock menu, so it’s important to offer the same commands elsewhere, like in your menu bar menus or within your interface.

**Prefer high-value custom items for your Dock menu.** For example, a Dock menu can list all currently or recently open windows, making it a convenient way to jump to the window people want. Also consider listing a few of the actions that are most likely to be useful when your app isn’t frontmost or when there are no open windows. For example, Mail includes items for getting new mail and composing a new message in addition to listing all open windows.

## Platform considerations

*Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.*

## Related guidelines

- [Menus](menus.md)
- [Home Screen quick actions](home-screen-quick-actions.md)

---


<a id="edit-menus"></a>
## edit-menus

# Edit menus

> Source: <https://developer.apple.com/design/human-interface-guidelines/edit-menus>
> Section: Components › Menus and actions
> Platforms covered: iOS, iPadOS, macOS (guidance specific to visionOS omitted)
> Last change on Apple's site: 2023-06-21 (Updated to include guidance for visionOS.)

An edit menu lets people make changes to selected content in the current view, in addition to offering related commands like Copy, Select, Translate, and Look Up.

---

In addition to text, an edit menu’s commands can apply to many types of selectable content, such as images, files, and objects like contact cards, charts, or map locations. In iOS, iPadOS, and visionOS, the system automatically detects the data type of a selected item, which can result in the addition of a related action to the edit menu. For example, selecting an address can add an  item like *Get directions* to the edit menu.

Edit menus can look and behave slightly differently in different platforms.

- In iOS, the edit menu displays commands in a compact, horizontal list that appears when people touch and hold or double-tap to select content in a view. People can tap a chevron on the trailing edge to expand it into a [context menu](context-menus.md).
- In iPadOS, the edit menu looks different depending on how people reveal it. When people use touch interactions to reveal the menu, it uses the compact, horizontal appearance. In contrast, when people use a keyboard or pointing device to reveal it, the edit menu opens directly in a context menu.
- In macOS, people can access editing commands in a context menu they can reveal while in an editing task, as well as through the app’s [Edit menu](the-menu-bar.md#edit-menu) in the menu bar.
- In visionOS, people use the standard [pinch and hold](gestures.md#standard-gestures) gesture to open the edit menu as a horizontal bar, or they can open it in a context menu.

Editing content is rare in tvOS and watchOS experiences, so the system doesn’t provide an edit menu in these platforms.

## Best practices

**Prefer the system-provided edit menu.** People are familiar with the contents and behavior of the system-provided component, so creating a custom menu that presents the same commands is redundant and likely to be confusing. For a list of standard edit menu commands, see [UIResponderStandardEditActions](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions).

**Let people reveal an edit menu using the system-defined interactions they already know.** For example, people expect to touch and hold on a touchscreen, pinch and hold in visionOS, or use a secondary click with an attached trackpad or keyboard. Although the interactions to reveal an edit menu can differ based on platform, people don’t appreciate having to learn a custom interaction to perform a standard task.

**Offer commands that are relevant in the current context, removing or dimming commands that don’t apply.** For example, if nothing is selected, avoid showing options that require a selection, such as Copy or Cut. Similarly, avoid showing a Paste option when there’s nothing to paste.

**List custom commands near relevant system-provided ones.** For example, if you offer custom formatting commands, you can help maintain the ordering people expect by listing them after the system-provided commands in the format section. Avoid overwhelming people with too many custom commands.

**When it makes sense, let people select and copy noneditable text.** People appreciate being able to paste static content — such as an image caption or social media status — into a message, note, or web search. In general, let people copy content text, but not control labels.

**Support undo and redo when possible.** Like all menus, an edit menu doesn’t require confirmation before performing its actions, so people can easily use undo and redo to recover a previous state. For guidance, see [Undo and redo](undo-and-redo.md).

**In general, avoid implementing other controls that perform the same functions as edit menu items.** People typically expect to choose familiar edit commands in an edit menu, or use standard keyboard shortcuts. Offering redundant controls can crowd your interface, giving you less space for presenting actions that people might not already know about.

**Differentiate different types of deletion commands when necessary.** For example, a Delete menu item behaves the same as pressing a Delete key, but a Cut menu item copies the selected content to the system pasteboard before deleting it.

## Content

**Create short labels for custom commands.** Use verbs or short verb phrases that succinctly describe the action your command performs. For guidance, see [Labels](labels.md).

## Platform considerations

### Mobile (iOS, iPadOS)

**Ensure your edit menu works well in both styles.** The system displays the compact, horizontal style when people use Multi-Touch gestures to reveal the edit menu, and the vertical style when people use a keyboard or pointing device to reveal it. For guidance using the vertical menu layout, see [Menus > iOS, iPadOS](menus.md#mobile-ios-ipados).

**Adjust an edit menu’s placement, if necessary.** Depending on available space, the default menu position is above or below the insertion point or selection. The system also displays a visual indicator that points to the targeted content. Although you can’t change the shape of the menu or its pointer, you can change the menu’s position. For example, you might need to move the menu to prevent it from covering important content or parts of your interface.

### Desktop (macOS)

To learn about the order of items in a macOS app’s Edit menu, see [Edit menu](the-menu-bar.md#edit-menu).

## Change log

| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Added guidance on supporting both edit-menu styles in iPadOS. |

## Related guidelines

- [Menus](menus.md)
- [Context menus](context-menus.md)
- [The menu bar](the-menu-bar.md)
- [Undo and redo](undo-and-redo.md)

---


<a id="home-screen-quick-actions"></a>
## home-screen-quick-actions

# Home Screen quick actions

> Source: <https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions>
> Section: Components › Menus and actions
> Platforms covered: iOS, iPadOS

Home Screen quick actions give people a way to perform app-specific actions from the Home Screen.

---

People can get a menu of available quick actions when they touch and hold an app icon (on a 3D Touch device, people can press on the icon with increased pressure to see the menu). For example, Mail includes quick actions that open the Inbox or the VIP mailbox, initiate a search, and create a new message. In addition to app-specific actions, a Home Screen quick action menu also lists items for removing the app and editing the Home Screen.

Each Home Screen quick action includes a title, an interface icon on the left or right (depending on your app’s position on the Home Screen), and an optional subtitle. The title and subtitle are always left-aligned in left-to-right languages. Your app can even dynamically update its quick actions when new information is available. For example, Messages provides quick actions for opening your most recent conversations.

## Best practices

**Create quick actions for compelling, high-value tasks.** For example, Maps lets people search near their current location or get directions home without first opening the Maps app. People tend to expect every app to provide at least one useful quick action; you can provide a total of four.

**Avoid making unpredictable changes to quick actions.** Dynamic quick actions are a great way to keep actions relevant. For example, it may make sense to update quick actions based on the current location or recent activities in your app, time of day, or changes in settings. Make sure that actions change in ways that people can predict.

**For each quick action, provide a succinct title that instantly communicates the results of the action.** For example, titles like “Directions Home,” “Create New Contact,” and “New Message” can help people understand what happens when they choose the action. If you need to give more context, provide a subtitle too. Mail uses subtitles to indicate whether there are unread messages in the Inbox and VIP folder. Don’t include your app name or any extraneous information in the title or subtitle, keep the text short to avoid truncation, and take localization into account as you write the text.

**Provide a familiar interface icon for each quick action.** Prefer using [SF Symbols](sf-symbols.md) to represent actions. For a list of icons that represent common actions, see [Standard icons](icons.md#standard-icons); for additional guidance, see [Menus](menus.md).

If you design your own interface icon, use the Quick Action Icon Template that’s included with [Apple Design Resources for iOS and iPadOS](https://developer.apple.com/design/resources/#ios-apps).

**Don’t use an emoji in place of a symbol or interface icon.** Emojis are full color, whereas quick action symbols are monochromatic and change appearance in Dark Mode to maintain contrast.

## Platform considerations

*No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.*

## Related guidelines

- [Menus](menus.md)

---


<a id="menus"></a>
## menus

# Menus

> Source: <https://developer.apple.com/design/human-interface-guidelines/menus>
> Section: Components › Menus and actions
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2026-06-08 (Updated guidance for menu item icons.)

A menu reveals its options when people interact with it, making it a space-efficient way to present commands in your app or game.

---

Menus are ubiquitous in apps and games, so most people already know how to use them. Whether you use system-provided components or custom ones, people expect menus to behave in familiar ways. For example, people understand that opening a menu reveals one or more *menu items*, each of which represents a command, option, or state that affects the current selection or context. The guidance for labeling and organizing menu items applies to all types of menus in all experiences.

> **Note:** Several system-provided components also include menus that support specific use cases. For example, a [pop-up button](pop-up-buttons.md) or [pull-down button](pull-down-buttons.md) can reveal a menu of options directly related to its action; a [context menu](context-menus.md) lets people access a small number of frequently used actions relevant to their current view or task; and in macOS and iPadOS, [menu bar](the-menu-bar.md) menus contain all the commands people can perform in the app or game.

## Labels

A menu item’s label describes what it does and may include a symbol if it helps to clarify meaning. In an app, a menu item can also display the associated keyboard command, if there is one; in a game, a menu item rarely displays a keyboard command because a game typically needs to handle input from a wider range of devices and may offer game-specific mappings for various keys.

> **Note:** Depending on menu layout, an iOS, iPadOS, or visionOS app can display a few unlabeled menu items that use only symbols or icons to identify them. For guidance, see visionOS and [iOS, iPadOS](#mobile-ios-ipados).

**For each menu item, write a label that clearly and succinctly describes it.** In general, label a menu item that initiates an action using a verb or verb phrase that describes the action, such as View, Close, or Select. For guidance labeling menu items that show and hide something in the interface or show the currently selected state of something, see [Toggled items](#toggled-items). As with all the copy you write, let your app’s or game’s communication style guide the tone of the menu-item labels you create.

**To be consistent with platform experiences, use title-style capitalization.** Although a game might have a different writing style, generally prefer using title-style capitalization, which capitalizes every word except articles, coordinating conjunctions, and short prepositions, and capitalizes the last word in the label, regardless of the part of speech. For complete guidance on this style of capitalization in English, see [title-style capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64).

**Remove articles like *a*, *an*, and *the* from menu-item labels to save space.** In English, articles always lengthen labels, but rarely enhance understanding. For example, changing a menu-item label from  View Settings to View the Settings doesn’t provide additional clarification.

**Show people when a menu item is unavailable.** An unavailable menu item often appears dimmed and doesn’t respond to interactions. If all of a menu’s items are unavailable, the menu itself needs to remain available so people can open it and learn about the commands it contains.

**Append an ellipsis to a menu item’s label when the action requires more information before it can complete.** The ellipsis character (…) signals that people need to input information or make additional choices, typically within another view.

## Icons

**Represent common actions consistently.** The system provides standard icons to represent common actions like Share, Print, and Search. Using standard icons makes your app easier to use and more familiar. For a list of icons that represent common actions, see [Standard icons](icons.md#standard-icons).

**Use menu item icons sparingly and with purpose.** Icons allow people to find menu items more quickly, and help clarify what selecting an item does. Use an icon to highlight the most common actions and key features of your app, file system locations, connected devices, visual concepts like rotating or flipping an image, and user-generated content like folders and documents. Don’t display an icon if you can’t find one that clearly represents the menu item.

**Apply a uniform visual treatment across menu items in the same group.** For visual consistency and balance, provide icons for all menu items in a group, or none of them.

## Organization

Organizing menu items in ways that reflect how people use your app or game can make your experience feel straightforward and easy to use.

**Prefer listing important or frequently used menu items first.** People tend to start scanning a menu from the top, so listing high-priority items first often means that people can find what they want without reading the entire menu.

**Consider grouping logically related items.** For example, grouping editing commands like Copy, Cut, and Paste or camera commands like Look Up, Look Down, and Look Left can help people remember where to find them. To help people visually distinguish such groups, use a separator. Depending on the platform and type of menu, a *separator* appears between groups of items as a horizontal line or a short gap in the menu’s background appearance.

**Prefer keeping all logically related commands in the same group, even if the commands don’t all have the same importance.** For example, people generally use Paste and Match Style much less often than they use Paste, but they expect to find both commands in the same group that contains more frequently used editing commands like Copy and Cut.

**Be mindful of menu length.** People need more time and attention to read a long menu, which means they may miss the command they want. If a menu is too long, consider dividing it into separate menus. Alternatively, you might be able to use a submenu to shorten the list, such as listing difficulty levels in a submenu of a New Game menu item. The exception is when a menu contains user-defined or dynamically generated content, like the History and Bookmarks menus in Safari. People expect such a menu to accommodate all the items they add to it, so a long menu is fine, and scrolling is acceptable.

## Submenus

Sometimes, a menu item can reveal a set of closely related items in a subordinate list called a *submenu*. A menu item indicates the presence of a submenu by displaying a symbol — like a chevron — after its label. Submenus are functionally identical to menus, aside from their hierarchical positioning.

**Use submenus sparingly.** Each submenu adds complexity to the interface and hides the items it contains. You might consider creating a submenu when a term appears in more than two menu items in the same group. For example, instead of offering separate menu items for Sort by Date, Sort by Score, and Sort by Time, a game could present a menu item that uses a submenu to list the sorting options Date, Score, and Time. It generally works well to use the repeated term — in this case, *Sort by* — in the menu item’s label to help people predict the contents of the submenu.

**Limit the depth and length of submenus.** It can be difficult for people to reveal multiple levels of hierarchical submenus, so it’s generally best to restrict them to a single level. Also, if a submenu contains more than about five items, consider creating a new menu.

**Make sure a submenu remains available even when its nested menu items are unavailable.** A submenu item — like all menu items — needs to let people open it and learn about the commands it contains.

**Prefer using a submenu to indenting menu items.** Using indentation is inconsistent with the system and doesn’t clearly express the relationships between the menu items.

## Toggled items

Menu items often represent attributes or objects that people can turn on or off. If you want to avoid listing a separate menu item for each state, it can be efficient to create a single, toggled menu item that communicates the current state and lets people change it.

**Consider using a changeable label that describes an item’s current state.** For example, instead of listing two menu items like Show Map and Hide Map, you could include one menu item whose label changes from Show Map to Hide Map, depending on whether the map is visible.

**Include a verb if a changeable label isn’t clear enough.** For example, people might not know whether the changeable labels HDR On and HDR Off describe actions or states. If you needed to clarify that these items represent actions, you could add verbs to the labels, like Turn HDR On and Turn HDR Off.

**If necessary, display both menu items instead of one toggled item.** Sometimes, it helps people to view both actions or states at the same time. For example, a game could list both Take Account Online and Take Account Offline items, so when someone’s account is online, only the Take Account Offline menu item appears available.

**Consider using a checkmark to show that an attribute is currently in effect.** It’s easy for people to scan for checkmarks in a list of attributes to find the ones that are selected. For example, in the standard Format > Font menu, checkmarks can make it easy for people notice the styles that apply to selected text.

**Consider offering a menu item that makes it easy to remove multiple toggled attributes.** For example, if you let people apply several styles to selected text, it can work well to provide a menu item — such as Plain — that removes all applied formatting attributes at one time.

## In-game menus

In-game menus give players ways to control gameplay as well as determine [settings](settings.md) for the game as a whole.

**Let players navigate in-game menus using the platform’s default interaction method.** People expect to use the same interactions to navigate your menus as they use for navigating other menus on the device. For example, players expect to navigate your game menus using touch in iOS and iPadOS, and direct and indirect gestures in visionOS.

**Make sure your menus remain easy to open and read on all platforms you support.** Each platform defines specific sizes that work best for fonts and interaction targets. Sometimes, scaling your game content to display on a different screen — especially a mobile device screen — can make in-game menus too small for people to read or interact with. If this happens, modify the size of the tap targets and consider alternative ways to communicate the menu’s content. For guidance, see [Typography](typography.md) and [Touch controls](game-controls.md#touch-controls).

## Platform considerations

*No additional considerations for macOS, tvOS, or watchOS.*

### Mobile (iOS, iPadOS)

In iOS and iPadOS, a menu can display items in one of the following three layouts.

- **Small.** A row of four items appears at the top of the menu, above a list that contains the remaining items. For each item in the top row, the menu displays a symbol or icon, but no label.
- **Medium.** A row of three items appears at the top of the menu, above a list that contains the remaining items. For each item in the top row, the menu displays a symbol or icon above a short label.
- **Large (the default).** The menu displays all items in a list.

For developer guidance, see [preferredElementSize](https://developer.apple.com/documentation/uikit/uimenu/preferredelementsize).

**Choose a small or medium menu layout when it can help streamline people’s choices.** Consider using the medium layout if your app has three important actions that people often want to perform. For example, Notes uses the medium layout to give people a quick way to perform the Scan, Lock, and Pin actions. Use the small layout only for closely related actions that typically appear as a group, such as Bold, Italic, Underline, and Strikethrough. For each action, use a recognizable symbol that helps people identify the action without a label.

## Change log

| Date | Changes |
| --- | --- |
| June 8, 2026 | Updated guidance for menu item icons. |
| December 16, 2025 | Added guidance for presenting menus with breakthrough effects in visionOS. |
| July 28, 2025 | Added guidance for representing menu items with icons. |
| June 10, 2024 | Added guidance for in-game menus and included game-specific examples. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Added guidelines for using the small, medium, and large menu layouts in iPadOS. |

## Related guidelines

- [Pop-up buttons](pop-up-buttons.md)
- [Pull-down buttons](pull-down-buttons.md)
- [Context menus](context-menus.md)
- [The menu bar](the-menu-bar.md)

---


<a id="pop-up-buttons"></a>
## pop-up-buttons

# Pop-up buttons

> Source: <https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons>
> Section: Components › Menus and actions
> Platforms covered: iOS, iPadOS, macOS (guidance specific to visionOS omitted)
> Last change on Apple's site: 2023-10-24 (Added artwork.)

A pop-up button displays a menu of mutually exclusive options.

---

After people choose an item from a pop-up button’s menu, the menu closes, and the button can update its content to indicate the current selection.

## Best practices

**Use a pop-up button to present a flat list of mutually exclusive options or states.** A pop-up button helps people make a choice that affects their content or the surrounding view. Use a [pull-down button](pull-down-buttons.md) instead if you need to:

- Offer a list of actions
- Let people select multiple items
- Include a submenu

**Provide a useful default selection.** A pop-up button can update its content to identify the current selection, but if people haven’t made a selection yet, it shows the default item you specify. When possible, make the default selection an item that most people are likely to want.

**Give people a way to predict a pop-up button’s options without opening it.** For example, you can use an introductory label or a button label that describes the button’s effect, giving context to the options.

**Consider using a pop-up button when space is limited and you don’t need to display all options all the time.** Pop-up buttons are a space-efficient way to present a wide array of choices.

**If necessary, include a Custom option in a pop-up button’s menu to provide additional items that are useful in some situations.** Offering a Custom option can help you avoid cluttering the interface with items or controls that people need only occasionally. You can also display explanatory text below the list to help people understand how the options work.

## Platform considerations

*No additional considerations for iOS, macOS, or visionOS. Not supported in tvOS or watchOS.*

### Tablet (iPadOS)

**Within a popover or modal view, consider using a pop-up button instead of a disclosure indicator to present multiple options for a list item.** For example, people can quickly choose an option from the pop-up button’s menu without navigating to a detail view. Consider using a pop-up button in this scenario when you have a fairly small, well-defined set of options that work well in a menu.

## Change log

| Date | Changes |
| --- | --- |
| October 24, 2023 | Added artwork. |
| September 14, 2022 | Added a guideline on using a pop-up button in a popover or modal view in iPadOS. |

## Related guidelines

- [Pull-down buttons](pull-down-buttons.md)
- [Buttons](buttons.md)
- [Menus](menus.md)

---


<a id="pull-down-buttons"></a>
## pull-down-buttons

# Pull-down buttons

> Source: <https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons>
> Section: Components › Menus and actions
> Platforms covered: iOS, iPadOS, macOS (guidance specific to visionOS omitted)

A pull-down button displays a menu of items or actions that directly relate to the button’s purpose.

---

After people choose an item in a pull-down button’s menu, the menu closes, and the app performs the chosen action.

## Best practices

**Use a pull-down button to present commands or items that are directly related to the button’s action.** The menu lets you help people clarify the button’s target or customize its behavior without requiring additional buttons in your interface. For example:

- An Add button could present a menu that lets people specify the item they want to add.
- A Sort button could use a menu to let people select an attribute on which to sort.
- A Back button could let people choose a specific location to revisit instead of opening the previous one.

If you need to provide a list of mutually exclusive choices that aren’t commands, use a [pop-up button](pop-up-buttons.md) instead.

**Avoid putting all of a view’s actions in one pull-down button.** A view’s primary actions need to be easily discoverable, so you don’t want to hide them in a pull-down button that people have to open before they can do anything.

**Balance menu length with ease of use.** Because people have to interact with a pull-down button before they can view its menu, listing a minimum of three items can help the interaction feel worthwhile. If you need to list only one or two items, consider using alternative components to present them, such as buttons to perform actions and toggles or switches to present selections. In contrast, listing too many items in a pull-down button’s menu can slow people down because it takes longer to find a specific item.

**Display a succinct menu title only if it adds meaning.** In general, a pull-down button’s content — combined with descriptive menu items — provides all the context people need, making a menu title unnecessary.

**Let people know when a pull-down button’s menu item is destructive, and ask them to confirm their intent.** Menus use red text to highlight actions that you identify as potentially destructive. When people choose a destructive action, the system displays an [action sheet](action-sheets.md) (iOS) or [popover](popovers.md) (iPadOS) in which they can confirm their choice or cancel the action. Because an action sheet appears in a different location from the menu and requires deliberate dismissal, it can help people avoid losing data by mistake.

**Include an interface icon with a menu item when it provides value.** If you need to clarify an item’s meaning, you can display an [icon](icons.md) or image after its label. Using [SF Symbols](sf-symbols.md) for this purpose can help you provide a familiar experience while ensuring that the symbol remains aligned with the text at every scale.

## Platform considerations

*No additional considerations for macOS or visionOS. Not supported in tvOS or watchOS.*

### Mobile (iOS, iPadOS)

> **Note:** You can also let people reveal a pull-down menu by performing a specific gesture on a button. For example, in iOS 14 and later, Safari responds to a touch and hold gesture on the Tabs button by displaying a menu of tab-related actions, like New Tab and Close All Tabs.

**Consider using a More pull-down button to present items that don’t need prominent positions in the main interface.** A More button can help you offer a range of items where space is constrained, but it can also hinder discoverability. Although people generally understand that a More button offers additional functionality related to the current context, the ellipsis icon doesn’t necessarily help them predict its contents. To design an effective More button, weigh the convenience of its size against its impact on discoverability to find a balance that works in your app.

## Change log

| Date | Changes |
| --- | --- |
| September 14, 2022 | Refined guidance on designing a useful menu length. |

## Related guidelines

- [Pop-up buttons](pop-up-buttons.md)
- [Buttons](buttons.md)
- [Menus](menus.md)

---


<a id="the-menu-bar"></a>
## the-menu-bar

# The menu bar

> Source: <https://developer.apple.com/design/human-interface-guidelines/the-menu-bar>
> Section: Components › Menus and actions
> Platforms covered: iPadOS, macOS
> Last change on Apple's site: 2025-06-09 (Added guidance for the menu bar in iPadOS.)

On a Mac or an iPad, the menu bar at the top of the screen displays the top-level menus in your app or game.

---

Mac users are very familiar with the macOS menu bar, and they rely on it to help them learn what an app does and find the commands they need. To help your app or game feel at home in macOS, it’s essential to provide a consistent menu bar experience.

Menu bar menus on iPad are similar to those on Mac, appearing in the same order and with familiar sets of menu items. When you adopt the menu structure that people expect from their experience on Mac, it helps them immediately understand and take advantage of the menu bar on iPad as well.

Keyboard shortcuts in iPadOS use the same patterns as in macOS. For guidance, see [Standard keyboard shortcuts](keyboards.md#standard-keyboard-shortcuts).

Menus in the menu bar share most of the appearance and behavior characteristics that all menu types have. To learn about menus in general — and how to organize and label menu items — see [Menus](menus.md).

## Anatomy

When present in the menu bar, the following menus appear in the order listed below.

- *YourAppName* (you supply a short version of your app’s name for this menu’s title)
- File
- Edit
- Format
- View
- App-specific menus, if any
- Window
- Help

In addition, the macOS menu bar includes the Apple menu on the leading side and menu bar extras on the trailing side. See [macOS Platform considerations](#desktop-macos) for guidance.

## Best practices

**Support the default system-defined menus and their ordering.** People expect to find menus and menu items in an order they’re familiar with. In many cases, the system implements the functionality of standard menu items so you don’t have to. For example, when people select text in a standard text field, the system makes the Edit > Copy menu item available.

**Always show the same set of menu items.** Keeping menu items visible helps people learn what actions your app supports, even if they’re unavailable in the current context. If a menu bar item isn’t actionable, disable the action instead of hiding it from the menu.

**Represent menu item actions with familiar icons.** Icons help people recognize common actions throughout your app. Use the same icons as the system to represent actions such as Copy, Share, and Delete, wherever they appear. For a list of icons that represent common actions, see [Standard icons](icons.md#standard-icons). For additional guidance, see [Menus](menus.md).

**Support the keyboard shortcuts defined for the standard menu items you include.** People expect to use the keyboard shortcuts they already know for standard menu items, like Copy, Cut, Paste, Save, and Print. Define custom keyboard shortcuts only when necessary. For guidance, see [Standard keyboard shortcuts](keyboards.md#standard-keyboard-shortcuts).

**Prefer short, one-word menu titles.** Various factors — like different display sizes and the presence of menu bar extras — can affect the spacing and appearance of your menus. One-word menu titles work especially well in the menu bar because they take little space and are easy for people to scan. If you need to use more than one word in the menu title, use title-style capitalization.

## App menu

The app menu lists items that apply to your app or game as a whole, rather than to a specific task, document, or window. To help people quickly identify the active app, the menu bar displays your app name in bold.

The app menu typically contains the following menu items listed in the following order.

| Menu item | Action | Guidance |
| --- | --- | --- |
| About *YourAppName* | Displays the About window for your app, which includes copyright and version information. | Prefer a short name of 16 characters or fewer. Don’t include a version number. |
| Settings… | Opens your [settings](settings.md) window, or your app’s page in iPadOS Settings. | Use only for app-level settings. If you also offer document-specific settings, put them in the File menu. |
| Optional app-specific items | Performs custom app-level setting or configuration actions. | List custom app-configuration items after the Settings item and within the same group. |
| Services (macOS only) | Displays a submenu of services from the system and other apps that apply to the current context. |  |
| Hide *YourAppName* (macOS only) | Hides your app and all of its windows, and then activates the most recently used app. | Use the same short app name you supply for the About item. |
| Hide Others (macOS only) | Hides all other open apps and their windows. |  |
| Show All (macOS only) | Shows all other open apps and their windows behind your app’s windows. |  |
| Quit *YourAppName* | Quits your app. Pressing Option changes Quit *YourAppName* to Quit and Keep Windows. | Use the same short app name you supply for the About item. |

**Display the About menu item first.** Include a separator after the About menu item so that it appears by itself in a group.

## File menu

The File menu contains commands that help people manage the files or documents an app supports. If your app doesn’t handle any types of files, you can rename or eliminate this menu.

The File menu typically contains the following menu items listed in the following order.

| Menu item | Action | Guidance |
| --- | --- | --- |
| New *Item* | Creates a new document, file, or window. | For *Item*, use a term that names the type of item your app creates. For example, Calendar uses *Event* and *Calendar*. |
| Open | Can open the selected item or present an interface in which people select an item to open. | If people need to select an item in a separate interface, an ellipsis follows the command to indicate that more input is required. |
| Open Recent | Displays a submenu that lists recently opened documents and files that people can select, and typically includes a *Clear Menu* item. | List document and filenames that people recognize in the submenu; don’t display file paths. List the documents in the order people last opened them, with the most recently opened document first. |
| Close | Closes the current window or document. Pressing Option changes Close to Close All. For a tab-based window, Close Tab replaces Close. | In a tab-based window, consider adding a Close Window item to let people close the entire window with one click or tap. |
| Close Tab | Closes the current tab in a tab-based window. Pressing Option changes Close Tab to Close Other Tabs. |  |
| Close File | Closes the current file and all its associated windows. | Consider supporting this menu item if your app can open multiple views of the same file. |
| Save | Saves the current document or file. | Automatically save changes periodically as people work so they don’t need to keep choosing File > Save. For a new document, prompt people for a name and location. If you need to let people save a file in multiple formats, prefer a pop-up menu that lets people choose a format in the Save sheet. |
| Save All | Saves all open documents. |  |
| Duplicate | Duplicates the current document, leaving both documents open. Pressing Option changes Duplicate to Save As. | Prefer Duplicate to menu items like Save As, Export, Copy To, and Save To because these items don’t clarify the relationship between the original file and the new one. |
| Rename… | Lets people change the name of the current document. |  |
| Move To… | Prompts people to choose a new location for the document. |  |
| Export As… | Prompts people for a name, output location, and export file format. After exporting the file, the current document remains open; the exported file doesn’t open. | Reserve the Export As item for when you need to let people export content in a format your app doesn’t typically handle. |
| Revert To | When people turn on autosaving, displays a submenu that lists recent document versions and an option to display the version browser. After people choose a version to restore, it replaces the current document. |  |
| Page Setup… | Opens a panel for specifying printing parameters like paper size and printing orientation. A document can save the printing parameters that people specify. | Include the Page Setup item if you need to support printing parameters that apply to a specific document. Parameters that are global in nature, like a printer’s name, or that people change frequently, like the number of copies to print, belong in the Print panel. |
| Print… | Opens the standard Print panel, which lets people print to a printer, send a fax, or save as a PDF. |  |

## Edit menu

The Edit menu lets people make changes to content in the current document or text container, and provides commands for interacting with the Clipboard. Because many editing commands apply to any editable content, the Edit menu is useful even in apps that aren’t document-based.

**Determine whether Find menu items belong in the Edit menu.** For example, if your app lets people search for files or other types of objects, Find menu items might be more appropriate in the File menu.

The Edit menu typically contains the following top-level menu items, listed in the following order.

| Menu item | Action | Guidance |
| --- | --- | --- |
| Undo | Reverses the effect of the previous user operation. | Clarify the target of the undo. For example, if people just selected a menu item, you can append the item’s title, such as Undo Paste and Match Style. For a text entry operation, you might append the word *Typing* to give Undo Typing. |
| Redo | Reverses the effect of the previous Undo operation. | Clarify the target of the redo. For example, if people just reversed a menu item selection, you can append the item’s title, such as Redo Paste and Match Style. For a text entry operation, you might append the word *Typing* to give Redo Typing. |
| Cut | Removes the selected data and stores it on the Clipboard, replacing the previous contents of the Clipboard. |  |
| Copy | Duplicates the selected data and stores it on the Clipboard. |  |
| Paste | Inserts the contents of the Clipboard at the current insertion point. The Clipboard contents remain unchanged, permitting people to choose Paste multiple times. |  |
| Paste and Match Style | Inserts the contents of the Clipboard at the current insertion point, matching the style of the inserted text to the surrounding text. |  |
| Delete | Removes the selected data, but doesn’t place it on the Clipboard. | Provide a Delete menu item instead of an Erase or Clear menu item. Choosing Delete is the equivalent of pressing the Delete key, so it’s important for the naming to be consistent. |
| Select All | Highlights all selectable content in the current document or text container. |  |
| Find | Displays a submenu containing menu items for performing search operations in the current document or text container. Standard submenus include: Find, Find and Replace, Find Next, Find Previous, Use Selection for Find, and Jump to Selection. |  |
| Spelling and Grammar | Displays a submenu containing menu items for checking for and correcting spelling and grammar in the current document or text container. Standard submenus include: Show Spelling and Grammar, Check Document Now, Check Spelling While Typing, Check Grammar With Spelling, and Correct Spelling Automatically. |  |
| Substitutions | Displays a submenu containing items that let people toggle automatic substitutions while they type in a document or text container. Standard submenus include: Show Substitutions, Smart Copy/Paste, Smart Quotes, Smart Dashes, Smart Links, Data Detectors, and Text Replacement. |  |
| Transformations | Displays a submenu containing items that transform selected text. Standard submenus include: Make Uppercase, Make Lowercase, and Capitalize. |  |
| Speech | Displays a submenu containing Start Speaking and Stop Speaking items, which control when the system audibly reads selected text. |  |
| Start Dictation | Opens the dictation window and converts spoken words into text that’s added at the current insertion point. The system automatically adds the Start Dictation menu item at the bottom of the Edit menu. |  |
| Emoji & Symbols | Displays a Character Viewer, which includes emoji, symbols, and other characters people can insert at the current insertion point. The system automatically adds the Emoji & Symbols menu item at the bottom of the Edit menu. |  |

## Format menu

The Format menu lets people adjust text formatting attributes in the current document or text container. You can exclude this menu if your app doesn’t support formatted text editing.

The Format menu typically contains the following top-level menu items, listed in the following order.

| Menu item | Action |
| --- | --- |
| Font | Displays a submenu containing items for adjusting font attributes of the selected text. Standard submenus include: Show Fonts, Bold, Italic, Underline, Bigger, Smaller, Show Colors, Copy Style, and Paste Style. |
| Text | Displays a submenu containing items for adjusting text attributes of the selected text. Standard submenus include: Align Left, Align Center, Justify, Align Right, Writing Direction, Show Ruler, Copy Ruler, and Paste Ruler. |

## View menu

The View menu lets people customize the appearance of all an app’s windows, regardless of type.

> **Important:** The View menu doesn’t include items for navigating between or managing specific windows; the [Window menu](#window-menu) provides these commands.

**Provide a View menu even if your app supports only a subset of the standard view functions.** For example, if your app doesn’t include a tab bar, toolbar, or sidebar, but does support full-screen mode, provide a View menu that includes only the Enter/Exit Full Screen menu item.

**Ensure that each show/hide item title reflects the current state of the corresponding view.** For example, when the toolbar is hidden, provide a Show Toolbar menu item; when the toolbar is visible, provide a Hide Toolbar menu item.

The View menu typically contains the following top-level menu items, listed in the following order.

| Menu item | Action |
| --- | --- |
| Show/Hide Tab Bar | Toggles the visibility of the [tab bar](tab-bars.md) above the body area in a tab-based window |
| Show All Tabs/Exit Tab Overview | Enters and exits a view (similar to Mission Control) that provides an overview of all open tabs in a tab-based window |
| Show/Hide Toolbar | In a window that includes a [toolbar](toolbars.md), toggles the toolbar’s visibility |
| Customize Toolbar | In a window that includes a toolbar, opens a view that lets people customize toolbar items |
| Show/Hide Sidebar | In a window that includes a [sidebar](sidebars.md), toggles the sidebar’s visibility |
| Enter/Exit Full Screen | In an app that supports a [full-screen experience](going-full-screen.md), opens the window at full-screen size in a new space |

## App-specific menus

Your app’s custom menus appear in the menu bar between the View menu and the Window menu. For example, Safari’s menu bar includes app-specific History and Bookmarks menus.

**Provide app-specific menus for custom commands.** People look in the menu bar when searching for app-specific commands, especially when using an app for the first time. Even when commands are available elsewhere in your app, it’s important to list them in the menu bar. Putting commands in the menu bar makes them easier for people to find, lets you assign keyboard shortcuts to them, and makes them more accessible to people using Full Keyboard Access. Excluding commands from the menu bar — even infrequently used or advanced commands — risks making them difficult for everyone to find.

**As much as possible, reflect your app’s hierarchy in app-specific menus.** For example, Mail lists the Mailbox, Message, and Format menus in an order that mirrors the relationships of these items: mailboxes contain messages, and messages contain formatting.

**Aim to list app-specific menus in order from most to least general or commonly used.** People tend to expect menus in the leading end of a list to be more specialized than menus in the trailing end.

## Window menu

The Window menu lets people navigate, organize, and manage an app’s windows.

> **Important:** The Window menu doesn’t help people customize the appearance of windows or close them. To customize a window, people use commands in the [View menu](#view-menu); to close a window, people choose Close in the [File menu](#file-menu).

**Provide a Window menu even if your app has only one window.** Include the Minimize and Zoom menu items so people using Full Keyboard Access can use the keyboard to invoke these functions.

**Consider including menu items for showing and hiding panels.** A [panel](panels.md) provides information, configuration options, or tools for interacting with content in a primary window, and typically appears only when people need it. There’s no need to provide access to the font panel or text color panel because the Format menu lists these panels.

The Window menu typically contains the following top-level menu items, listed in the following order.

| Menu item | Action | Guidance |
| --- | --- | --- |
| Minimize | Minimizes the active window to the Dock. Pressing the Option key changes this item to Minimize All. |  |
| Zoom | Toggles between a predefined size appropriate to the window’s content and the window size people set. Pressing the Option key changes this item to Zoom All. | Avoid using Zoom to enter or exit full-screen mode. The [View menu](#view-menu) supports these functions. |
| Show Previous Tab | Shows the tab before the current tab in a tab-based window. |  |
| Show Next Tab | Shows the tab after the current tab in a tab-based window. |  |
| Move Tab to New Window | Opens the current tab in a new window. |  |
| Merge All Windows | Combines all open windows into a single tabbed window. |  |
| Enter/Exit Full Screen | In an app that supports a [full-screen experience](going-full-screen.md), opens the window at full-screen size in a new space. | Include this item in the Window menu only if your app doesn’t have a View menu. In this scenario, continue to provide separate Minimize and Zoom menu items. |
| Bring All to Front | Brings all an app’s open windows to the front, maintaining their onscreen location, size, and layering order. (Clicking the app icon in the Dock has the same effect.) Pressing the Option key changes this item to Arrange in Front, which brings an app’s windows to the front in a neatly tiled arrangement. |  |
| *Name of an open app-specific window* | Brings the selected window to the front. | List the currently open windows in alphabetical order for easy scanning. Avoid listing panels or other modal views. |

## Help menu

The Help menu — located at the trailing end of the menu bar — provides access to an app’s help documentation. When you use the Help Book format for this documentation, macOS automatically includes a search field at the top of the Help menu.

| Menu item | Action | Guidance |
| --- | --- | --- |
| Send *YourAppName* Feedback to Apple | Opens the Feedback Assistant, in which people can provide feedback. |  |
| *YourAppName* Help | When the content uses the Help Book format, opens the content in the built-in Help Viewer. |  |
| *Additional Item* |  | Use a separator between your primary help documentation and additional items, which might include registration information or release notes. Keep the total the number of items you list in the Help menu small to avoid overwhelming people with too many choices when they need help. Alternatively, consider linking to additional items from within your help documentation. |

For guidance, see [Offering help](offering-help.md); for developer guidance, see [NSHelpManager](https://developer.apple.com/documentation/appkit/nshelpmanager).

## Dynamic menu items

In rare cases, it can make sense to present a *dynamic menu item*, which is a menu item that changes its behavior when people choose it while pressing a modifier key (Control, Option, Shift, or Command). For example, the *Minimize* item in the Window menu changes to *Minimize All* when people press the Option key.

**Avoid making a dynamic menu item the only way to accomplish a task.** Dynamic menu items are hidden by default, so they’re best suited to offer shortcuts to advanced actions that people can accomplish in other ways. For example, if someone hasn’t discovered the *Minimize All* dynamic menu item in the Window menu, they can still minimize each open window.

**Use dynamic menu items primarily in menu bar menus.** Adding a dynamic menu item to contextual or Dock menus can make the item even harder for people to discover.

**Require only a single modifier key to reveal a dynamic menu item.** It can be physically awkward to press more than one key while simultaneously opening a menu and choosing a menu item, in addition to reducing the discoverability of the dynamic behavior. For developer guidance, see [isAlternate](https://developer.apple.com/documentation/appkit/nsmenuitem/isalternate).

> **Tip:** macOS automatically sets the width of a menu to hold the widest item, including dynamic menu items.

## Platform considerations

*Not supported in iOS, tvOS, visionOS, or watchOS.*

### Tablet (iPadOS)

The menu bar displays the top-level menus for your app or game, including both system-provided menus and any custom ones you choose to add. People reveal the menu bar by moving the pointer to the top edge of the screen, or swiping down from it. When visible, the menu bar occupies the same vertical space as the [status bar](status-bars.md) at the top edge of the screen.

As with the macOS menu bar, the iPadOS menu bar provides a familiar way for people to learn what an app does, find the commands they need, and discover keyboard shortcuts.  While they are similar in most respects, there are a few key differences between the menu bars on each platform.

|  | iPadOS | macOS |
| --- | --- | --- |
| Menu bar visibility | Hidden until revealed | Visible by default |
| Horizontal alignment | Centered | Leading side |
| Menu bar extras | Not available | System default and custom |
| Window controls | In the menu bar when the app is full screen | Never in the menu bar |
| Apple menu | Not available | Always available |
| App menu | About, Services, and app visibility-related items not available | Always available |

**Because the menu bar is often hidden when running an app full screen, ensure that people can access all of your app’s functions through its UI.**  In particular, always offer other ways to accomplish tasks assigned to dynamic menu items, since these are only available when a hardware keyboard is connected. Avoid using the menu bar as a catch-all location for functionality that doesn’t fit in elsewhere.

**Reserve the YourAppName > Settings menu item for opening your app’s page in iPadOS Settings.** If your app includes its own internal preferences area, link to it with a separate menu item beneath Settings in the same group. Place any other custom app-wide configuration options in this section as well.

**For apps with tab-style navigation, consider adding each tab as a menu item in the View menu.** Since each tab is a different view of the app, the View menu is a natural place to offer an additional way to navigate between tabs. If you do this, consider assigning key bindings to each tab to make navigation even more convenient.

**Consider grouping menu items into submenus to conserve vertical space.** Menu item rows on iPad use more space than on Mac to make them easier to tap. Because of this, and the smaller screen sizes of some iPads, it can be helpful to group related items into submenus more frequently than in the menu bar on Mac.

### Desktop (macOS)

The menu bar in macOS includes the Apple menu, which is always the first item on the leading side of the menu bar. The Apple menu includes system-defined menu items that are always available, and you can’t modify or remove it. Space permitting, the system can also display menu bar extras in the trailing end of the menu bar. For guidance, see [Menu bar extras](#menu-bar-extras).

When menu bar space is constrained, the system prioritizes the display of menus and essential menu bar extras. To ensure that menus remain readable, the system may decrease the space between the titles, truncating them if necessary.

When people enter full-screen mode, the menu bar typically hides until they reveal it by moving the pointer to the top of the screen. For guidance, see [Going full screen](going-full-screen.md).

#### Menu bar extras

A menu bar extra exposes app-specific functionality using an icon that appears in the menu bar when your app is running, even when it’s not the frontmost app. Menu bar extras are on the opposite side of the menu bar from your app’s menus. For developer guidance, see [MenuBarExtra](https://developer.apple.com/documentation/swiftui/menubarextra).

When necessary, the system hides menu bar extras to make room for app menus. Similarly, if there are too many menu bar extras, the system may hide some to avoid crowding app menus.

**Consider using a symbol to represent your menu bar extra.** You can create an [icon](icons.md) or you can choose one of the [SF Symbols](sf-symbols.md), using it as-is or customizing it to suit your needs. Both interface icons and symbols use black and clear colors to define their shapes; the system can apply other colors to the black areas in each image so it looks good on both dark and light menu bars, and when your menu bar extra is selected. The menu bar’s height is 24 pt.

**Display a menu — not a popover — when people click your menu bar extra.** Unless the app functionality you want to expose is too complex for a menu, avoid presenting it in a [popover](popovers.md).

**Let people — not your app — decide whether to put your menu bar extra in the menu bar.** Typically, people add a menu bar extra to the menu bar by changing a setting in an app’s settings window. To ensure discoverability, however, consider giving people the option of doing so during setup.

**Avoid relying on the presence of menu bar extras.** The system hides and shows menu bar extras regularly, and you can’t be sure which other menu bar extras people have chosen to display or predict the location of your menu bar extra.

**Consider exposing app-specific functionality in other ways, too.** For example, you can provide a [Dock menu](dock-menus.md) that appears when people Control-click your app’s Dock icon. People can hide or choose not to use your menu bar extra, but a Dock menu is aways available when your app is running.

## Change log

| Date | Changes |
| --- | --- |
| June 9, 2025 | Added guidance for the menu bar in iPadOS. |

## Related guidelines

- [Menus](menus.md)
- [Dock menus](dock-menus.md)

---


<a id="toolbars"></a>
## toolbars

# Toolbars

> Source: <https://developer.apple.com/design/human-interface-guidelines/toolbars>
> Section: Components › Menus and actions
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-12-16 (Updated guidance for Liquid Glass.)

A toolbar provides convenient access to frequently used commands, controls, navigation, and search.

---

A toolbar consists of one or more sets of controls arranged horizontally along the top or bottom edge of the view, grouped into logical sections.

Toolbars act on content in the view, facilitate navigation, and help orient people in the app. They include three types of content:

- The title of the current view
- Navigation controls, like back and forward, and [search fields](search-fields.md)
- Actions, or bar items, like [buttons](buttons.md) and [menus](menus.md)

In contrast to a toolbar, a [tab bar](tab-bars.md) is specifically for navigating between areas of an app.

## Best practices

**Choose items deliberately to avoid overcrowding.** People need to be able to distinguish and activate each item, so you don’t want to put too many items in the toolbar. To accommodate variable view widths, define which items move to the overflow menu as the toolbar becomes narrower.

> **Note:** The system automatically adds an overflow menu in macOS or iPadOS when items no longer fit. Don’t add an overflow menu manually, and avoid layouts that cause toolbar items to overflow by default.

**Add a More menu to contain additional actions.** Prioritize less important actions for inclusion in the More menu. Try to include all actions in the toolbar if possible, and only add this menu if you really need it.

*Illustrated: Standard, Compact.*

**In iPadOS and macOS apps, consider letting people customize the toolbar to include their most common items.** Toolbar customization is especially useful in apps that provide a lot of items — or that include advanced functionality that not everyone needs — and in apps that people tend to use for long periods of time. For example, it works well to make a range of editing actions available for toolbar customization, because people often use different types of editing commands based on their work style and their current project.

**Reduce the use of toolbar backgrounds and tinted controls.** Any custom backgrounds and appearances you use might overlay or interfere with background effects that the system provides. Instead, use the content layer to inform the color and appearance of the toolbar, and use a [ScrollEdgeEffectStyle](https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle) when necessary to distinguish the toolbar area from the content area. This approach helps your app express its unique personality without distracting from content.

**Avoid applying a similar color to toolbar item labels and content layer backgrounds.** If your app already has bright, colorful content in the content layer, prefer using the default monochromatic appearance of toolbars. For more guidance, see [Liquid Glass color](color.md#liquid-glass-color).

**Prefer using standard components in a toolbar.** By default, standard buttons, text fields, headers, and footers have corner radii that are concentric with bar corners. If you need to create a custom component, ensure that its corner radius is also concentric with the bar’s corners.

**Consider temporarily hiding toolbars for a distraction-free experience.** Sometimes people appreciate a minimal interface to reduce distractions or reveal more content. If you support this, do so contextually when it makes the most sense, and offer ways to reliably restore hidden interface elements. For guidance, see [Going full screen](going-full-screen.md). For guidance specific to visionOS, see Immersive experiences.

## Titles

**Provide a useful title for each window.** A title helps people confirm their location as they navigate your app, and differentiates between the content of multiple open windows. If titling a toolbar seems redundant, you can leave the title area empty. For example, Notes doesn’t title the current note when a single window is open, because the first line of content typically supplies sufficient context. However, when opening notes in separate windows, the system titles them with the first line of content so people can tell them apart.

**Don’t title windows with your app name.** Your app’s name doesn’t provide useful information about your content hierarchy or any window or area in your app, so it doesn’t work well as a title.

**Write a concise title.** Aim for a word or short phrase that distills the purpose of the window or view, and keep the title under 15 characters long so you leave enough room for other controls.

## Navigation

A toolbar with navigation controls appears at the top of a window, helping people move through a hierarchy of content. A toolbar also often contains a [search field](search-fields.md) for quick navigation between areas or pieces of content. In iOS, a navigation-specific toolbar is sometimes called a navigation bar.

**Use the standard Back and Close buttons.** People know that the standard Back button lets them retrace their steps through a hierarchy of information, and the standard Close button closes a modal view. Prefer the standard symbols for each, and don’t use a text label that says *Back* or *Close*. If you create a custom version of either, make sure it still looks the same, behaves as people expect, and matches the rest of your interface, and ensure you consistently implement it throughout your app or game. For guidance, see [Icons](icons.md).

## Actions

**Provide actions that support the main tasks people perform.** In general, prioritize the commands that people are most likely to want. These commands are often the ones people use most frequently, but in some apps it might make sense to prioritize commands that map to the highest level or most important objects people work with.

**Make sure the meaning of each control is clear.** Don’t make people guess or experiment to figure out what a toolbar item does. Prefer simple, recognizable symbols for items instead of text, except for actions like *edit* that aren’t well-represented by symbols. For guidance on symbols that represent common actions, see [Standard icons](icons.md#standard-icons).

**Prefer system-provided symbols without borders.** System-provided symbols are familiar, automatically receive appropriate coloring and vibrancy, and respond consistently to user interactions. Borders (like outlined circle symbols) aren’t necessary because the section provides a visible container, and the system defines hover and selection state appearances automatically. For guidance, see [SF Symbols](sf-symbols.md).

**Use the `.prominent` style for key actions such as Done or Submit.** This separates and tints the action so there’s a clear focal point. Only specify one primary action, and put it on the trailing side of the toolbar.

## Item groupings

You can position toolbar items in three locations: the leading edge, center area, and trailing edge of the toolbar. These areas provide familiar homes for navigation controls, window or document titles, common actions, and search.

- **Leading edge.** Elements that let people return to the previous document and show or hide a sidebar appear at the far leading edge, followed by the view title. Next to the title, the toolbar can include a document menu that contains standard and app-specific commands that affect the document as a whole, such as Duplicate, Rename, Move, and Export. To ensure that these items are always available, items on the toolbar’s leading edge aren’t customizable.
- **Center area.** Common, useful controls appear in the center area, and the view title can appear here if it’s not on the leading edge. In macOS and iPadOS, people can add, remove, and rearrange items here if you let them customize the toolbar, and items in this section automatically collapse into the system-managed overflow menu when the window shrinks enough in size.
- **Trailing edge.** The trailing edge contains important items that need to remain available, buttons that open nearby inspectors, an optional search field, and the More menu that contains additional items and supports toolbar customization. It also includes a primary action like Done when one exists. Items on the trailing edge remain visible at all window sizes.

To position items in the groupings you want, pin them to the leading edge, center, or trailing edge, and insert space between buttons or other items where appropriate.

**Group toolbar items logically by function and frequency of use.**  For example, Keynote includes several sections that are based on functionality, including one for presentation-level commands, one for playback commands, and one for object insertion.

**Group navigation controls and critical actions like Done, Close, or Save in dedicated, familiar, and visually distinct sections.** This reflects their importance and helps people discover and understand these actions.

**Keep consistent groupings and placement across platforms.** This helps people develop familiarity with your app and trust that it behaves similarly regardless of where they use it.

**Minimize the number of groups.** Too many groups of controls can make a toolbar feel cluttered and confusing, even with the added space on iPad and Mac. In general, aim for a maximum of three.

**Keep actions with text labels separate.** Placing an action with a text label next to an action with a symbol can create the illusion of a single action with a combined text and symbol, leading to confusion and misinterpretation. If your toolbar includes multiple text-labeled buttons, the text of those buttons may appear to run together, making the buttons indistinguishable. Add separation by inserting fixed space between the buttons. For developer guidance, see [UIBarButtonItem.SystemItem.fixedSpace](https://developer.apple.com/documentation/uikit/uibarbuttonitem/systemitem/fixedspace).

## Platform considerations

### Phone (iOS)

**Prioritize only the most important items for inclusion in the main toolbar area.** Because space is so limited, carefully consider which actions are essential to your app and include those first. Create a More menu to include additional items.

**Use a large title to help people stay oriented as they navigate and scroll.** By default, a large title transitions to a standard title as people begin scrolling the content, and transitions back to large when people scroll to the top, reminding them of their current location. For developer guidance, see [prefersLargeTitles](https://developer.apple.com/documentation/uikit/uinavigationbar/preferslargetitles).

### Tablet (iPadOS)

**Consider combining a toolbar with a tab bar.** In iPadOS, a toolbar and a [tab bar](tab-bars.md) can coexist in the same horizontal space at the top of the view. This is particularly useful for layouts where you want to navigate between a few main app areas while keeping the full width of the window available for content. For guidance, see [Layout](layout.md) and [Windows](windows.md).

### Desktop (macOS)

In a macOS app, the toolbar resides in the frame at the top of a window, either below or integrated with the title bar. Note that window titles can display inline with controls, and toolbar items don’t include a bezel.

**Make every toolbar item available as a command in the menu bar.** Because people can customize the toolbar or hide it, it can’t be the only place that presents a command. In contrast, it doesn’t make sense to provide a toolbar item for every menu item, because not all menu commands are important enough or used often enough to warrant space in the toolbar.

## Change log

| Date | Changes |
| --- | --- |
| December 16, 2025 | Updated guidance for Liquid Glass. |
| June 9, 2025 | Added guidance for grouping bar items, updated guidance for using symbols, and incorporated navigation bar guidance. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance for using toolbars in watchOS. |

## Related guidelines

- [Sidebars](sidebars.md)
- [Tab bars](tab-bars.md)
- [Layout](layout.md)
- [Buttons](buttons.md)
- [Search fields](search-fields.md)

---
