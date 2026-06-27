---
title: "Annotation::GetAttachedEntities"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__GetAttachedEntities.htm"
---

# Annotation::GetAttachedEntities

This method is obsolete and has been superseded
by[Annotation::GetAttachedEntities2](Annotation__GetAttachedEntities2.htm).

Description

This method returns the entities associated
with this annotation.

Syntax (OLE Automation)

retval = Annotation.GetAttachedEntities ( )

(Table)=========================================================

| Return: | (VARIANT) retval | Pointer to an array of Dispatch objects |
| --- | --- | --- |

Syntax (COM)

status = Annotation->IGetAttachedEntities ( retval
)

(Table)=========================================================

| Output: | (LPUNKNOWN*) retval | Pointer to an array of LPUNKNOWN objects |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

This method now supports all annotation types. In SolidWorks 99, datecode
1999207, support was only available for cosmetic thread annotations and
surface finish symbol annotations (swCThread and swSFSymbol, respectively).
See Annotation::GetType to determine the type of annotation.

The array returned by this function may contain
one or more objects of varying type. To determine the corresponding object
type in the Annotation::GetAttachedEntites array, see Annotation::GetAttachedEntityTypes.
COM applications can use QueryInterface to obtain the specific object
from the LPUNKNOWN pointer.

(Table)=========================================================

| Object Type | Object
Returned |
| --- | --- |
| swSelFACES | Face2 |
| swSelEDGES | Edge |
| swSelVERTICES | Vertex |
| swSelSKETCHSEGS | SketchSegment |
| swSelSKETCHPOINTS | SketchPoint |
| swSelNOTHING | NULL (annotation is dangling or unsupported) |

You can associate annotations with some items not
listed in the previous table (for example, origins). If this annotation
is attached to one or more of those entities, then SolidWorks returns
a corresponding NULL in one of the array positions and Annotation::GetAttachedEntityTypes
indicates the unsupported entity by returning a corresponding swSelNOTHING
value. COM applications that call Annotation::IGetAttachedEntityCount
include the NULL value in the total count of associated entities.

Likewise, if an annotation has become disassociated
from its geometry, then SolidWorks returns a corresponding NULL in one
of the array positions and Annotation::GetAttachedEntityTypes indicates
the dangling item by returning a corresponding swSelNOTHING value.

COM applications must call Annotation::IGetAttachedEntityCount
before calling this this method. Annotation::IGetAttachedEntityCount determines
the necessary array size in your call to Annotation::IGetAttachedEntities
and creates the list of attached entities. Dispatch applications can determine
the number of associated entities by checking the size of the SafeArray.

If this annotation is not associated with any geometry
(for example, a note without a leaderline), then SolidWorks returns an
empty array. See Return Values for details on detecting empty arrays.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Annotation_Object$$**$$Annotation::GetAttachedEntityTypes$$**$$Annotation::IGetAttachedEntityCount$$**$$Annotation::GetType$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Annotation\Annotation__GetAttachedEntities.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Get_Entities_Attached_To_Cosmetic_Thread_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Annotation\Annotation__GetAttachedEntities.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
