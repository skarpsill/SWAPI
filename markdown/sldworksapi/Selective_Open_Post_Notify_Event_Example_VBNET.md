---
title: "Selective Open Post-Notify Event Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Selective_Open_Post_Notify_Event_Example_VBNET.htm"
---

# Selective Open Post-Notify Event Example (VB.NET)

This example shows how to handle the post-notification event that fires when
components are selected for Quick View/Selective Open.

```
'------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly to open
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. If the Large Design Review dialog displays,
'    then click OK to close it.
' 2. When prompted, select the components to open
'    and click Open Selected.
' 3. Click OK to close the message box.
' 4. If prompted to rebuild, then click Rebuild.
' 5. After reading the next message box displayed,
'    click OK to close it.
' 6. Displays only the selected components.
' 7. Inspect the Immediate Window and graphics area.
'
' NOTE: Because the assembly is used elsewhere, do not save
' changes.
'--------------------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Partial Class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public WithEvents swAssembly As AssemblyDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, False)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDocSpecification As DocumentSpecification
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bowl and chute.sldasm")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.InteractiveComponentSelection = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.DocumentType = swDocumentTypes_e.swDocASSEMBLY
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.OpenDoc7(swDocSpecification)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swAssembly = swModel
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Set up event
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachEventHandlers()
kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachSWEvents()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swAssembly.SelectiveOpenPostNotify, AddressOf Me.swAssembly_SelectiveOpenPostNotify
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Function swAssembly_SelectiveOpenPostNotify(ByVal NewAddedDisplayStateName As String, ByRef SelectedComponentNames As Object) As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("A post-notification event has been fired for the selective open.")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}System.Diagnostics.Debug.Print("New display state name: " & NewAddedDisplayStateName)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}System.Diagnostics.Debug.Print("Selected component names:")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 To UBound(SelectedComponentNames)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}System.Diagnostics.Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}" & SelectedComponentNames(i))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, True)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```
