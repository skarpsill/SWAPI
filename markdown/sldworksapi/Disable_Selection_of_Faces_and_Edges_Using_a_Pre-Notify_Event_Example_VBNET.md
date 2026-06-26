---
title: "Disable Selection of Faces and Edges Using a Pre-Notify Event Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Disable_Selection_of_Faces_and_Edges_Using_a_Pre-Notify_Event_Example_VBNET.htm"
---

# Disable Selection of Faces and Edges Using a Pre-Notify Event Example (VB.NET)

This example shows how to disable the interactive selection of these entities
using a pre-notify event:

- faces in part and assembly documents
- edges in drawing documents

```vb
'---------------------------------------------------
 ' Preconditions: Open a part, assembly, or drawing.
 '
 ' NOTE: Tools > Options > System > Stop VSTA debugger
 ' kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}  on macro exit must be cleared for this macro
 ' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}to run to completion.
 '
 ' Postconditions:
 ' kadov_tag{{<spaces>}}1. Disables interactively selecting faces in
 ' kadov_tag{{<spaces>}}   a part or assembly.
 '    - or -
 '    Disables interactively selecting edges in a
 ' kadov_tag{{<spaces>}}   drawing.
 ' 2. Click the Stop Debugging button in the
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}SOLIDWORKS Visual Studio Tools for
 ' kadov_tag{{<spaces>}}   Applications IDE to re-enable the
 ' kadov_tag{{<spaces>}}   interactive selection of faces in
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}a part or assembly document or edges in
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}a drawing document.
 '----------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Collections
 Partial Class SolidWorksMacro
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public WithEvents pDoc As PartDoc
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public WithEvents aDoc As AssemblyDoc
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public WithEvents dDoc As DrawingDoc
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim openPart As Hashtable
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim openAssembly As Hashtable
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim openDrawing As Hashtable
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Determine the document type
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' and set up event handlers
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swModel.GetType = swDocumentTypes_e.swDocPART Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pDoc = swModel
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}openPart = New Hashtable
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf swModel.GetType = swDocumentTypes_e.swDocASSEMBLY Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}aDoc = swModel
             kadov_tag{{</spaces>}}openAssembly = New Hashtable
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf swModel.GetType = swDocumentTypes_e.swDocDRAWING Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dDoc = swModel
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}openDrawing = New Hashtable
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachEventHandlers()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachEventHandlers()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachSWEvents()
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachSWEvents()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Not pDoc Is Nothing Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AddHandler pDoc.UserSelectionPreNotify, AddressOf Me.pDoc_UserSelectionPreNotify
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Not aDoc Is Nothing Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AddHandler aDoc.UserSelectionPreNotify, AddressOf Me.aDoc_UserSelectionPreNotify
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Not dDoc Is Nothing Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AddHandler dDoc.UserSelectionPreNotify, AddressOf Me.dDoc_UserSelectionPreNotify
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function pDoc_UserSelectionPreNotify(ByVal SelectionType As Integer) As Integer
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Disable the selection of faces in this part
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If SelectionType = swSelectType_e.swSelFACES Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pDoc_UserSelectionPreNotify = True
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Function aDoc_UserSelectionPreNotify(ByVal SelectionType As Integer) As Integer
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Disable the selection of faces in this assembly
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If SelectionType = swSelectType_e.swSelFACES Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}aDoc_UserSelectionPreNotify = True
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function dDoc_UserSelectionPreNotify(ByVal SelectionType As Integer) As Integer
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Disable the selection of edges in this drawing
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If SelectionType = swSelectType_e.swSelEDGES Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dDoc_UserSelectionPreNotify = True
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```
