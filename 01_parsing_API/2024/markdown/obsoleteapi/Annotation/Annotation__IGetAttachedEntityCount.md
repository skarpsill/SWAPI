---
title: "Annotation::IGetAttachedEntityCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__IGetAttachedEntityCount.htm"
---

# Annotation::IGetAttachedEntityCount

This method is obsolete and has been superseded
by[Annotation::GetAttachedEntityCount2](Annotation__GetAttachedEntityCount2.htm).

Description

This method gets the number of items associated
with this annotation and creates a static list of elements.

Syntax (OLE Automation)

Not Available.

Syntax (COM)

status = Annotation->IGetAttachedEntityCount (
&retval )

(Table)=========================================================

| Output: | (long) retval | Number of objects attached to this annotation |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

You can use the list of elements created by this
method with Annotation::IGetAttachedEntities and Annotation::IGetAttachedEntityTypes.

This method supports all annotation types. See
Annotation::GetType to determine the type of annotation.

COM applications must call this method before calling
Annotation::IGetAttachedEntities or Annotation::IGetAttachedEntityTypes.
Dispatch applications do not need a count method because they can use
the upper SafeArray bound from the Annotation::GetAttachedEntities and
Annotation::GetAttachedEntityTypes return values to determine the array
size.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Annotation_Object$$**$$Annotation::GetAttachedEntities$$**$$Annotation::GetAttachedEntityTypes$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Annotation\Annotation__IGetAttachedEntityCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
