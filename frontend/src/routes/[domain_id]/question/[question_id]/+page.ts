
export async function load({ fetch, params }) {

    return {
      question_id: params.question_id,
      domain: params.domain_id
    };
  }