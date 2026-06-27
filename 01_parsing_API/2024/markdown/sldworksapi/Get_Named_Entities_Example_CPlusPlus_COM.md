---
title: "Get Named Entities Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Named_Entities_Example_CPlusPlus_COM.htm"
---

# Get Named Entities Example (C++ COM)

This example shows how to get the named entities.

// -------------------------------------------------------------------

// Preconditions:

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1)
An part is open.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2)
At least one named entity exists in the part.

//

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}void
APITestFunction()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULTkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VARIANT_BOOLkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= VARIANT_FALSE;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<ISldWorks>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IModelDoc>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComQIPtr
<IPartDoc>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pPart;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nEntCount
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IEntity>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pEntity;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPENTITY*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ppEntity
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Connect to SOLIDWORKS

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks
= TheApplication->GetSWApp();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pSldWorks);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSldWorks->get_IActiveDoc(&pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pPart
= pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pPart);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pPart->GetNamedEntitiesCount(&nEntCount);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(nEntCount
> 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ppEntity
= new LPENTITY[nEntCount];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(ppEntity);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ZeroMemory(ppEntity,
nEntCount * sizeof(LPENTITY));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pPart->IGetNamedEntities(nEntCount,
ppEntity);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(S_OK
== hr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i = 0; i < nEntCount; i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IEntity>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pEntity;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComBSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sEntName;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pEntity.Attach(ppEntity[i]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pPart->IGetEntityName(pEntity,
&sEntName);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OutputDebugString(sEntName);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OutputDebugString(_T("\n"));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
[] ppEntity;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}
//void APITestFunction()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
-------------------------------------------------------------------
