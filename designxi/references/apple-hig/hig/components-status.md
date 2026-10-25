# Apple HIG — Components › Status
Bundled HIG pages for the “Components › Status” group. Each page kept verbatim under an anchor heading `## <slug>`. Cite as **components-status.md › <slug> › heading**.


<a id="gauges"></a>
## gauges

# Gauges

> Source: <https://developer.apple.com/design/human-interface-guidelines/gauges>
> Section: Components › Status
> Platforms covered: iOS, iPadOS, macOS (guidance specific to visionOS, watchOS omitted)

A gauge displays a specific numerical value within a range of values.

---

In addition to indicating the current value in a range, a gauge can provide more context about the range itself. For example, a temperature gauge can use text to identify the highest and lowest temperatures in the range and display a spectrum of colors that visually reinforce the changing values.

## Anatomy

A gauge uses a circular or linear path to represent a range of values, mapping the current value to a specific point on the path. A standard gauge displays an indicator that shows the current value’s location; a gauge that uses the capacity style displays a fill that stops at the value’s location on the path.

Circular and linear gauges in both standard and capacity styles are also available in a variant that’s visually similar to watchOS complications. This variant — called accessory — works well in iOS Lock Screen widgets and anywhere you want to echo the appearance of complications.

> **Note:** In addition to gauges, macOS also supports level indicators, some of which have visual styles that are similar to gauges. For guidance, see [macOS](#desktop-macos).

## Best practices

**Write succinct labels that describe the current value and both endpoints of the range.** Although not every gauge style displays all labels, VoiceOver reads the visible labels to help people understand the gauge without seeing the screen.

**Consider filling the path with a gradient to help communicate the purpose of the gauge.** For example, a temperature gauge might use colors that range from red to blue to represent temperatures that range from hot to cold.

## Platform considerations

*No additional considerations for iOS, iPadOS, visionOS, or watchOS. Not supported in tvOS.*

### Desktop (macOS)

In addition to supporting gauges, macOS also defines a level indicator that displays a specific numerical value within a range. You can configure a level indicator to convey capacity, rating, or — rarely — relevance.

The capacity style can depict discrete or continuous values.

**Continuous.** A horizontal translucent track that fills with a solid bar to indicate the current value.

**Discrete.** A horizontal row of separate, equally sized, rectangular segments. The number of segments matches the total capacity, and the segments fill completely — never partially — with color to indicate the current value.

**Consider using the continuous style for large ranges.** A large value range can make the segments of a discrete capacity indicator too small to be useful.

**Consider changing the fill color to inform people about significant parts of the range.** By default, the fill color for both capacity indicator styles is green. If it makes sense in your app, you can change the fill color when the current value reaches certain levels, such as very low, very high, or just past the middle. You can change the fill color of the entire indicator or you can use the tiered state to show a sequence of several colors in one indicator, as shown below.

For guidance using the rating style to help people rank something, see [Rating indicators](rating-indicators.md).

Although rarely used, the relevance style can communicate relevancy using a shaded horizontal bar. For example, a relevance indicator might appear in a list of search results, helping people visualize the relevancy of the results when sorting or comparing multiple items.

## Change log

| Date | Changes |
| --- | --- |
| September 23, 2022 | New page. |

## Related guidelines

- [Ratings and reviews](ratings-and-reviews.md)

---


<a id="progress-indicators"></a>
## progress-indicators

# Progress indicators

> Source: <https://developer.apple.com/design/human-interface-guidelines/progress-indicators>
> Section: Components › Status
> Platforms covered: iOS, iPadOS, macOS (guidance specific to tvOS, visionOS, watchOS omitted)
> Last change on Apple's site: 2023-09-12 (Combined guidance common to all platforms.)

Progress indicators let people know that your app isn’t stalled while it loads content or performs lengthy operations.

---

Some progress indicators also give people a way to estimate how long they have to wait for something to complete. All progress indicators are transient, appearing only while an operation is ongoing and disappearing after it completes.

Because the duration of an operation is either known or unknown, there are two types of progress indicators:

- *Determinate*, for a task with a well-defined duration, such as a file conversion
- *Indeterminate*, for unquantifiable tasks, such as loading or synchronizing complex data

Both determinate and indeterminate progress indicators can have different appearances depending on the platform. A determinate progress indicator shows the progress of a task by filling a linear or circular track as the task completes. *Progress bars* include a track that fills from the leading side to the trailing side. *Circular progress indicators* have a track that fills in a clockwise direction.

An indeterminate progress indicator — also called an *activity indicator* — uses an animated image to indicate progress. All platforms support a circular image that appears to spin; however, macOS also supports an indeterminate progress bar.

For developer guidance, see [ProgressView](https://developer.apple.com/documentation/swiftui/progressview).

## Best practices

**When possible, use a determinate progress indicator.** An indeterminate progress indicator shows that a process is occurring, but it doesn’t help people estimate how long a task will take. A determinate progress indicator can help people decide whether to do something else while waiting for the task to complete, restart the task at a different time, or abandon the task.

**Be as accurate as possible when reporting advancement in a determinate progress indicator.** Consider evening out the pace of advancement to help people feel confident about the time needed for the task to complete. Showing 90 percent completion in five seconds and the last 10 percent in 5 minutes can make people wonder if your app is still working and can even feel deceptive.

**Keep progress indicators moving so people know something is continuing to happen.** People tend to associate a stationary indicator with a stalled process or a frozen app. If a process stalls for some reason, provide feedback that helps people understand the problem and what they can do about it.

**When possible, switch a progress bar from indeterminate to determinate.** If an indeterminate process reaches a point where you can determine its duration, switch to a determinate progress bar. People generally prefer a determinate progress indicator, because it helps them gauge what’s happening and how long it will take.

**Don’t switch from the circular style to the bar style.** Activity indicators (also called *spinners*) and progress bars are different shapes and sizes, so transitioning between them can disrupt your interface and confuse people.

**If it’s helpful, display a description that provides additional context for the task.** Be accurate and succinct. Avoid vague terms like *loading* or *authenticating* because they seldom add value.

**Display a progress indicator in a consistent location.** Choosing a consistent location for a progress indicator helps people reliably find the status of an operation across platforms or within or between apps.

**When it’s feasible, let people halt processing.** If people can interrupt a process without causing negative side effects, include a Cancel button. If interrupting the process might cause negative side effects — such as losing the downloaded portion of a file — it can be useful to provide a Pause button in addition to a Cancel button.

**Let people know when halting a process has a negative consequence.** When canceling a process results in lost progress, it’s helpful to provide an [alert](alerts.md) that includes an option to confirm the cancellation or resume the process.

## Platform considerations

### Mobile (iOS, iPadOS)

#### Refresh content controls

A refresh control lets people immediately reload content, typically in a table view, without waiting for the next automatic content update to occur. A refresh control is a specialized type of activity indicator that’s hidden by default, becoming visible when people drag down the view they want to reload. In Mail, for example, people can drag down the list of Inbox messages to check for new messages.

**Perform automatic content updates.** Although people appreciate being able to do an immediate content refresh, they also expect automatic refreshes to occur periodically. Don’t make people responsible for initiating every update. Keep data fresh by updating it regularly.

**Supply a short title only if it adds value.** Optionally, a refresh control can include a title. In most cases, this is unnecessary, as the animation of the control indicates that content is loading. If you do include a title, don’t use it to explain how to perform a refresh. Instead, provide information of value about the content being refreshed. A refresh control in Podcasts, for example, uses a title to tell people when the last podcast update occurred.

For developer guidance, see [UIRefreshControl](https://developer.apple.com/documentation/uikit/uirefreshcontrol).

### Desktop (macOS)

In macOS, an indeterminate progress indicator can have a bar or circular appearance. Both versions use an animated image to indicate that the app is performing a task.

**Prefer an activity indicator (spinner) to communicate the status of a background operation or when space is constrained.** Spinners are small and unobtrusive, so they’re useful for asynchronous background tasks, like retrieving messages from a server. Spinners are also good for communicating progress within a small area, such as within a text field or next to a specific control, such as a button.

**Avoid labeling a spinning progress indicator.** Because a spinner typically appears when people initiate a process, a label is usually unnecessary.

## Change log

| Date | Changes |
| --- | --- |
| September 12, 2023 | Combined guidance common to all platforms. |
| June 5, 2023 | Updated guidance to reflect changes in watchOS 10. |

---


<a id="rating-indicators"></a>
## rating-indicators

# Rating indicators

> Source: <https://developer.apple.com/design/human-interface-guidelines/rating-indicators>
> Section: Components › Status
> Platforms covered: macOS

A rating indicator uses a series of horizontally arranged graphical symbols — by default, stars — to communicate a ranking level.

---

A rating indicator doesn’t display partial symbols; it rounds the value to display complete symbols only. Within a rating indicator, symbols are always the same distance apart and don’t expand or shrink to fit the component’s width.

## Best practices

**Make it easy to change rankings.** When presenting a list of ranked items, let people adjust the rank of individual items inline without navigating to a separate editing screen.

**If you replace the star with a custom symbol, make sure that its purpose is clear.** The star is a very recognizable ranking symbol, and people may not associate other symbols with a rating scale.

## Platform considerations

*No additional considerations for macOS.  Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.*

## Change log

| Date | Changes |
| --- | --- |
| September 23, 2022 | New page. |

## Related guidelines

- [Ratings and reviews](ratings-and-reviews.md)

---
