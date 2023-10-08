from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate

# Environment Variables
import os
from dotenv import load_dotenv
openai_api_key = os.getenv('OPENAI_API_KEY')
# Twitter
import tweepy
load_dotenv()
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost/",
    "http://localhost:3000/",
    "http://localhost:8000/",
    "http://localhost:8080/",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)


llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key, model_name='gpt-4')

agreement_template_demos="""
> **[Non-Disclosure Agreement]{.smallcaps}**

[This Agreement made on this the \_\_\_\_\_\_\_\_\_ day of
\_\_\_\_\_\_\_\_\_, 2016]{.smallcaps}

**[By and Between]{.smallcaps}**

##

**\<*Party 1*\>,** a company incorporated under the Companies Act, 1956
and having its registered office at \<\<address\>\> (hereinafter
referred to as "\_\_\_\_", which expression shall unless repugnant to
the context or meaning thereof, include its successors in interests and
assigns) [**of the** **one part**]{.smallcaps};

[And]{.smallcaps}

**\[*Please fill in Customers name*\]** a company incorporated under the
Companies Act, 2013 and having its registered office at **\[*Please fill
in address*\]** (hereinafter referred to as "**Company**" which
expression shall, unless repugnant to the context or meaning thereof, be
deemed to include, its representatives and permitted assigns) **[of the
Other part;]{.smallcaps}**

*PARTY 1* and COMPANY shall hereinafter be referred to as such or
collectively as "**Parties**" and individually as "**Party**".

**WHEREAS** both the Parties herein wish to pursue discussions and
negotiate with each other for the purpose of entering into a potential
business arrangement in relation to \[*Please fill in details of
proposed transaction*\] ("**Proposed Transaction**");

**AND WHEREAS** the Parties contemplate that with respect to the
Proposed Transaction, both the Parties may exchange certain information,
material and documents relating to each other's business, assets,
financial condition, operations, plans and/or prospects of their
businesses (hereinafter referred to as "**Confidential Information**",
more fully detailed in clause 1 herein below) that each Party regards as
proprietary and confidential; and

**AND WHEREAS**, each Party wishes to review such Confidential
Information of the other for the sole purpose of determining their
mutual interest in engaging in the Proposed Transaction;

**IN CONNECTION WITH THE ABOVE, THE PARTIES HEREBY AGREE AS FOLLOWS:**

1\. "**Confidential and or proprietary Information**" shall mean and
include any information disclosed by one Party (Disclosing Party) to the
other (Receiving Party) either directly or indirectly, in writing,
orally, by inspection of tangible objects (including, without
limitation, documents, prototypes, samples, media, documentation, discs
and code). Confidential information shall include, without limitation,
any materials, trade secrets, network information, configurations,
trademarks, brand name, know-how, business and marketing plans,
financial and operational information, and all other non-public
information, material or data relating to the current and/ or future
business and operations of the Disclosing Party and analysis,
compilations, studies, summaries, extracts or other documentation
prepared by the Disclosing Party. Confidential Information may also
include information disclosed to the Receiving Party by third parties on
behalf of the Disclosing Party.

2\. The Receiving Party shall refrain from disclosing, reproducing,
summarising and/or distributing Confidential Information and
confidential materials of the Disclosing Party except in connection with
the Proposed Transaction.

3\. The Parties shall protect the confidentiality of each other's
Confidential Information in the same manner as they protect the
confidentiality of their own proprietary and confidential information of
similar nature. Each Party, while acknowledging the confidential and
proprietary nature of the Confidential Information agrees to take all
reasonable measures at its own expense to restrain its representatives
from prohibited or unauthorised disclosure or use of the Confidential
Information.

4.  Confidential Information shall at all times remain the property of
    the Disclosing Party and may not be copied or reproduced by the
    Receiving Party without the Disclosing Party's prior written
    consent.

5\. Within seven (7) days of a written request by the Disclosing Party,
the Receiving Party shall return/destroy (as may be requested in writing
by the Disclosing Party or upon expiry and or earlier termination) all
originals, copies, reproductions and summaries of Confidential
Information provided to the Receiving Party as Confidential Information.
The Receiving Party shall certify to the Disclosing Party in writing
that it has satisfied its obligations under this paragraph.

6\. The Receiving Party may disclose the Confidential Information only
to the Receiving Party\'s employees and consultants on a need-to-know
basis. The Receiving Party shall have executed or shall execute
appropriate written agreements with third parties, in a form and manner
sufficient to enable the Receiving Party to enforce all the provisions
of this Agreement.

7\. Confidential Information, however, shall not include any information
which the Receiving Party can show:

> i\) is in or comes into the public domain otherwise than through a
> breach of this Agreement or the fault of the Receiving Party; or
>
> ii\) was already in its possession free of any such restriction prior
> to receipt from the Disclosing Party; or
>
> iii\) was independently developed by the Receiving Party without
> making use of the Confidential Information; or
>
> iv\) has been approved for release or use (in either case without
> restriction) by written authorisation of the Disclosing Party.

8\. In the event either Party receives a summons or other validly issued
administrative or judicial process requiring the disclosure of
Confidential Information of the other Party, the Receiving Party shall
promptly notify the Disclosing Party. The Receiving Party may disclose
Confidential Information to the extent such disclosure is required by
law, rule, regulation or legal process; *provided however*, that, to the
extent practicable, the Receiving Party shall give prompt written notice
of any such request for such information to the Disclosing Party, and
agrees to co-operate with the Disclosing Party, at the Disclosing
Party's expense, to the extent permissible and practicable, to challenge
the request or limit the scope there of, as the Disclosing Party may
reasonably deem appropriate.

9\. Neither Party shall use the other's name, trademarks, proprietary
words or symbols or disclose under this Agreement in any publication,
press release, marketing material, or otherwise without the prior
written approval of the other.

10\. Each Party agrees that the conditions in this Agreement and the
Confidential Information disclosed pursuant to this Agreement are of a
special, unique, and extraordinary character and that an impending or
existing violation of any provision of this Agreement would cause the
other Party irreparable injury for which it would have no adequate
remedy at law and further agrees that the other Party shall be entitled
to obtain immediately injunctive relief prohibiting such violation, in
addition to any other rights and remedies available to it at law or in
equity.

11\. The Receiving Party shall indemnify the Disclosing Party for all
costs, expenses or damages that Disclosing Party incurs as a result of
any violation of any provisions of this Agreement. This obligation shall
include court, litigation expenses, and actual, reasonable attorney's
fees. The Parties acknowledge that as damages may not be a sufficient
remedy for any breach under this Agreement, the non-breaching party is
entitled to seek specific performance or injunctive relief (as
appropriate) as a remedy for any breach or threatened breach, in
addition to any other remedies at law or in equity.

12\. Neither Party shall be liable for any special, consequential,
incidental or exemplary damages or loss (or any lost profits, savings or
business opportunity) regardless of whether a Party was advised of the
possibility of the damage or loss asserted.

13\. Both the Parties agree that by virtue of the Parties entering into
this Agreement neither Party is obligated to disclose all or any of the
Confidential Information to the other as stated in this Agreement. The
Parties reserve the right to disclose only such information at its
discretion and which it thinks, is necessary to disclose in relation to
the Proposed Transaction.

14\. Both the Parties agree that this Agreement will be effective from
the date of execution of this Agreement by both Parties and shall
continue to be effective till the Proposed Transaction is terminated by
either Party by giving a thirty (30)days notice, in case either Party
foresees that the Proposed Transaction would not be achieved.

> Notwithstanding anything contained herein, the provisions of this
> Agreement shall survive and continue after expiration or termination
> of this Agreement for a further period of five year(s) from the date
> of expiration.
>
> It being further clarified that notwithstanding anything contained
> herein, in case a binding agreement is executed between the Parties in
> furtherance of the Proposed Transaction, the terms and conditions of
> this Agreement shall become effective and form a part of that binding
> agreement and be co-terminus with such binding agreement and shall be
> in effect till the term of such binding agreement and shall after its
> expiry and or early termination shall continue to be in force in the
> following manner:

i.  ... .............. years after the termination of the binding
    > agreement

ii. ......... ......years after the expiry of the binding agreement

> (whichever is earlier)

15\. Each Party warrants that it has the authority to enter into this
Agreement.

16\. If any provision of this agreement is held to be invalid or
unenforceable to any extent, the remainder of this Agreement shall not
be affected and each provision hereof shall be valid and enforceable to
the fullest extent permitted by law. Any invalid or unenforceable
provision of this Agreement shall be replaced with a provision that is
valid and enforceable and most nearly reflects the original intent of
the unenforceable provision.

17\. This Agreement may be executed in two counterparts, each of which
will be deemed to be an original, and all of which, when taken together,
shall be deemed to constitute one and the same agreement.

18\. The relationship between both the Parties to this Agreement shall
be on a principal-to-principal basis and nothing in this agreement shall
be deemed to have created a relationship of an agent or partner between
the Parties and none of the employees of COMPANY shall be considered as
employees of PARTY 1.

19\. This Agreement shall be governed by the laws of India. Both parties
irrevocably submit to the exclusive jurisdiction of the Courts in
Bangalore, for any action or proceeding regarding this Agreement. Any
dispute or claim arising out of or in connection herewith, or the
breach, termination or invalidity thereof, shall be settled by
arbitration in accordance with the provisions of Procedure of the Indian
Arbitration & Conciliation Act, 1996, including any amendments thereof.
The arbitration tribunal shall be composed of a sole arbitrator, and
such arbitrator shall be appointed mutually by the Parties. The place of
arbitration shall be Bangalore, India and the arbitration proceedings
shall take place in the English language.

20\. Additional oral agreements do not exist. All modifications and
amendments to this Agreement must be made in writing.

21\. The Agreement and/or any rights arising from it cannot be assigned
or otherwise transferred either wholly or in part, without the written
consent of the other Party.

**[in witness whereof, the parties hereto have executed this
confidentiality agreement in duplicate by affixing the signature of the
authorised representatives as of the date herein above
mentioned.]{.smallcaps}**

  ---------------- ----------------- -- ----------------- -----------------
  **Party 1**                           **\[*Please fill
                                        in Customer
                                        name*\]**

  **Signature 1**                       **Signature 1**

  Name                                  Name

  Désignations                          Désignations

  Place                                 Place

  Date                                  Date



  **Signature 2**                       **Signature 2**

  Name                                  Name

  Désignations                          Désignations

  Place Date                            Place

  Date                                  Date
  ---------------- ----------------- -- ----------------- -----------------
"""




prompt = """
Can you please generate a list of tone attributes and a description to describe a piece of writing like legal NDA agreement?

Things like pace, mood, etc.

Respond with nothing else besides the list
"""

how_to_interpret_agrrement = llm.predict(prompt)
print (how_to_interpret_agrrement)

def generate_employee_agreement(how_to_interpret_agreement, agreement_template):
    template = """
        You are an AI Bot skilled in understanding and generating employee agreements.
        Use a formal and clear tone.Keep it easy as much as possible.
        Ensure accuracy and clarity in the generated agreement.

        % HOW TO INTERPRET AGREEMENT
        {how_to_interpret_agreement}

        % START OF TEMPLATE
        {agreement_template}
        % END OF TEMPLATE

        Based on the provided interpretation and template, generate a customized employee agreement.
        Ask for more information if needed.
        """

    prompt = PromptTemplate(
        input_variables=["how_to_interpret_agreement", "agreement_template"],
        template=template,
    )

    final_prompt = prompt.format(how_to_interpret_agreement=how_to_interpret_agrrement, agreement_template=agreement_template)

    customized_agreement = llm.predict(final_prompt)

    return customized_agreement

agreement_template = generate_employee_agreement(how_to_interpret_agrrement, agreement_template_demos )

template = """
% INSTRUCTIONS
 - You are an AI Bot skilled in understanding and generating NDA agreements.
 - Your goal is to draft content based on the provided NDA agreement templates and user inputs.
 - Ensure accuracy, clarity, and formality in the generated agreement.
 - Do not use slang, emojis, or informal language.
 - Respond in a professional and clear tone.

% Description of the agreement tone and structure:
{agreement_tone_description}

% Employee agreement template samples:
{agreement_template_samples}

% YOUR TASK
Please draft an NDA agreement based on the provided templates and user inputs. Make sure to ask for any additional information if required.
"""

prompt = PromptTemplate(
    input_variables=["agreement_tone_description", "agreement_template_samples"],
    template=template,
)

# Example usage:
final_prompt = prompt.format(agreement_tone_description="The agreement should be formal, clear, and concise, ensuring all terms and conditions are well-defined.", agreement_template_samples=agreement_template)

@app.get("/")
async def root():
    return {"message": "Hello World"}

#make a route to that take the final_proompt and take a input text and return the llm.predict(final_prompt+ input_text) as a jso
@app.post("/generate-agreement")
async def generate_agreement(input_text: str):
    final_prompt = prompt.format(agreement_tone_description="The agreement should be formal, clear, and concise, ensuring all terms and conditions are well-defined.", agreement_template_samples=agreement_template)
    result = llm.predict(final_prompt + input_text)
    return {"result": result}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


