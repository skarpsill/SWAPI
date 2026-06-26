---
title: "Fire Events When Display State Changes Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Display_State_Changes_Example_VBNET.htm"
---

# Fire Events When Display State Changes Example (VB.NET)

This example shows how to fire the events related to changing display
states of a configuration in an assembly document.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open an assembly document that has a configuration with multiple
'    display states.
' 2. Run this macro in debug mode.
' 3. Change the display state of the active configuration in SOLIDWORKS
'    (click the ConfigurationManager tab and double-click
'    a different display state).
'
' Postconditions:
' 1. Displays a message box informing you that the display state is about to
'    change.
' 2. After the display state changes, displays another message informing you
'    that the display state has changed.
'
' NOTE: This example also fires these events when you change
' configurations in an assembly document.
'---------------------------------------------------------------
Option Explicit On
```

```vb
Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics
 Imports System.Collections

 Partial Class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public WithEvents swAssem As AssemblyDoc

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub Main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim openAssem As Hashtable
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Set up events
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swAssem = swModel
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}openAssem = New Hashtable
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachEventHandlers()

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachEventHandlers()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachSWEvents()
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachSWEvents()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swAssem.ActiveDisplayStateChangePreNotify, AddressOf Me.swAssem_ActiveDisplayStateChangePreNotify
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swAssem.ActiveDisplayStateChangePostNotify, AddressOf Me.swAssem_ActiveDisplayStateChangePostNotify
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function swAssem_ActiveDisplayStateChangePreNotify() As Integer
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Send message when user changes display state in the ConfigurationManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("The active configuration's display state is about to change.")
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function swAssem_ActiveDisplayStateChangePostNotify(ByVal DisplayStateName As String) As Integer
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Send message after user changes display state in the ConfigurationManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("The active configuration's display state has changed.")
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```
