---
title: "Fire Events When Dragging Instant3D Manipulator in an Assembly Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Dragging_Instant3D_Manipulator_in_an_Assembly_Example_VBNET.htm"
---

# Fire Events When Dragging Instant3D Manipulator in an Assembly Example (VB.NET)

This example shows how to fire events when dragging an Instant3D manipulator
in an assembly document.

```vb
'------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document.
 ' 2. Open the Immediate window.
 '
 ' NOTE: Instant3D is enabled by the macro.
 '
 ' Postconditions:
 ' 1. Select an Instant3D manipulator in the
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}open assembly by right-clicking a floating
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}assembly component, clicking the down arrows
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}at the bottom of the shortcut menu, and selecting
 ' kadov_tag{{<spaces>}}   Move with Triad.
 ' 2. Drag the Instant3D handle kadov_tag{{</spaces>}}to move the assembly
 '    component.
 ' 3. Writes a debug statement to the Immediate window
 '    informing you that kadov_tag{{</spaces>}}dragging of an Instant3D
 '    manipulator has started.
 ' 4. Stop dragging the manipulator.
 ' 5. Writes a debug statement to the Immediate window
 '    informing you that kadov_tag{{</spaces>}}dragging of an Instant3D
 '    manipulator has stopped.
 ' 6. Examine the Immediate window.
 '----------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Collections
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public WithEvents pDoc As AssemblyDoc

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeatMgr As FeatureManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim openAssembly As Hashtable

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Enable Instant3D
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeatMgr = swModel.FeatureManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeatMgr.MoveSizeFeatures = True

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Execute events
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}pDoc = swModel
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}openAssembly = New Hashtable

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachEventHandlers()

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachEventHandlers()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachSWEvents()
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachSWEvents()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Not pDoc Is Nothing Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AddHandler pDoc.DragStateChangeNotify, AddressOf Me.pDoc_DragStateChangeNotify
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function pDoc_DragStateChangeNotify(ByVal State As Boolean) As Integer
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Write debug statement when dragging of manipulator started and stopped
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If State = True Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Dragging of manipulator started.")
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Dragging of manipulator stopped.")
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

 End Class
```
