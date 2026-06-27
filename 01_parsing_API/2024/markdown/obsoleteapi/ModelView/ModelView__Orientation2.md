---
title: "ModelView::Orientation2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelView/ModelView__Orientation2.htm"
---

# ModelView::Orientation2

This method is obsolete and has been superseded
by[ModelView::Orientation3](sldworksAPI.chm::/ModelView/ModelView__Orientation3.htm).

Description

This property gets and sets the view orientation matrix. This matrix
represents the model-to-view orientation and is in column-major order
and is pre-multiplied.

Syntax (OLE Automation)

orientation = ModelView.Orientation2 (VB
Get property)

ModelView.Orientation2 = orientation (VB
Set property)

orientation = ModelView.GetOrientation2
( ) (C++ Get property)

ModelView.SetOrientation2 ( orientation
) (C++ Set property)

(Table)=========================================================

| Property: | (VARIANT) orientation | a VARIANT containing an array of 16 doubles representing
the view orientation matrix |
| --- | --- | --- |

Syntax (COM)

status = ModelView->get_IOrientation2(
orientation)

status = ModelView->put_IOrientation2
( orientation )

(Table)=========================================================

| Property: | (double*) orientation | Pointer to an array of 16 doubles representing the view orientation
matrix |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Using data returned from this property along with information from the
ModelView::Scale2 and ModelView::Translation2 properties should be multiplied
in this order: orientation -> scale -> transform.

To map your coordinates from 3D space to the screen, refer to the ModelView::Xform
property. The Xform property returns a different set of data since it
is used for mapping to screen space which has its origin in the upper
left corner of the current view with the X vector pointing to the right
and the Y vector pointing down.

The matrix returned by this property is the following array of 16 doubles
representing the view rotation matrix:

image\ebd_Ebd1.gif

Be aware that the view rotation is in column-major order. This means
that the X component is represented by the 0, 4, 8, 12 positions, the
Y component by 1, 5, 9, 13, and the Z component by 2, 6, 10, and 14. The
Translation and Scale are not returned by this property.

As further illustration, some of the standard view orientations would
be returned as follows.

image\ebd_Ebd2.gif

Front View Right
View

The Right View matrix illustrates the column-major order returned by
SolidWorks.

If the SolidWorks file is in View-Only mode and is NOT displaying a
shaded image, then you cannot perform any view rotations. In this situation
you should not call any of the view rotation API's.

To determine if the file is in View-Only mode and whether it is shaded
refer to ModelDoc2::IsOpenedViewOnly and ModelView::GetDisplayState.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelView_Object$$**$$ZGetInfoModelView$$**$$ZModifyModelView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelView\ModelView__Orientation2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
