---
title: "Apply and Remove Texture By Body Display State Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Body_Display_State_Example_VBNET.htm"
---

# Apply and Remove Texture By Body Display State Example (VB.NET)

This example shows how to add and remove texture to and from a body
using the name of a display state of the model.

```
'--------------------------------------------------
' Preconditions: Verify that the specified part to open
' and texture exist.
'
' Postconditions:
' 1. Opens the specified part and applies texture to the
'    selected body.
' 2. In the IDE, click the Continue button
'    at Stop.
' 3. Removes texture from selected body.
' 4. To verify, click the Stop Debugging button in the
'    IDE to stop execution of the macro and click anywhere
'    in the graphics area.
'    - or -
'    If the Stop Debugging button is grayed out, click
'    anywhere in the graphics area.
'----------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
```

```vb
Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim body As Body2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim texture As Texture
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim modelview As ModelView
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim status As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim displayState As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim errors As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim warnings As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim namStr As String

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Open document and select a body
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2017\tutoria\multibody\multi_bridge.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}status = swModelDocExt.SelectByID2("hub", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}body = swSelMgr.GetSelectedObject6(1, -1)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Set texture on selected body in the
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' specified display state
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}displayState = "<Default>_Display State 1"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}namStr = "<SystemTexture>\images\textures\pattern\checker2.jpg"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}texture = swModelDocExt.CreateTexture(namStr, 5, 45, False)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}status = body.SetTextureByDisplayState(displayState, texture)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Redraw the window view
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}modelview = swModel.ActiveView
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}modelview.GraphicsRedraw(Nothing)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Examine the selected body to verify
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' that the specified texture was set
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' In the IDE, click the Continue button to
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' resume running macro
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Stop

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Remove texture from body by display state
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}status = swModelDocExt.SelectByID2("hub", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}body = swSelMgr.GetSelectedObject6(1, -1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}status = body.RemoveTextureByDisplayState(displayState)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
