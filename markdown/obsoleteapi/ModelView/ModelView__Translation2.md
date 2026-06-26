---
title: "ModelView::Translation2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelView/ModelView__Translation2.htm"
---

# ModelView::Translation2

This method is obsolete and has been superseded
by[ModelView::Translation3](sldworksAPI.chm::/ModelView/ModelView__Translation3.htm).

Description

This property gets and sets the view translation vector. These values
are in meters and describe the vector from the current screen center to
the center of the bounding box, where the bounding box represents the
extents of the current model in this orientation.

Syntax (OLE Automation)

translation = ModelView.Translation2 (VB
Get property)

ModelView.Translation2 = translation (VB
Set property)

translation = ModelView.GetTranslation2
( ) (C++ Get property)

ModelView.SetTranslation2 ( translation
) (C++ Set property)

(Table)=========================================================

| Property: | (VARIANT) translation | VARIANT of type SafeArray containing the desired view panning translation
vector in format of 3 doubles. |
| --- | --- | --- |

Syntax (COM)

status = ModelView->get_ITranslation2(
translation)

status = ModelView->put_ITranslation2
( translation )

(Table)=========================================================

| Property: | (double*) translation | Pointer to an array of 3 doubles representing the view panning translation
vector |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Using data returned from this property with information from ModelView::Orientation2
and ModelView::Scale2 should be multiplied in this order: 0rientation
-> scale -> transform.

To map your coordinates from 3D space to the screen, use ModelView::Xform.

To increase the speed of your view changes, use ModelView::StartDynamics
and ModelView::StopDynamics.

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
<param name="Items" value="ModelView_Object$$**$$ZGetInfoModelView$$**$$ZModifyModelView$$**$$ZXform$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelView\ModelView__Translation2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
