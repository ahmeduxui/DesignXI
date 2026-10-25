# Apple HIG — Components › Layout and organization
Bundled HIG pages for the “Components › Layout and organization” group. Each page kept verbatim under an anchor heading `## <slug>`. Cite as **components-layout-and-organization.md › <slug> › heading**.


<a id="boxes"></a>
## boxes

# Boxes

> Source: <https://developer.apple.com/design/human-interface-guidelines/boxes>
> Section: Components › Layout and organization
> Platforms covered: iOS, iPadOS, macOS (guidance specific to visionOS omitted)

A box creates a visually distinct group of logically related information and components.

---

By default, a box uses a visible border or background color to separate its contents from the rest of the interface. A box can also include a title.

## Best practices

**Prefer keeping a box relatively small in comparison with its containing view.** As a box’s size gets close to the size of the containing window or screen, it becomes less effective at communicating the separation of grouped content, and it can crowd other content.

**Consider using padding and alignment to communicate additional grouping within a box.** A box’s border is a distinct visual element — adding nested boxes to define subgroups can make your interface feel busy and constrained.

## Content

**Provide a succinct introductory title if it helps clarify the box’s contents.** The appearance of a box helps people understand that its contents are related, but it might make sense to provide more detail about the relationship. Also, a title can help VoiceOver users predict the content they encounter within the box.

**If you need a title, write a brief phrase that describes the contents.** Use sentence-style capitalization. Avoid ending punctuation unless you use a box in a settings pane, where you append a colon to the title.

## Platform considerations

### Mobile (iOS, iPadOS)

By default, iOS and iPadOS use the secondary and tertiary background [colors](color.md) in boxes.

### Desktop (macOS)

By default, macOS displays a box’s title above it.

## Related guidelines

- [Layout](layout.md)

---


<a id="collections"></a>
## collections

# Collections

> Source: <https://developer.apple.com/design/human-interface-guidelines/collections>
> Section: Components › Layout and organization
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS omitted)

A collection manages an ordered set of content and presents it in a customizable and highly visual layout.

---

Generally speaking, collections are ideal for showing image-based content.

## Best practices

**Use the standard row or grid layout whenever possible.** Collections display content by default in a horizontal row or a grid, which are simple, effective appearances that people expect. Avoid creating a custom layout that might confuse people or draw undue attention to itself.

**Consider using a table instead of a collection for text.** It’s generally simpler and more efficient to view and digest textual information when it’s displayed in a scrollable list.

**Make it easy to choose an item.** If it’s too difficult to get to an item in your collection, people will get frustrated and lose interest before reaching the content they want. Use adequate padding around images to keep focus or hover effects easy to see and prevent content from overlapping.

**Add custom interactions when necessary.** By default, people can tap to select, touch and hold to edit, and swipe to scroll. If your app requires it, you can add more gestures for performing custom actions.

**Consider using animations to provide feedback when people insert, delete, or reorder items.** Collections support standard animations for these actions, and you can also use custom animations.

## Platform considerations

*No additional considerations for macOS, tvOS, or visionOS. Not supported in watchOS.*

### Mobile (iOS, iPadOS)

**Use caution when making dynamic layout changes.** The layout of a collection can change dynamically. Be sure any changes make sense and are easy to track. If possible, try to avoid changing the layout while people are viewing and interacting with it, unless it’s in response to an explicit action.

## Related guidelines

- [Lists and tables](lists-and-tables.md)
- [Image views](image-views.md)
- [Layout](layout.md)

---


<a id="column-views"></a>
## column-views

# Column views

> Source: <https://developer.apple.com/design/human-interface-guidelines/column-views>
> Section: Components › Layout and organization
> Platforms covered: macOS

A column view — also called a *browser* — lets people view and navigate a data hierarchy using a series of vertical columns.

---

Each column represents one level of the hierarchy and contains horizontal rows of data items. Within a column, any parent item that contains nested child items is marked with a triangle icon. When people select a parent, the next column displays its children. People can continue navigating in this way until they reach an item with no children, and can also navigate back up the hierarchy to explore other branches of data.

> **Note:** If you need to manage the presentation of hierarchical content in your iPadOS or visionOS app, consider using a [split view](split-views.md).

## Best practices

Consider using a column view when you have a deep data hierarchy in which people tend to navigate back and forth frequently between levels, and you don’t need the sorting capabilities that a [list or table](lists-and-tables.md) provides. For example, Finder offers a column view (in addition to icon, list, and gallery views) for navigating directory structures.

**Show the root level of your data hierarchy in the first column.** People know they can quickly scroll back to the first column to begin navigating the hierarchy from the top again.

**Consider showing information about the selected item when there are no nested items to display.** The Finder, for example, shows a preview of the selected item and information like the creation date, modification date, file type, and size.

**Let people resize columns.** This is especially important if the names of some data items are too long to fit within the default column width.

## Platform considerations

*Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.*

## Related guidelines

- [Lists and tables](lists-and-tables.md)
- [Outline views](outline-views.md)
- [Split views](split-views.md)

---


<a id="disclosure-controls"></a>
## disclosure-controls

# Disclosure controls

> Source: <https://developer.apple.com/design/human-interface-guidelines/disclosure-controls>
> Section: Components › Layout and organization
> Platforms covered: iOS, iPadOS, macOS (guidance specific to visionOS omitted)

Disclosure controls reveal and hide information and functionality related to specific controls or views.

---

## Best practices

**Use a disclosure control to hide details until they’re relevant.** Place controls that people are most likely to use at the top of the disclosure hierarchy so they’re always visible, with more advanced functionality hidden by default. This organization helps people quickly find the most essential information without overwhelming them with too many detailed options.

## Disclosure triangles

A disclosure triangle shows and hides information and functionality associated with a view or a list of items. For example, Keynote uses a disclosure triangle to show advanced options when exporting a presentation, and the Finder uses disclosure triangles to progressively reveal hierarchy when navigating a folder structure in list view.

*Illustrated: Collapsed, Expanded.*

A disclosure triangle points inward from the leading edge when its content is hidden and down when its content is visible. Clicking or tapping the disclosure triangle switches between these two states, and the view expands or collapses accordingly to accommodate the content.

**Provide a descriptive label when using a disclosure triangle.** Make sure your labels indicate what is disclosed or hidden, like “Advanced Options.”

For developer guidance, see [NSButton.BezelStyle.disclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/disclosure).

## Disclosure buttons

A disclosure button shows and hides functionality associated with a specific control. For example, the macOS Save sheet shows a disclosure button next to the Save As text field. When people click or tap this button, the Save dialog expands to give advanced navigation options for selecting an output location for their document.

A disclosure button points down when its content is hidden and up when its content is visible. Clicking or tapping the disclosure button switches between these two states, and the view expands or collapses accordingly to accommodate the content.

*Illustrated: Collapsed, Expanded.*

**Place a disclosure button near the content that it shows and hides.** Establish a clear relationship between the control and the expanded choices that appear when a person clicks or taps a button.

**Use no more than one disclosure button in a single view.** Multiple disclosure buttons add complexity and can be confusing.

For developer guidance, see [NSButton.BezelStyle.pushDisclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/pushdisclosure).

## Platform considerations

*No additional considerations for macOS. Not supported in tvOS or watchOS.*

### Mobile (iOS, iPadOS, visionOS)

Disclosure controls are available in iOS, iPadOS, and visionOS with the SwiftUI [DisclosureGroup](https://developer.apple.com/documentation/swiftui/disclosuregroup) view.

## Related guidelines

- [Outline views](outline-views.md)
- [Lists and tables](lists-and-tables.md)
- [Buttons](buttons.md)

---


<a id="labels"></a>
## labels

# Labels

> Source: <https://developer.apple.com/design/human-interface-guidelines/labels>
> Section: Components › Layout and organization
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2023-06-05 (Updated guidance to reflect changes in watchOS 10.)

A label is a static piece of text that people can read and often copy, but not edit.

---

Labels display text throughout the interface, in buttons, menu items, and views, helping people understand the current context and what they can do next.

The term *label* refers to uneditable text that can appear in various places. For example:

- Within a button, a label generally conveys what the button does, such as Edit, Cancel, or Send.
- Within many lists, a label can describe each item, often accompanied by a symbol or an image.
- Within a view, a label might provide additional context by introducing a control or describing a common action or task that people can perform in the view.

> **Developer note:** To display uneditable text, SwiftUI defines two components: [Label](https://developer.apple.com/documentation/swiftui/label) and [Text](https://developer.apple.com/documentation/swiftui/text).

The guidance below can help you use a label to display text. In some cases, guidance for specific components — such as [action buttons](buttons.md), [menus](menus.md), and [lists and tables](lists-and-tables.md) — includes additional recommendations for using text.

## Best practices

**Use a label to display a small amount of text that people don’t need to edit.** If you need to let people edit a small amount of text, use a [text field](text-fields.md). If you need to display a large amount of text, and optionally let people edit it, use a [text view](text-views.md).

**Prefer system fonts.** A label can display plain or styled text, and it supports Dynamic Type (where available) by default. If you adjust the style of a label or use custom fonts, make sure the text remains legible.

**Use system-provided label colors to communicate relative importance.** The system defines four label colors that vary in appearance to help you give text different levels of visual importance. For additional guidance, see [Color](color.md).

| System color | Example usage | iOS, iPadOS, tvOS, visionOS | macOS |
| --- | --- | --- | --- |
| Label | Primary information | [label](https://developer.apple.com/documentation/uikit/uicolor/label) | [labelColor](https://developer.apple.com/documentation/appkit/nscolor/labelcolor) |
| Secondary label | A subheading or supplemental text | [secondaryLabel](https://developer.apple.com/documentation/uikit/uicolor/secondarylabel) | [secondaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/secondarylabelcolor) |
| Tertiary label | Text that describes an unavailable item or behavior | [tertiaryLabel](https://developer.apple.com/documentation/uikit/uicolor/tertiarylabel) | [tertiaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/tertiarylabelcolor) |
| Quaternary label | Watermark text | [quaternaryLabel](https://developer.apple.com/documentation/uikit/uicolor/quaternarylabel) | [quaternaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/quaternarylabelcolor) |

**Make useful label text selectable.** If a label contains useful information — like an error message, a location, or an IP address — consider letting people select and copy it for pasting elsewhere.

## Platform considerations

*No additional considerations for iOS, iPadOS, tvOS, or visionOS.*

### Desktop (macOS)

> **Developer note:** To display uneditable text in a label, use the [isEditable](https://developer.apple.com/documentation/appkit/nstextfield/iseditable) property of [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield).

## Change log

| Date | Changes |
| --- | --- |
| June 5, 2023 | Updated guidance to reflect changes in watchOS 10. |

## Related guidelines

- [Text fields](text-fields.md)
- [Text views](text-views.md)

---


<a id="lists-and-tables"></a>
## lists-and-tables

# Lists and tables

> Source: <https://developer.apple.com/design/human-interface-guidelines/lists-and-tables>
> Section: Components › Layout and organization
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2023-06-21 (Updated to include guidance for visionOS.)

Lists and tables present data in one or more columns of rows.

---

A table or list can represent data that’s organized in groups or hierarchies, and it can support user interactions like selecting, adding, deleting, and reordering. Apps and games in all platforms can use tables to present content and options; many apps use lists to express an overall information hierarchy and help people navigate it. For example, iOS Settings uses a hierarchy of lists to help people choose options, and several apps — such as Mail in iPadOS and macOS — use a table within a [split view](split-views.md).

Sometimes, people need to work with complex data in a multicolumn table or a spreadsheet. Apps that offer productivity tasks often use a table to represent various characteristics or attributes of the data in separate, sortable columns.

## Best practices

**Prefer displaying text in a list or table.** A table can include any type of content, but the row-based format is especially well suited to making text easy to scan and read. If you have items that vary widely in size — or you need to display a large number of images — consider using a [collection](collections.md) instead.

**Let people edit a table when it makes sense.** People appreciate being able to reorder a list, even if they can’t add or remove items. In iOS and iPadOS, people must enter an edit mode before they can select table items.

**Provide appropriate feedback when people select a list item.** The feedback can vary depending on whether selecting the item reveals a new view or toggles the item’s state. In general, a table that helps people navigate through a hierarchy persistently highlights the selected row to clarify the path people are taking. In contrast, a table that lists options often highlights a row only briefly before adding an image — such as a checkmark — indicating that the item is selected.

## Content

**Keep item text succinct so row content is comfortable to read.** Short, succinct text can help minimize truncation and wrapping, making text easier to read and scan. If each item consists of a large amount of text, consider alternatives that help you avoid displaying over-large table rows. For example, you could list item titles only, letting people choose an item to reveal its content in a detail view.

**Consider ways to preserve readability of text that might otherwise get clipped or truncated.** When a table is narrow — for example, if people can vary its width — you want content to remain recognizable and easy to read. Sometimes, an ellipsis in the middle of text can make an item easier to distinguish because it preserves both the beginning and the end of the content.

**Use descriptive column headings in a multicolumn table.** Use nouns or short noun phrases with [title-style capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64), and don’t add ending punctuation. If you don’t include a column heading in a single-column table view, use a label or a header to help people understand the context.

## Style

**Choose a table or list style that coordinates with your data and platform.** Some styles use visual details to help communicate grouping and hierarchy or to provide specific experiences. In iOS and iPadOS, for example, the grouped style uses headers, footers, and additional space to separate groups of data; the elliptical style available in watchOS makes items appear as if they’re rolling off a rounded surface as people scroll; and macOS defines a bordered style that uses alternating row backgrounds to help make large tables easier to use. For developer guidance, see [ListStyle](https://developer.apple.com/documentation/swiftui/liststyle).

**Choose a row style that fits the information you need to display.** For example, you might need to display a small image in the leading end of a row, followed by a brief explanatory label. Some platforms provide built-in row styles you can use to arrange content in list rows, such as the [UIListContentConfiguration](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct) API you can use to lay out content in a list’s rows, headers, and footers in iOS, iPadOS, and tvOS.

## Platform considerations

### Mobile (iOS, iPadOS, visionOS)

**Use an info button only to reveal more information about a row’s content.** An info button — called a *detail disclosure button* when it appears in a list row — doesn’t support navigation through a hierarchical table or list. If you need to let people drill into a list or table row’s subviews, use a disclosure indicator accessory control. For developer guidance, see [UITableViewCell.AccessoryType.disclosureIndicator](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/disclosureindicator).

**Avoid adding an index to a table that displays controls — like disclosure indicators — in the trailing ends of its rows.** An *index* typically consists of the letters in an alphabet, displayed vertically at the trailing side of a list. People can jump to a specific section in the list by choosing the index letter that maps to it. Because both the index and elements like disclosure indicators appear on the trailing side of a list, it can be difficult for people to use one element without activating the other.

### Desktop (macOS)

**When it provides value, let people click a column heading to sort a table view based on that column**. If people click the heading of a column that’s already sorted, re-sort the data in the opposite direction.

**Let people resize columns.** Data displayed in a table view often varies in width. People appreciate resizing columns to help them concentrate on different areas or reveal clipped data.

**Consider using alternating row colors in a multicolumn table.** Alternating colors can help people track row values across columns, especially in a wide table.

**Use an outline view instead of a table view to present hierarchical data.** An [outline view](outline-views.md) looks like a table view, but includes disclosure triangles for exposing nested levels of data. For example, an outline view might display folders and the items they contain.

## Change log

| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance to reflect changes in watchOS 10. |

## Related guidelines

- [Collections](collections.md)
- [Outline views](outline-views.md)
- [Layout](layout.md)

---


<a id="outline-views"></a>
## outline-views

# Outline views

> Source: <https://developer.apple.com/design/human-interface-guidelines/outline-views>
> Section: Components › Layout and organization
> Platforms covered: macOS

An outline view presents hierarchical data in a scrolling list of cells that are organized into columns and rows.

---

An outline view includes at least one column that contains primary hierarchical data, such as a set of parent containers and their children. You can add columns, as needed, to display attributes that supplement the primary data; for example, sizes and modification dates. Parent containers have disclosure triangles that expand to reveal their children.

Finder windows offer an outline view for navigating the file system.

## Best practices

Outline views work well to display text-based content and often appear in the leading side of a [split view](split-views.md), with related content on the opposite side.

**Use a table instead of an outline view to present data that’s not hierarchical.** For guidance, see [Lists and tables](lists-and-tables.md).

**Expose data hierarchy in the first column only.** Other columns can display attributes that apply to the hierarchical data in the primary column.

**Use descriptive column headings to provide context.** Use nouns or short noun phrases with [title-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64) and no punctuation; in particular, avoid adding a trailing colon. Always provide column headings in a multi-column outline view. If you don’t include a column heading in a single-column outline view, use a label or other means to make sure there’s enough context.

**Consider letting people click column headings to sort an outline view.** In a sortable outline view, people can click a column heading to perform an ascending or descending sort based on that column. You can implement additional sorting based on secondary columns behind the scenes, if necessary. If people click the primary column heading, sorting occurs at each hierarchy level. For example, in the Finder, all top-level folders are sorted, then the items within each folder are sorted. If people click the heading of a column that’s already sorted, the folders and their contents are sorted again in the opposite direction.

**Let people resize columns.** Data displayed in an outline view often varies in width. It’s important to let people adjust column width as needed to reveal data that’s wider than the column.

**Make it easy for people to expand or collapse nested containers.** For example, clicking a disclosure triangle for a folder in a Finder window expands only that folder. However, Option-clicking the disclosure triangle expands all of its subfolders.

**Retain people’s expansion choices.** If people expand various levels of an outline view to reach a specific item, store the state so you can display it again the next time. This way, people won’t need to navigate back to the same place again.

**Consider using alternating row colors in multi-column outline views.** Alternating colors can make it easier for people to track row values across columns, especially in wide outline views.

**Let people edit data if it makes sense in your app.** In an editable outline view cell, people expect to be able to single-click a cell to edit its contents. Note that a cell can respond differently to a double click. For example, an outline view listing files might let people single-click a file’s name to edit it, but double-click a file’s name to open the file. You can also let people reorder, add, and remove rows if it would be useful.

**Consider using a centered ellipsis to truncate cell text instead of clipping it.** An ellipsis in the middle preserves the beginning and end of the cell text, which can make the content more distinct and recognizable than clipped text.

**Consider offering a search field to help people find values quickly in a lengthy outline view.** Windows with an outline view as the primary feature often include a search field in the toolbar. For guidance, see [Search fields](search-fields.md).

## Platform considerations

*Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.*

## Related guidelines

- [Column views](column-views.md)
- [Lists and tables](lists-and-tables.md)
- [Split views](split-views.md)

---


<a id="split-views"></a>
## split-views

# Split views

> Source: <https://developer.apple.com/design/human-interface-guidelines/split-views>
> Section: Components › Layout and organization
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2025-06-09 (Added iOS and iPadOS platform considerations.)

A split view manages the presentation of multiple adjacent panes of content, each of which can contain a variety of components, including tables, collections, images, and custom views.

---

Typically, you use a split view to show multiple levels of your app’s hierarchy at once and support navigation between them. In this scenario, selecting an item in the view’s primary pane displays the item’s contents in the secondary pane. Similarly, a split view can display a tertiary pane if items in the secondary pane contain additional content.

It’s common to use a split view to display a [sidebar](sidebars.md) for navigation, where the leading pane lists the top-level items or collections in an app, and the secondary and optional tertiary panes can present child collections and item details. Rarely, you might also use a split view to provide groups of functionality that supplement the primary view — for example, Keynote in macOS uses split view panes to present the slide navigator, the presenter notes, and the inspector pane in areas that surround the main slide canvas.

## Best practices

**To support navigation, persistently highlight the current selection in each pane that leads to the detail view.** The selected appearance clarifies the relationship between the content in various panes and helps people stay oriented.

**Consider letting people drag and drop content between panes.** Because a split view provides access to multiple levels of hierarchy, people can conveniently move content from one part of your app to another by dragging items to different panes. For guidance, see [Drag and drop](drag-and-drop.md).

## Platform considerations

### Phone (iOS)

**Prefer using a split view in a regular — not a compact — environment.** A split view needs horizontal space in which to display multiple panes. In a compact environment, such as iPhone in portrait orientation, it’s difficult to display multiple panes without wrapping or truncating the content, making it less legible and harder to interact with.

### Tablet (iPadOS)

In iPadOS, a split view can include either two vertical panes, like Mail, or three vertical panes, like Keynote.

**Account for narrow, compact, and intermediate window widths.** Since iPad windows are fluidly resizable, it’s important to consider the design of a split view layout at multiple widths. In particular, ensure that it’s possible to navigate between the various panes in a logical way. For guidance, see [Layout](layout.md). For developer guidance, see [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) and [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller).

### Desktop (macOS)

In macOS, you can arrange the panes of a split view vertically, horizontally, or both. A split view includes dividers between panes that can support dragging to resize them. For developer guidance, see [VSplitView](https://developer.apple.com/documentation/swiftui/vsplitview) and [HSplitView](https://developer.apple.com/documentation/swiftui/hsplitview).

*Illustrated: Vertical, Horizontal, Multiple.*

**Set reasonable defaults for minimum and maximum pane sizes.** If people can resize the panes in your app’s split view, make sure to use sizes that keep the divider visible. If a pane gets too small, the divider can seem to disappear, becoming difficult to use.

**Consider letting people hide a pane when it makes sense.** If your app includes an editing area, for example, consider letting people hide other panes to reduce distractions or allow more room for editing — in Keynote, people can hide the navigator and presenter notes panes when they want to edit slide content.

**Provide multiple ways to reveal hidden panes.** For example, you might provide a toolbar button or a menu command — including a keyboard shortcut — that people can use to restore a hidden pane.

**Prefer the thin divider style.** The thin divider measures one point in width, giving you maximum space for content while remaining easy for people to use. Avoid using thicker divider styles unless you have a specific need. For example, if both sides of a divider present table rows that use strong linear elements that might make a thin divider hard to distinguish, it might work to use a thicker divider. For developer guidance, see [NSSplitView.DividerStyle](https://developer.apple.com/documentation/appkit/nssplitview/dividerstyle-swift.enum).

## Change log

| Date | Changes |
| --- | --- |
| June 9, 2025 | Added iOS and iPadOS platform considerations. |
| December 5, 2023 | Added guidance for split views in visionOS. |
| June 5, 2023 | Added guidance for split views in watchOS. |

## Related guidelines

- [Sidebars](sidebars.md)
- [Tab bars](tab-bars.md)
- [Layout](layout.md)

---


<a id="tab-views"></a>
## tab-views

# Tab views

> Source: <https://developer.apple.com/design/human-interface-guidelines/tab-views>
> Section: Components › Layout and organization
> Platforms covered: macOS (guidance specific to watchOS omitted)
> Last change on Apple's site: 2023-06-05 (Added guidance for using tab views in watchOS.)

A tab view presents multiple mutually exclusive panes of content in the same area, which people can switch between using a tabbed control.

---

## Best practices

**Use a tab view to present closely related areas of content.** The appearance of a tab view provides a strong visual indication of enclosure. People expect each tab to display content that is in some way similar or related to the content in the other tabs.

**Make sure the controls within a pane affect content only in the same pane.** Panes are mutually exclusive, so ensure they’re fully self-contained.

**Provide a label for each tab that describes the contents of its pane.** A good label helps people predict the contents of a pane before clicking or tapping its tab. In general, use nouns or short noun phrases for tab labels. A verb or short verb phrase may make sense in some contexts. Use title-style capitalization for tab labels.

**Avoid using a pop-up button to switch between tabs.** A tabbed control is efficient because it requires a single click or tap to make a selection, whereas a pop-up button requires two. A tabbed control also presents all choices onscreen at the same time, whereas people must click a pop-up button to see its choices. Note that a pop-up button can be a reasonable alternative in cases where there are too many panes of content to reasonably display with tabs.

**Avoid providing more than six tabs in a tab view.** Having more than six tabs can be overwhelming and create layout issues. If you need to present six or more tabs, consider another way to implement the interface. For example, you could instead present each tab as a view option in a pop-up button menu.

For developer guidance, see [NSTabView](https://developer.apple.com/documentation/appkit/nstabview).

## Anatomy

The tabbed control appears on the top edge of the content area. You can choose to hide the control, which is appropriate for an app that switches between panes programmatically.

When you hide the tabbed control, the content area can be borderless, bezeled, or bordered with a line. A borderless view can be solid or transparent.

**In general, inset a tab view by leaving a margin of window-body area on all sides of a tab view.** This layout looks clean and leaves room for additional controls that aren’t directly related to the contents of the tab view. You can extend a tab view to meet the window edges, but this layout is unusual.

## Platform considerations

*Not supported in iOS, iPadOS, tvOS, or visionOS.*

### Mobile (iOS, iPadOS)

For similar functionality, consider using a [segmented control](segmented-controls.md) instead.

## Change log

| Date | Changes |
| --- | --- |
| June 5, 2023 | Added guidance for using tab views in watchOS. |

## Related guidelines

- [Tab bars](tab-bars.md)
- [Segmented controls](segmented-controls.md)

---
