---
title: "Annotation::GetNext2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__GetNext2.htm"
---

# Annotation::GetNext2

This
method is obsolete and has been superseded by[Annotation::GetNext3](sldworksAPI.chm::/Annotation/Annotation__GetNext3.htm).

#### Description

This method gets the next annotation.

#### Syntax (OLE Automation)

retval = Annotation.GetNext2 ()

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Dispatch object of the next annotation |
| --- | --- | --- |

#### Syntax
(COM)

status = Annotation->IGetNext2 (
&retval )

(Table)=========================================================

| Output: | (LPANNOTATION) retval | Pointer to the next annotation |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method retrieves all display dimensions, including suppressed,
hidden, and dangling dimensions, if the sheet format is visible. See Sheet::SheetFormatVisible.

SolidWorks suppresses or hides a dimension when you specifically select
a dimension and hide it, or when you select a feature and hide all dimensions.
If you need to filter out these dimensions, use Annotation::Visibleto check that status.

SolidWorks returns the annotation even if it is on a layer that is not
displayed.

If annotations or any specific type of annotations are not displayed,
use ModelDoc2::GetUserPreferenceToggle to discover those situations.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Annotation_Object$$**$$ZGetAnnotation$$**$$ZGetInfoAnnotation$$**$$ZGetInfoAnnotations$$**$$SheetFormatVisible$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Annotation\Annotation__GetNext2.htm" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Get_Entities_Attached_To_Cosmetic_Thread_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Annotation\Annotation__GetNext2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
