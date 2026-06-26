---
title: "ModelView::Xform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelView/ModelView__Xform.htm"
---

# ModelView::Xform

This
method is obsolete and has been superseded by[ModelView::Transform](sldworksAPI.chm::/ModelView/ModelView__Transform.htm).

Description

This property gets the total transform to go from 3D space to the screen.

Syntax (OLE Automation)

Xform = ModelView.Xform (VB Get
property)

Xform = ModelView.GetXform ( ) (C++
Get property)

(Table)=========================================================

| Property: | (VARIANT) Xform | VARIANT of type SafeArray of 16 doubles; first 9 are elements of 3x3
rotation matrix, next 3 define translation, next element is scaling, and
the last 3 elements are not used |
| --- | --- | --- |

Syntax (Com)

status = ModelView->get_IXform(
Xform)

(Table)=========================================================

| Property: | (double*) Xform | Pointer to an array of 16 doubles; first 9 are elements of 3x3 rotation
matrix, next 3 define translation, next element is scaling, and the last
3 elements are not used |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is typically used when you are grabbing the view handle
using ModelView::GetViewHWnd and drawing to the view. For example, if
you had a point located at 2,2,2 in model space coordinates, then you
could multiply it by this return value to determine where to draw in screen
space coordinates. The result will be pixel values for the current view.

The screen space coordinate system has its origin in the upper-left
corner of the current view with the X vector pointing to the right and
the Y vector pointing down.

If the SolidWorks file is in view-only mode and is not displaying a
shaded image, then you cannot perform any view rotations. In this situation,
you should not call any of the view rotation APIs.

To determine if the file is in view-only mode and whether it is shaded
or not, seekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc2::IsOpenedViewOnly
and ModelView::GetDisplayState.

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
<param name="Items" value="ModelView_Object$$**$$ZGetModelView$$**$$ZGetInfoModelView$$**$$ZModifyModelView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelView\ModelView__Xform.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Get_ModelView_Screen_Transform_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelView\ModelView__Xform.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
