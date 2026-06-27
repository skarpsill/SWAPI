---
title: "Show Bubble ToolTip Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swhtmlcontrolapi/Show_Bubble_ToolTip_Example_VB.htm"
---

# Show Bubble ToolTip Example (VBA)

This example shows how to display a Bubble ToolTip.

'--------------------------------------------

'

' Preconditions: HTML file exists at the specified location.

'

' Postconditions: Contents of the HTML file are displayed
in a Bubble ToolTip.

'

'--------------------------------------------

Option Explicit

Public Enum swArrowPosition_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowLeftTop
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowLeftBottom
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowRightTop
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowRightBottom
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowUpTopLeft
= 4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowUpTopRight
= 5

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowDownBottomLeft
= 6

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowDownBottomRight
= 7

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowLeftOrRightTop
= 8

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowLeftOrRightBottom
= 9

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowLeftOrRight
= 10

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowUpOrDownLeft
= 11

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowUpOrDownRight
= 12

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowUpOrDown
= 13

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowNone
= 14

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swArrowUnknown
= 15

End Enum

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Const
sURLpathkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
String = "D:/Samples/Sample_QuickTips.html"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
pSldWorkskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pSldWorks = CreateObject("SwHtmlControl.SwHtmlInterface")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks.ShowBubbleTooltipAt
300, 400, swArrowLeftTop, "Sample Bubble ToolTip", "Message
of Sample Bubble ToolTip", sURLpath

End Sub

'--------------------------------------------
