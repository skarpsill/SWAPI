---
title: "Annotation::GetAttachedEntityCount2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__GetAttachedEntityCount2.htm"
---

# Annotation::GetAttachedEntityCount2

This method is obsolete and has been superseded
by[Annotation::GetAttachedEntityCount3](sldworksAPI.chm::/Annotation/Annotation__GetAttachedEntityCount3.htm).

Description

This method gets the number
of entities to which this annotation is attached.

Syntax (OLE Automation)

retval = Annotation.GetAttachedEntityCount2 ()

(Table)=========================================================

| Output: | (long) retval | Number of entities to which this
annotation is attached |
| --- | --- | --- |

Syntax (COM)

status = Annotation->GetAttachedEntityCount2 (
&retval)

Parameters Table Start

(Table)=========================================================

| Output: | (long) retval | Number of entities to which this annotation is
attached |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method supports all annotation types. See
Annotation::GetType to determine the type of annotation.

Call this method before calling the COM versions
of Annotation::GetAttachedEntities2 or Annotation::GetAttachedEntityTypes.
Dispatch applications do not need a count method because they can use
the upper SafeArray bound from the Annotation::GetAttachedEntities2 and
Annotation::GetAttachedEntityTypes return values to determine the array
size.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Annotation\Annotation__GetAttachedEntityCount2.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Annotation_Object$$**$$ZGetInfoAnnotation$$**$$AnnotationAttachEntities$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Annotation\Annotation__GetAttachedEntityCount2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
