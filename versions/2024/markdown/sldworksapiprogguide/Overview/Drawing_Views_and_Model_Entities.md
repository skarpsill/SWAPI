---
title: "Drawing Views and Model Entities"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Drawing_Views_and_Model_Entities.htm"
---

# Drawing Views and Model Entities

[IView::GetPolylines7](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~GetPolylines7.html)and[IView::IGetPolylines7](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~IGetPolylines7.html)return all of the polylines in a drawing view, including visible and partially
and completely obscured polylines. Because these polylines are not related
to the topology of the model, you do not know their relationship to the
model, making it difficult to work with them.

[IView::GetVisibleComponents](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~GetVisibleComponents.html),[IView::IGetVisibleComponents](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~IGetVisibleComponents.html),[IView::GetVisibleEntities](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~GetVisibleEntities.html),
and[IView::IGetVisibleEntities](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~IGetVisibleEntities.html)return the visible components, edges, faces, and vertices in relation
to the topology of the model, which simplifies working with them. Visible
components, edges, faces, and vertices are all of the components and entities
not completely obscured by other components in the drawing view.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Typical uses of IView::GetVisibleComponents or IView::IGetVisibleComponents
and IView::GetVisibleEnities or IView::IGetVisibleEntities might be to
get a component or an entity in order to get its properties or to add
an annotation to it.

The following example shows how to retrieve all of the visible components,
edges, faces, and vertices in a drawing view.

'--------------------------------------------------

' Preconditions: Drawing document is open, and

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}a
drawing view containing at lkadov_tag{{<spaces>}}east
one component

' is selected.

'

' Postconditions: None

'--------------------------------------------------

Option Explicit

Sub main()

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swSelMgr As SldWorks.SelectionMgr

Dim swDrawing As SldWorks.DrawingDoc

Dim drView As SldWorks.View

Dim Comp As SldWorks.Component2

Dim selData As SldWorks.SelectData

Dim ent As SldWorks.Entity

Dim EntComp As SldWorks.Component2

Dim itr As Long

Dim CompCount As Long

Dim vComps As Variant

Dim vEdges As Variant

Dim vVerts As Variant

Dim vFaces As Variant

Dim i As Long

Dim boolstatus As Boolean

Set swApp = Application.SldWorks

Set swModel = swApp.ActiveDoc

Set swDrawing = swModel

Set swSelMgr = swModel.SelectionManager

Set drView = swDrawing.ActiveDrawingView

Debug.Assert Not drView Is Nothing

Debug.Print "Name of drawing view: "; drView.Name

Debug.Print

CompCount = drView.GetVisibleComponentCount

Debug.Assert CompCount <> 0

Debug.Print "Number of visible components = ";
CompCount

vComps = drView.GetVisibleComponents

Debug.Assert Not IsEmpty(vComps)

For i = LBound(vComps) To UBound(vComps)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Component " & i & " name is " & vComps(i).Name2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Comp = vComps(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Get
all edges of this component that are visible in this drawing view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vEdges
= drView.GetVisibleEntities(Comp,
swViewEntityType_Edge)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
selData = swSelMgr.CreateSelectData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}selData.View
= drView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
IsEmpty(vEdges) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}No
edges"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}This
component has " & UBound(vEdges) + 1 & " visible edges
in this view."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
itr = 0 To UBound(vEdges)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
ent = vEdges(itr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= ent.Select4(False, selData)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
itr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Get
all vertices of this component that are visible in this drawing view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vVerts
= drView.GetVisibleEntities(Comp,
swViewEntityType_Vertex)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
IsEmpty(vVerts) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}No
vertices"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}This
component has " & UBound(vVerts) + 1 & " visible vertices
in this view"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
itr = 0 To UBound(vVerts)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
ent = vVerts(itr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= ent.Select4(False, selData)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
itr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Get
all faces of this component that are visible in this drawing view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vFaces
= drView.GetVisibleEntities(Comp,
swViewEntityType_Face)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
IsEmpty(vFaces) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}No
faces"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}This
component has " & UBound(vFaces) + 1 & " visible faces
in this view."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
itr = 0 To UBound(vFaces)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
ent = vFaces(itr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= ent.Select4(False, selData)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
itr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

Next i

'Get all the entities (edges, faces, and vertices) that
are visible in the drawing view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Comp = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
EntComp = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Get
all edges of all components that are visible in this drawing view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vEdges
= drView.GetVisibleEntities(Comp,
swViewEntityType_Edge)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"There are a total of " & UBound(vEdges) + 1 & "
visible edges in this view."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
itr = 0 To UBound(vEdges)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
ent = vEdges(itr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'boolstatus
= ent.Select4(False, selData)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
EntComp = ent.GetComponent

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
EntComp = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
itr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Get
all vertices of all components that are visible in this drawing view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vVerts
= drView.GetVisibleEntities(Comp,
swViewEntityType_Vertex)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"There are a total of " & UBound(vVerts) + 1 & "
visible vertices in this view."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
itr = 0 To UBound(vVerts)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
ent = vVerts(itr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'boolstatus
= ent.Select4(False, selData)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
EntComp = ent.GetComponent

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
EntComp = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
itr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Get
all faces of all components that are visible in this drawing view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vFaces
= drView.GetVisibleEntities(Comp,
swViewEntityType_Face)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"There are a total of " & UBound(vFaces) + 1 & "
visible faces in this view."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
itr = 0 To UBound(vFaces)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
ent = vFaces(itr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'boolstatus
= ent.Select4(False, selData)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
itr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub
