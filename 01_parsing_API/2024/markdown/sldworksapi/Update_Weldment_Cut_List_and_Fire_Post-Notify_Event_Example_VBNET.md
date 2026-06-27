---
title: "Update Weldment Cut List and Fire Post-Notify Event Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_Weldment_Cut_List_and_Fire_Post-Notify_Event_Example_VBNET.htm"
---

# Update Weldment Cut List and Fire Post-Notify Event Example (VB.NET)

This example shows how to handle the post-notification event that fires

when the weldment cut list is updated.

```vb
'------------------------------------------------------
' Preconditions: Specified file to open exists.
'
' Postconditions:
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. Right-click on the Cut list folder.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2. Select Update from the right-click menu.
' kadov_tag{{<spaces>}}3. A message box displays (look in the taskbar for the hidden dialog).
' kadov_tag{{<spaces>}}4. Click OK.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}5. Stop the macro.
'------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Partial Class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public WithEvents swPart As PartDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, False)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDocSpecification As DocumentSpecification
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\weldments\weldment_box2.sldprt")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.DocumentType = swDocumentTypes_e.swDocPART
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.OpenDoc7(swDocSpecification)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swPart = swModel
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Set up event
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachEventHandlers()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachSWEvents()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swPart.WeldmentCutListUpdatePostNotify, AddressOf Me.swPart_WeldmentCutListUpdatePostNotify
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Function swPart_WeldmentCutListUpdatePostNotify() As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("The cut list is updated.")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, True)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```
