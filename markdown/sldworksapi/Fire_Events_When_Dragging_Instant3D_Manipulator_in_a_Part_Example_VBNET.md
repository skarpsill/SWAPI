---
title: "Fire Events When Dragging Instant3D Manipulator in a Part Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Dragging_Instant3D_Manipulator_in_a_Part_Example_VBNET.htm"
---

# Fire Events When Dragging Instant3D Manipulator in a Part Example (VB.NET)

This example shows how to fire events when dragging an Instant3D manipulator
in a part document.

```vb
'------------------------------------
 ' Preconditions:
 ' 1. Open a part document.
 ' 2. Open the Immediate window.
 '
 ' kadov_tag{{</spaces>}}NOTE: Instant3D is enabled by the macro.
 '
 ' Postconditions:
 ' 1. Select an Instant3D manipulator in the
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}open part. For example,
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}double-click an extrude feature in a part,
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}then select one of the Instant3D manipulators
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}and drag it.
 ' 2. Writes a debug statement to the Immediate window
 '    informing you that kadov_tag{{</spaces>}}dragging of an Instant3D
 '    manipulator has started.
 ' 3. Stop dragging the manipulator.
 ' 4. Writes a debug statement to the Immediate kadov_tag{{</spaces>}}
 ' kadov_tag{{<spaces>}}   window informing you that dragging of
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}an Instant3D manipulator has stopped.
 ' 5. Examine the Immediate window.
 '----------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Collections
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public WithEvents pDoc As PartDoc

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeatMgr As FeatureManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim openPart As Hashtable

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Enable Instant3D
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeatMgr = swModel.FeatureManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeatMgr.MoveSizeFeatures = True

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Execute events
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}pDoc = swModel
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}openPart = New Hashtable
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
