
export async function load({ fetch, params}) {

    return {
      // -1 to sync question index
      question_id: params.question_id - 1,
      domain: params.domain_id
    };
  }