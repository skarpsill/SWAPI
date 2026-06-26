---
title: "Fire Events When Display State Changes in Part Document (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Display_State_Changes_in_Part_Document_Example_VB6.htm"
---

# Fire Events When Display State Changes in Part Document (VBA)

## Fire Events When Display State Changes in Part Document Example (VBA)

This example shows how to fire the events related to changing display
states of a configuration in a part document.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

- [Module](#Module)
- [Class Module](#Class)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Module

```vb
'---------------------------------------------------------------
' Preconditions:
' 1. Open a part document that has kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
' kadov_tag{{<spaces>}}   a configuration with multiple display states.
' kadov_tag{{<spaces>}}2. Run this macro in debug mode.
' kadov_tag{{<spaces>}}3. Change the display state of the active configuration in SOLIDWORKS
' kadov_tag{{<spaces>}}   (click the ConfigurationManager tab and double-click
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}a different display state).
'
' Postcondition: A message box is displayed informing
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}you that the display state is about change. After the display state changes,
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}another message box is displayed informing you that the display
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}state has changed.
'---------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swPart As SldWorks.PartDoc
Dim swPartEvents As Class1

Sub main()
Set swApp = Application.SldWorks
Set swPart = swApp.ActiveDoc

'Set up events
Set swPartEvents = New Class1
Set swPartEvents.swPart = swApp.ActiveDoc
End Sub
```

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Class
Module

```vb
Option Explicit

Public WithEvents swPart As SldWorks.PartDoc

Private Function swPart_ActiveDisplayStateChangePreNotify() As Long
'Send message when user changes display state in the ConfigurationManager
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}MsgBox "The active configuration's display state is about to change."
End Function

Private Function swPart_ActiveDisplayStateChangePostNotify(ByVal DisplayStateName As String) As Long
'Send message after user changes display state in the ConfigurationManager
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}MsgBox "The active configuration's display state has changed."
End Function
```
