---
title: "Fire Events When Display State Changes in Part Document (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Display_State_Changes_in_Part_Document_Example_VBNET.htm"
---

# Fire Events When Display State Changes in Part Document (VB.NET)

## Fire Events When Display State Changes in Part Document Example (VB.NET)

This example shows how to fire the events related to changing display
states of a configuration in a part document.

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
Option Explicit On

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Collections

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public WithEvents swPart As PartDoc

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim openPart As Hashtable

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Set up events
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swPart = swModel
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}openPart = New Hashtable
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachEventHandlers()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachSWEvents()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swPart.ActiveDisplayStateChangePreNotify, AddressOf Me.swPart_ActiveDisplayStateChangePreNotify
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swPart.ActiveDisplayStateChangePostNotify, AddressOf Me.swPart_ActiveDisplayStateChangePostNotify
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function swPart_ActiveDisplayStateChangePreNotify() As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Send message when user changes display state in the ConfigurationManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("The active configuration's display state is about to change.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function swPart_ActiveDisplayStateChangePostNotify(ByVal DisplayStateName As String) As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Send message after user changes display state in the ConfigurationManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("The active configuration's display state has changed.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
